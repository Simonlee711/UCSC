#include "code.h"
#include "defines.h"
#include "header.h"
#include "huffman.h"
#include "io.h"
#include "node.h"
#include "pq.h"
#include "stack.h"

#include <fcntl.h>
#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

#define OPTIONS "hi:o:v"

uint64_t bytes_read;
uint64_t bytes_written;
static uint8_t bytes = 0;
static uint64_t hist[ALPHABET];

void LIpt(Node *root, Stack **s) { //Leaf and Internal Post Traversal
    if (root == NULL) { //->left == NULL && root->right == NULL){
        return;
    }
    LIpt(root->left, s);
    LIpt(root->right, s);
    if (root->left == NULL && root->right == NULL) {
        Node *L = node_create('L', 0);
        stack_push(*s, L);
        stack_push(*s, root);
    }
    if (root->left != NULL && root->right != NULL) {
        Node *I = node_create('I', 0);
        stack_push(*s, I);
    }
}

int main(int argc, char **argv) {
    int opt = 0;
    int in = STDIN_FILENO, out = STDOUT_FILENO;
    int verbose = 0;
    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {
        case 'h':
            printf("SYNOPSIS\n");
            printf("  A Huffman encoder.\n");
            printf("  Compresses a file using the Huffman coding algorithm.\n\n");
            printf("USAGE\n");
            printf("  ./encode [-h] [-v] [-i infile] [-o outfile]\n\n");
            printf("OPTIONS\n");
            printf("  -h             Program usage and help.\n");
            printf("  -v             Print compression statistics.\n");
            printf("  -i infile      Input file to compress.\n");
            printf("  -o outfile     Output of compressed data.\n");
            exit(1);
        case 'i': in = open(optarg, O_RDONLY); break;
        case 'o': out = open(optarg, O_WRONLY | O_CREAT | O_TRUNC); break;
        case 'v': verbose = 1; break;
        }
    }

    //make histogram
    //SOURCE: Proffessor Long's example from class to construct histogram
    int length = 0;
    uint8_t buffer[BLOCK];
    while ((length = read(in, buffer, sizeof(BLOCK)) > 0)) {
        bytes += length;
        for (int i = 0; i < length + 1; i++) {
            hist[buffer[i]] += 1;
        }
    }
    hist[0] += 1;
    hist[255] += 1;

    //build tree
    Node *huffman_tree = build_tree(hist);

    //construct codes
    Code table[ALPHABET];
    for (int i = 0; i < ALPHABET; i++) {
        table[i] = code_init();
    }
    build_codes(huffman_tree, table);

    //counter for leaf's
    int leaf_counter = 0;
    for (int k = 0; k < ALPHABET; k++) {
        if (hist[k] != 0) {
            leaf_counter += 1;
        }
    }

    //header
    struct stat statbuf;
    fstat(in, &statbuf);
    fchmod(out, statbuf.st_mode);

    Header h;
    h.magic = MAGIC; //change to -> if dot notation doesn't work
    h.permissions = statbuf.st_mode;
    h.tree_size = ((3 * leaf_counter) - 1);
    h.file_size = statbuf.st_size;
    write_bytes(out, (uint8_t *) &h, sizeof(h));

    //build the Leaf and internal post traversal array
    Stack *s = stack_create(h.tree_size);
    uint8_t arr[h.tree_size];
    LIpt(huffman_tree, &s);
    Node *temp;
    for (int i = h.tree_size - 1; i >= 0; i--) {
        stack_pop(s, &temp);
        arr[i] = temp->symbol;
        node_delete(&temp);
    }
    write_bytes(out, arr, sizeof(arr));

    //write out to outfile
    lseek(in, 0, SEEK_SET);
    uint8_t bit;
    uint64_t byte_counter = 0;
    uint64_t bit_counter = 0;
    for (uint64_t sym = 0; sym < h.file_size; sym++) {
        read_bytes(in, &bit, 1);
        if (table[bit].top != 0) {
            write_code(out, &table[bit]);
        }
        bit_counter += code_size(&table[bit]);
    }
    flush_codes(out);

    //calculating bytes compressed
    if (bit_counter <= 8) {
        byte_counter = 1;
    } else {
        if ((bit_counter % 8) == 0) {
            byte_counter = bit_counter / 8;
        } else {
            byte_counter = (bit_counter / 8) + 1;
        }
    }

    //verbose printing
    if (verbose) {
        printf("uncompressed file size: %lu\n", h.file_size);
        double total = sizeof(h) + sizeof(arr) + byte_counter;
        printf("compressed file size: %0.0f\n", total);
        double all_bytes = h.file_size;
        printf("Space saving: %0.2f%%\n", (1.0 - (total / all_bytes)) * 100.0);
    }

    //close files
    close(in);
    close(out);
}
