//shell sorting algorithm
// SOURCES: Darrell Long's Python Pseudocode
#include "shell.h"

#include "gaps.h"

#include <stdbool.h>
#include <stdio.h>

void shell_sort(uint32_t *A, uint32_t n, uint32_t *moves, uint32_t *compares) {
    for (uint32_t gap = 0; gap < GAPS; gap++) {
        if (gaps[gap] > n) {
            continue;
        }
        for (uint32_t i = gaps[gap]; i < n; i++) {
            *compares += 1;
            uint32_t j = i;
            *moves += 1;
            uint32_t temp = A[i];
            while (j >= gaps[gap] && temp < A[j - (gaps[gap])]) {
                *compares += 2;
                A[j] = A[j - (gaps[gap])];
                j -= gaps[gap];
                *moves += 2;
            }
            A[j] = temp;
            *moves += 1;
        }
    }
}
