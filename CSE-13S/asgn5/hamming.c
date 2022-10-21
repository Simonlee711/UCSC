#include "bm.h"

#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

//global variables for counting

uint8_t low_nib(uint8_t val) {
    return val & 0xF;
}

typedef enum HAM_STATUS {
    HAM_OK = -3, // No  error  detected.
    HAM_ERR = -2, //  Uncorrectable.
    HAM_CORRECT = -1 //  Detected  error  and  corrected.
} HAM_STATUS;

static int lookup_table[16] = { -2, 4, 5, -2, 6, -2, -2, 3, 7, -2, -2, 2, -2, 1, 0, -2 };

//Sahiti's section logic
uint8_t ham_encode(BitMatrix *G, uint8_t msg) {
    BitMatrix *message = bm_from_data(msg, 4);
    G = bm_multiply(message, G);
    uint8_t code = bm_to_data(G);
    return code;
}

//Sahiti's section logic
HAM_STATUS ham_decode(BitMatrix *Ht, uint8_t code, uint8_t *msg) {
    BitMatrix *the_code = bm_from_data(code, 8);
    BitMatrix *error = bm_multiply(the_code, Ht);
    int look = bm_to_data(error);
    if (lookup_table[look] == -3) {
        *msg = low_nib(code);
        return HAM_OK;
    }
    if (lookup_table[look] == -2) {
        return HAM_ERR;
    }
    if ((lookup_table[look] != -2) && (lookup_table[look] != -3)) {
        if (bm_get_bit(the_code, 1, lookup_table[look]) == 1) {
            bm_clr_bit(the_code, 1, lookup_table[look]);
        }
        if (bm_get_bit(the_code, 1, lookup_table[look]) == 0) {
            bm_set_bit(the_code, 1, lookup_table[look]);
        }
        *msg = low_nib(code);
        return HAM_CORRECT;
    }
    return HAM_CORRECT;
}
