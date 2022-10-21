#include "bf.h"
#include "bv.h"
#include "ht.h"
#include "ll.h"
#include "messages.h"
#include "node.h"
#include "parser.h"
#include "speck.h"

#include <ctype.h>
#include <inttypes.h>
#include <regex.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

#define ONE_KB 1024
//Eugene covered alot of regex and helped me figure this out
#define VALID_WORD "[A-Za-z0-9]+(('|-)[A-Za-z0-9]+)*"
#define OPTIONS    "ht:f:ms"
uint64_t links;
uint64_t seeks;

int main(int argc, char **argv) {
    int opt = 0;
    uint64_t ht_cur_size = 10000;
    uint64_t bf_cur_size = 1048576;
    int statistics = 0;
    int mtf = 0;
    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {
        case 'h':
            printf("SYNOPSIS\n");
            printf("  A word filtering program for the GPRSC.\n");
            printf("  Filters out and reports bad words parsed from stdin.\n\n");
            printf("USAGE\n");
            printf("  ./banhammer [-hsm] [-t size] [-f size]\n\n");
            printf("OPTIONS\n");
            printf("  -h           Program usage and help.\n");
            printf("  -s           Print program statistics.\n");
            printf("  -m           Enable move-to-front rule.\n");
            printf("  -t size      Specify hash table size (default: 10000).\n");
            printf("  -f size      Specify Bloom filter size (default: 2^20).\n");
            return 0;
        case 't':
            ht_cur_size = atoi(optarg); //from asgn3
            if (ht_cur_size < 10000) {
                printf("failed to allocate memory for hash table\n");
                return 0;
            }
            break;
        case 'f':
            bf_cur_size = atoi(optarg); //from asgn3
            if (bf_cur_size < 1048576) {
                printf("failed to allocate memory for bloom filter\n");
                return 0;
            }
            break;
        case 'm': mtf = 1; break;
        case 's': statistics = 1; break;
        }
    }
    //Brians section logic
    //create hash table and bloom filter
    HashTable *ht = ht_create(ht_cur_size, mtf);
    if (ht == NULL) {
        printf("failed to allocate memory for hash table\n");
        return 0;
    }

    BloomFilter *bf = bf_create(bf_cur_size);
    if (bf == NULL) {
        printf("failed to allocate memory for Bloom Filter\n");
        return 0;
    }
    //read in badspeak and newspeak
    FILE *badspeak = fopen("badspeak.txt", "r");
    if (badspeak == NULL) {
        printf("invalid file: Badspeak\n");
        return 0;
    }

    FILE *newspeak = fopen("newspeak.txt", "r");
    if (newspeak == NULL) {
        printf("invalid file: Newspeak\n");
        return 0;
    }

    //intializing buffers - Eugene said to make buffers size of 1KB
    char buffer_badspeak[ONE_KB] = { 0 };
    char buffer_oldspeak[ONE_KB] = { 0 };
    char buffer_newspeak[ONE_KB] = { 0 };

    //reading in badspeak file and inserting words into bf and ht
    while (fscanf(badspeak, "%s\n", buffer_badspeak) != EOF) {
        bf_insert(bf, buffer_badspeak);
        ht_insert(ht, buffer_badspeak, NULL);
    }
    //reading in from newspeak putting in old and newspeak translations
    while (fscanf(newspeak, "%s %s", buffer_oldspeak, buffer_newspeak) != EOF) {
        bf_insert(bf, buffer_oldspeak);
        ht_insert(ht, buffer_oldspeak, buffer_newspeak);
    }

    //create linked lists to store badwords and oldwords
    LinkedList *forbidden_words = ll_create(mtf);
    LinkedList *replaceable_words = ll_create(mtf);

    //make a compiling regex - Eugene answered my question here and helped me here
    regex_t regex;
    if (regcomp(&regex, VALID_WORD, REG_EXTENDED)) {
        printf("Compiling Regex has failed\n");
        return 0;
    }

    //begin looping through word and parsing them and seeing if they are badword or oldword
    char *word = NULL;
    uint32_t bad_word_counter = 0;
    uint32_t old_word_counter = 0;
    while ((word = next_word(stdin, &regex)) != NULL) {
        //Eugene told us to loop through because you need to lower each character
        for (uint32_t i = 0; i < strlen(word); i += 1) {
            word[i] = tolower(word[i]);
        }
        //if word not in bloom filter it is neither a badword or oldword
        if (bf_probe(bf, word) == false) {
            continue;
        }
        //perform a lookup to distinguish if bad speak or old speak
        Node *bad_old = ht_lookup(ht, word);
        //if there is a translation you can replace it to its newspeak translation
        if (bad_old->newspeak != NULL) {
            old_word_counter += 1;
            ll_insert(replaceable_words, bad_old->oldspeak, bad_old->newspeak);
        }
        //if there is no translation you know its a badspeak word
        if (bad_old->newspeak == NULL) {
            bad_word_counter += 1;
            ll_insert(forbidden_words, bad_old->oldspeak, bad_old->newspeak);
        }
    }

    //for printing statistics of the program
    if (statistics == 1) {
        printf("Seeks: %lu\n", seeks);
        float avg = ((float) links) / ((float) seeks);
        printf("Average seek length: %0.6f\n", avg);
        float ht_pct = (((float) ht_count(ht)) / ((float) ht_size(ht))) * 100.0;
        printf("Hash Table load: %f%%\n", ht_pct);
        float bf_pct = (((float) bf_count(bf)) / ((float) bf_size(bf))) * 100.0;
        printf("Bloom filter load: %0.6f%%\n", bf_pct);
        return 0;
    }

    //messages per situation
    //situation 1 - fix oldspeak and make them newspeak
    if ((old_word_counter > 0) && (bad_word_counter == 0)) {
        printf("%s", goodspeak_message);
        ll_print(replaceable_words);
    }
    //situation 2 - bad words only send em to Joycamp
    if ((old_word_counter == 0) && (bad_word_counter > 0)) {
        printf("%s", badspeak_message);
        ll_print(forbidden_words);
    }
    //situation 3 - mix of both old speak and bad speak. Warning is given out
    if ((old_word_counter > 0) && (bad_word_counter > 0)) {
        printf("%s", mixspeak_message);
        ll_print(forbidden_words);
        ll_print(replaceable_words);
    }

    //close files and free memory
    fclose(badspeak);
    fclose(newspeak);

    clear_words();
    regfree(&regex);

    bf_delete(&bf);
    ht_delete(&ht);

    ll_delete(&forbidden_words);
    ll_delete(&replaceable_words);
    return 0;
}
