#include "code.h"
#include "defines.h"
#include "header.h"
#include "huffman.h"
#include "io.h"

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

int main(int argc, char **argv) {
    int opt = 0;
    int in = STDIN_FILENO, out = STDOUT_FILENO;
    int verbose = 0;

    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {
        case 'h':
            printf("SYNOPSIS\n");
            printf("  A Huffman decoder.\n");
            printf("  Decompresses a file using the Huffman coding algorithm.\n\n");
            printf("USAGE\n");
            printf("  ./decode [-h] [-v] [-i infile] [-o outfile]\n\n");
            printf("OPTIONS\n");
            printf("  -h             Program usage and help.\n");
            printf("  -v             Print decompression statistics.\n");
            printf("  -i infile      Input file to decompress.\n");
            printf("  -o outfile     Output of decompressed data.\n");
            return 0;
        case 'i': in = open(optarg, O_RDONLY); break;
        case 'o': out = open(optarg, O_WRONLY | O_CREAT); break;
        case 'v': verbose = 1; break;
        }
    }
    //read in header
    Header h = { 0 };
    read_bytes(in, (uint8_t *) &h, sizeof(Header));

    //header check
    if (h.magic != 0xDEADBEEF) {
        fprintf(stderr, "*** Invalid Magic Number ***\n");
        return 0;
    }

    //file permission
    struct stat statbuf;
    fstat(in, &statbuf);
    fchmod(out, statbuf.st_mode);

    //rebuild tree;
    uint8_t dump[h.tree_size];
    read(in, dump, h.tree_size);
    Node *root = rebuild_tree(h.tree_size, dump);

    //decompress the message
    uint8_t bit; // = 0;
    uint64_t pos = 0;
    Node *curr = root;
    uint32_t bits = 0;
    double byte_counter;
    while ((bits = read_bit(in, &bit)) > 0) {
        if (pos == h.file_size + 1) {
            break;
        }
        if (bit == 0) {
            if (curr->left == NULL) {
                write_bytes(out, &(curr->symbol), 1);
                curr = root;
            } else {
                curr = curr->left;
            }
        }
        if (bit == 1) {
            if (curr->right == NULL) {
                write_bytes(out, &(curr->symbol), 1);
                curr = root;
            } else {
                curr = curr->right;
            }
        }
        pos += 1;
    }
    //calculating bytes to decompress
    if ((pos) <= 8) {
        byte_counter = 1;
    } else {
        if (((pos) % 8) == 0) {
            byte_counter = (pos) / 8;
        } else {
            byte_counter = ((pos) / 8) + 1;
        }
    }

    //verbose printing
    if (verbose) {
        printf("compressed file size: %0.0f\n", byte_counter);
        printf("uncompressed file size %lu: \n", h.file_size);
        double all_bytes = h.file_size;
        printf("Space saving: %0.2f%%\n", (1.0 - (byte_counter / all_bytes)) * 100);
    }

    close(in);
    close(out);
}
