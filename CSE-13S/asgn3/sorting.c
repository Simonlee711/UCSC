#include "bubble.h"
#include "quick.h"
#include "set.c"
#include "shell.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef enum Sorts {
    Bubblesort,
    Shellsort,
    quicksort,
    QUICKsort,
} Sorts;

const char *names[] = { "Bubblesort", "Shellsort", "quicksort", "QUICKsort" };

#define OPTIONS "absqQr:n:p:"

int main(int argc, char **argv) {
    int opt = 0;
    int seed = 0;
    int size = 0;
    int f_elements = 0;
    uint32_t seeds = 13371453;
    uint32_t elements = 100;
    uint32_t p_elements = 100;

    Set sorts = set_empty();

    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {
        case 'a':
            sorts = set_insert(sorts, Bubblesort);
            sorts = set_insert(sorts, Shellsort);
            sorts = set_insert(sorts, quicksort);
            sorts = set_insert(sorts, QUICKsort);
            break;
        case 'b': sorts = set_insert(sorts, Bubblesort); break;
        case 's': sorts = set_insert(sorts, Shellsort); break;
        case 'q': sorts = set_insert(sorts, quicksort); break;
        case 'Q': sorts = set_insert(sorts, QUICKsort); break;
        case 'r':
            seed = 1;
            seeds = atoi(optarg);
            break;
        case 'n':
            size = 1;
            elements = atoi(optarg);
            break;
        case 'p':
            f_elements = 1;
            p_elements = atoi(optarg);
            break;
        default:
            printf("correct usage %s -[absqQrnp]", argv[0]);
            return 1;
            break;
        }
    }

    //Eugene's Section
    for (Sorts i = Bubblesort; i <= QUICKsort; i += 1) {
        if (set_member(sorts, i)) {
            srandom(seeds);

            //array generating random numbers to be sorted
            uint32_t A[elements];
            for (uint32_t j = 0; j < elements; j++) {
                A[j] = random();
            }

            //Printing Statements;
            uint32_t moves = 0;
            uint32_t compares = 0;
            uint32_t stack_size = 0;
            uint32_t queue_size = 0;
            if (set_member(sorts, Bubblesort)) {
                bubble_sort(&A[0], elements, &moves, &compares);
                printf("Bubble Sort\n");
                printf("%d elements, %d moves, %d compares ", elements, moves, compares);
                for (uint32_t k = 0; k < p_elements; k++) {
                    if (k % 5 == 0) {
                        printf("\n");
                    }
                    printf("%13" PRIu32, A[k]);
                }
                printf("\n");
            }
            if (set_member(sorts, Shellsort)) {
                shell_sort(&A[0], elements, &moves, &compares);
                printf("Shell Sort\n");
                printf("%d elements, %d moves, %d compares ", elements, moves, compares);
                for (uint32_t k = 0; k < p_elements; k++) {
                    if (k % 5 == 0) {
                        printf("\n");
                    }
                    printf("%13" PRIu32, A[k]);
                }
                printf("\n");
            }
            if (set_member(sorts, quicksort)) {
                quick_sort_stack(&A[0], elements, &moves, &compares, &stack_size);
                printf("Quick Sort (Stack)\n");
                printf("%d elements, %d moves, %d compares\n", elements, moves, compares);
                printf("Max stack size: %d", stack_size);
                for (uint32_t k = 0; k < p_elements; k++) {
                    if (k % 5 == 0) {
                        printf("\n");
                    }
                    printf("%13" PRIu32, A[k]);
                }
                printf("\n");
            }
            if (set_member(sorts, QUICKsort)) {
                quick_sort_queue(&A[0], elements, &moves, &compares, &queue_size);
                printf("Quick Sort (Queue)\n");
                printf("%d elements, %d moves, %d compares\n", elements, moves, compares);
                printf("Max queue size: %d", queue_size);
                for (uint32_t k = 0; k < p_elements; k++) {
                    if (k % 5 == 0) {
                        printf("\n");
                    }
                    printf("%13" PRIu32, A[k]);
                }
                printf("\n");
            }
        }
    }
}
