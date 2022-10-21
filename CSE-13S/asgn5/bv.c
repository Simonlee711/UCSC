#include "bv.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

//SGT Tutoring William Dai helped us make BitVector

struct BitVector {
    uint32_t length;
    uint8_t *vector;
};

//Sahiti's section taught us how to give too much memory using a turnary operator
BitVector *bv_create(uint32_t length) {
    BitVector *v = (BitVector *) calloc(1, sizeof(BitVector));
    if (v) {
        v->length = length;
        uint8_t size = length % 8 == 0 ? length / 8 : (length / 8) + 1;
        v->vector = (uint8_t *) calloc(size, sizeof(uint8_t));
        if (!v->vector) {
            exit(0);
        }
    }
    return v;
}

//similar to stack implementation
void bv_delete(BitVector **v) {
    if (*v && (*v)->vector) {
        free((*v)->vector);
        free(*v);
        *v = NULL;
    }
}

uint32_t bv_length(BitVector *v) {
    return v->length;
}

//Eugene's section, Darrell Long's lecture
void bv_set_bit(BitVector *v, uint32_t i) {
    v->vector[i / 8] |= (1 << (i % 8));
    return;
}

//Eugene's section, Darrell Longs lecture
void bv_clr_bit(BitVector *v, uint32_t i) {
    (v->vector[i / 8] &= ~(1 << (i % 8)));
    return;
}

void bv_xor_bit(BitVector *v, uint32_t i, uint8_t bit) {
    (v->vector[i / 8] ^= (bit << (i % 8)));
    return;
}

//Eugene's section, Darrell Longs Lecture
uint8_t bv_get_bit(BitVector *v, uint32_t i) {
    return (v->vector[i / 8] >> (i % 8)) & 1;
}
//debugging funciton
void bv_print(BitVector *v) {
    for (int i = 32; i > 0; i--) {
        printf("%d", bv_get_bit(v, i));
    }
}
