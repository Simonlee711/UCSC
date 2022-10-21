#include "bm.h"

#include "bv.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
struct BitMatrix {
    uint32_t rows;
    uint32_t cols;
    BitVector *vector;
};
//SGT William Dai helped us with how much to calloc
BitMatrix *bm_create(uint32_t rows, uint32_t cols) {
    BitMatrix *m = (BitMatrix *) calloc(1, sizeof(BitMatrix));
    if (m) {
        m->rows = rows;
        m->cols = cols;
        m->vector = bv_create(m->rows * m->cols);
        if (!m->vector) {
            free(m);
            m = NULL;
        }
    }

    return m;
}

//similar to my stack implementation
void bm_delete(BitMatrix **m) {
    if (*m && (*m)->vector) {
        free((*m)->vector);
        free(*m);
        *m = NULL;
    }
}

uint32_t bm_rows(BitMatrix *m) {
    return m->rows;
}

uint32_t bm_cols(BitMatrix *m) {
    return m->cols;
}
//Brians sections pseudo code inspired: using r * n + c equation
void bm_set_bit(BitMatrix *m, uint32_t r, uint32_t c) {
    bv_set_bit(m->vector, r * (m->cols) + c);
    return;
}
//Brian's sections pseudo code inspired: using r * n  + c equation
void bm_clr_bit(BitMatrix *m, uint32_t r, uint32_t c) {
    bv_clr_bit(m->vector, r * (m->cols) + c);
    return;
}

//Brian's sections pseudo code inspired: using r * n + c equation
uint8_t bm_get_bit(BitMatrix *m, uint32_t r, uint32_t c) {
    return bv_get_bit(m->vector, r * (m->cols) + c);
}

//Sahiti's section pseudo code inspired
BitMatrix *bm_from_data(uint8_t byte, uint32_t length) {
    BitMatrix *bm = bm_create(1, length);
    for (uint32_t i = 0; i < length; i++) {
        if (byte & (1 << i)) {
            bv_set_bit(bm->vector, i);
        } else {
            bv_clr_bit(bm->vector, i);
        }
    }
    return bm;
}

//tutor Eric helped me out here
uint8_t bm_to_data(BitMatrix *m) {
    uint32_t data = 0;
    for (int i = 0; i < 8; i++) {
        if (bm_get_bit(m, 0, i) == 1) {
            data = (data | (0x1 << i));
        } else {
            continue;
        }
    }
    return data;
}

//Sahiti's section logic + lecture inspired
uint8_t product = 0;
BitMatrix *bm_multiply(BitMatrix *A, BitMatrix *B) {
    BitMatrix *new_matrix = bm_create(A->rows, B->cols);
    for (uint32_t i = 0; i < A->rows; i++) {
        for (uint32_t j = 0; j < B->cols; j++) {
            for (uint32_t k = 0; k < new_matrix->cols; k++) {
                product = bm_get_bit(A, i, k) & bm_get_bit(B, k, j);
                bv_xor_bit(new_matrix->vector, i * (new_matrix->cols) + j, product);
            }
        }
    }
    return new_matrix;
}

void bm_print(BitMatrix *m) {
    for (uint32_t r = 0; r < m->rows; r++) {
        for (uint32_t c = 0; c <= (m->cols - 1); c++) {
            printf("%u", bm_get_bit(m, r, c));
        }
        printf("\n");
    }
}
