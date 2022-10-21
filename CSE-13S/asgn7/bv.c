#include "bv.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct BitVector {
    uint32_t length;
    uint8_t *vector;
};

//same as asgn5
BitVector *bv_create(uint32_t length) {
    BitVector *v = (BitVector *) calloc(1, sizeof(BitVector));
    if (v) {
        v->length = length;
        //uint8_t size = length % 8 == 0 ? (length / 8) : (length / 8) + 1;
        uint32_t size = length;
        v->vector = (uint8_t *) calloc(size, sizeof(uint8_t));
        if (!v->vector) {
            exit(0);
        }
    }
    return v;
}

//same as asgn5
void bv_delete(BitVector **v) {
    if (*v && (*v)->vector) {
        free((*v)->vector);
        free(*v);
        *v = NULL;
    }
}

//same as asgn5
uint32_t bv_length(BitVector *v) {
    return v->length;
}

//same as asgn5
void bv_set_bit(BitVector *v, uint32_t i) {
    v->vector[i / 8] |= (1 << (i % 8));
    return;
}

//same as asgn5
void bv_clr_bit(BitVector *v, uint32_t i) {
    (v->vector[i / 8] &= ~(1 << (i % 8)));
    return;
}

//same as asgn5
uint8_t bv_get_bit(BitVector *v, uint32_t i) {
    return (v->vector[i / 8] >> (i % 8)) & 1;
}

//same as asgn5
void bv_print(BitVector *v) {
    printf("BLOOM FILTER:\n");
    for (int i = 32; i > 0; i--) {
        printf("%d", bv_get_bit(v, i));
    }
}
