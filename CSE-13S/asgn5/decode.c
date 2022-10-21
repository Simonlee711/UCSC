#include "bm.h"
#include "hamming.h"

#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

#define OPTIONS "hi:o:v"

//print the counters

uint8_t pack_byte(uint8_t upper, uint8_t lower) {
    return (upper << 4) | (lower & 0xF);
}

int main(int argc, char **argv) {
    int opt = 0;
    FILE *in = stdin, *out = stdout;
    int verbose = 0;

    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {
        case 'h':
            printf("SYNOPSIS\n");
            printf("  A Hamming(8, 4) systematic code decoder.\n\n");
            printf("USAGE\n");
            printf("  ./decode [-h] [-v] [-i infile] [-o outfile]\n\n");
            printf("OPTIONS\n");
            printf("  -h             Program usage and help.\n");
            printf("  -v             Print statistics of decoding to stderr.\n");
            printf("  -i infile      Input data to decode.\n");
            printf("  -o outfile     Output of decoded data.\n");
            return 0;
        case 'i':
            if ((in = fopen(optarg, "r")) == NULL) {
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
        case 'v': verbose = 1; break;
        }
    }
    //set file permissions
    struct stat statbuf;
    fstat(fileno(in), &statbuf);
    fchmod(fileno(out), statbuf.st_mode);

    // make Ht matrix
    BitMatrix *H_transpose = bm_create(8, 4);
    bm_set_bit(H_transpose, 0, 1);
    bm_set_bit(H_transpose, 0, 2);
    bm_set_bit(H_transpose, 0, 3);
    bm_set_bit(H_transpose, 1, 0);
    bm_set_bit(H_transpose, 1, 2);
    bm_set_bit(H_transpose, 1, 3);
    bm_set_bit(H_transpose, 2, 0);
    bm_set_bit(H_transpose, 2, 1);
    bm_set_bit(H_transpose, 2, 3);
    bm_set_bit(H_transpose, 3, 0);
    bm_set_bit(H_transpose, 3, 1);
    bm_set_bit(H_transpose, 3, 2);
    bm_set_bit(H_transpose, 4, 0);
    bm_set_bit(H_transpose, 5, 1);
    bm_set_bit(H_transpose, 6, 2);
    bm_set_bit(H_transpose, 7, 3);

    //read in file
    //Sahiti's section logic
    int byte;
    int byte2;
    int8_t counter = 0;
    int8_t u_counter = 0;
    int8_t c_counter = 0;
    float error_rate = 0.0;
    uint8_t msg1;
    uint8_t msg2;
    uint8_t data;
    while (((byte = fgetc(in)) != EOF) && ((byte2 = fgetc(in)) != EOF)) {
        ham_decode(H_transpose, byte, &msg1);
        ham_decode(H_transpose, byte2, &msg2);
        if ((ham_decode(H_transpose, byte, &msg1) == HAM_ERR)
            || (ham_decode(H_transpose, byte2, &msg2) == HAM_ERR)) {
            u_counter += 1;
            data = pack_byte(byte2, byte);
            counter += 2;
            fputc(data, out);
            continue;
        }
        if ((ham_decode(H_transpose, byte, &msg1) == HAM_OK)
            || (ham_decode(H_transpose, byte2, &msg2) == HAM_OK)) {
            c_counter += 1;
            data = pack_byte(byte2, byte);
            counter += 2;
            fputc(data, out);
            continue;

        } else {
            data = pack_byte(msg2, msg1);
            counter += 2;
            fputc(data, out);
        }
    }
    error_rate = ((float) u_counter / counter); //discord told me I can float cast
    if (verbose) {
        fprintf(stderr, "Total bytes processed: %d\n", counter);
        fprintf(stderr, "Uncorrected errors: %d\n", u_counter);
        fprintf(stderr, "Corrected error: %d\n", c_counter);
        fprintf(stderr, "Error rate: %f\n", error_rate); //discord told me you can float cast
    }
    bm_delete(&H_transpose);
    fclose(in);
    fclose(out);
}
