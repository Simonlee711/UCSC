#include "bm.h"
#include "bv.h"
#include "hamming.h"

#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

#define OPTIONS "hi:o:"

//SOURCE: Darrell Long's Assignment document
//  Returns  the  lower  nibble  of val
uint8_t lower_nibble(uint8_t val) {
    return val & 0xF;
}

//SOURCE: Darell Long's Assignment document
//  Returns  the  upper  nibble  of val
uint8_t upper_nibble(uint8_t val) {
    return val >> 4;
}

int main(int argc, char **argv) {
    int opt = 0;
    FILE *in = stdin, *out = stdout;

    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {
        case 'h':
            printf("SYNOPSIS\n");
            printf("  A Hamming(8, 4) systematic code generator.\n\n");
            printf("USAGE\n");
            printf("  ./encode [-h] [-i infile] [-o outfile]\n\n");
            printf("OPTIONS\n");
            printf("  -h             Program usage and help.\n");
            printf("  -i infile      Input data to encode.\n");
            printf("  -o outfile     Output of encoded data.\n");
            exit(1);
        case 'i':
            if ((in = fopen(optarg, "rb")) == NULL) {
                fprintf(stderr, "failed to open infile\n");
                exit(1);
            }

            break;
        case 'o':
            if ((out = fopen(optarg, "w")) == NULL) {
                fprintf(stderr, "failed to write outfile\n");
                exit(1);
            }
            break;
        }
    }
    //set file permissions
    struct stat statbuf;
    fstat(fileno(in), &statbuf);
    fchmod(fileno(out), statbuf.st_mode);

    //initialzing Generator Matrix

    //       c o l u m n s
    // r  | 1 0 0 0 0 1 1 1 |
    // o  | 0 1 0 0 1 0 1 1 |   4 x 8 Matrix
    // w  | 0 0 1 0 1 1 0 1 |
    // s  | 0 0 0 1 1 1 1 0 |

    BitMatrix *Generator_matrix = bm_create(4, 8);
    bm_set_bit(Generator_matrix, 0, 0);
    bm_set_bit(Generator_matrix, 0, 5);
    bm_set_bit(Generator_matrix, 0, 6);
    bm_set_bit(Generator_matrix, 0, 7);
    bm_set_bit(Generator_matrix, 1, 1);
    bm_set_bit(Generator_matrix, 1, 4);
    bm_set_bit(Generator_matrix, 1, 6);
    bm_set_bit(Generator_matrix, 1, 7);
    bm_set_bit(Generator_matrix, 2, 2);
    bm_set_bit(Generator_matrix, 2, 4);
    bm_set_bit(Generator_matrix, 2, 5);
    bm_set_bit(Generator_matrix, 2, 7);
    bm_set_bit(Generator_matrix, 3, 3);
    bm_set_bit(Generator_matrix, 3, 4);
    bm_set_bit(Generator_matrix, 3, 5);
    bm_set_bit(Generator_matrix, 3, 6);

    // read in a byte from FILE
    //Sahiti's Section logic
    int byte;
    uint8_t msg1;
    uint8_t msg2;
    uint8_t code1;
    uint8_t code2;
    while ((byte = fgetc(in)) != EOF) {
        msg1 = lower_nibble(byte);
        msg2 = upper_nibble(byte);
        code1 = ham_encode(Generator_matrix, msg1);
        fputc(code1, out);
        code2 = ham_encode(Generator_matrix, msg2);
        fputc(code2, out);
    }
    bm_delete(&Generator_matrix);
    fclose(in);
    fclose(out);
}
