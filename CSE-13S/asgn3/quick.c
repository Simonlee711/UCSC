//2 quick sorting algorithms
//SOURCES Darrell Long's Python Pseudocode
#include "quick.h"

#include "queue.h"
#include "stack.h"

#include <stdbool.h>
#include <stdio.h>

int64_t partition(uint32_t *A, int64_t lo, int64_t hi) {
    int64_t pivot = A[lo + ((hi - lo) / 2)];
    int64_t i = lo - 1;
    int64_t j = hi + 1;
    while (i < j) {
        i += 1;
        //*compares += 1;
        while (A[i] < pivot) {
            //*compares += 1;
            i += 1;
        }
        j -= 1;
        while (A[j] > pivot) {
            j -= 1;
            //*compares += 1;
        }
        if (i < j) {
            int64_t temp = A[j];
            A[j] = A[i];
            A[i] = temp;
            //*moves += 2;
        }
    }
    return j;
}

void quick_sort_stack(
    uint32_t *A, uint32_t n, uint32_t *moves, uint32_t *compares, uint32_t *stack_size) {
    int64_t lo = 0;
    int64_t hi = n - 1;
    Stack *make_stack = stack_create(n);
    stack_push(make_stack, lo);
    stack_push(make_stack, hi);
    *moves += 1;
    *compares += 1;
    *stack_size += 2;
    while (!stack_empty(make_stack)) {
        stack_pop(make_stack, &hi);
        stack_pop(make_stack, &lo);
        *moves += 2;
        *stack_size -= 2;
        uint32_t p = partition(A, lo, hi);
        *compares += 9;
        *moves += 1;
        if (lo < p) {
            stack_push(make_stack, lo);
            stack_push(make_stack, p);
            *compares += 1;
            *moves += 2;
            *stack_size += 2;
        }
        if (hi > p + 1) {
            stack_push(make_stack, p + 1);
            stack_push(make_stack, hi);
            *compares += 1;
            *moves += 2;
            *stack_size += 2;
        }
    }

    stack_delete(&make_stack);
}

void quick_sort_queue(
    uint32_t *A, uint32_t n, uint32_t *moves, uint32_t *compares, uint32_t *queue_size) {
    int64_t lo = 0;
    int64_t hi = n - 1;
    Queue *make_queue = queue_create(n);
    enqueue(make_queue, lo);
    enqueue(make_queue, hi);
    *queue_size += 2;
    *moves += 1;
    *compares += 1;
    while (!queue_empty(make_queue)) {
        dequeue(make_queue, &lo);
        dequeue(make_queue, &hi);
        *queue_size -= 2;
        *moves += 2;
        uint32_t p = partition(A, lo, hi);
        *compares += 9;
        *moves += 1;
        if (lo < p) {
            *moves += 1;
            enqueue(make_queue, lo);
            enqueue(make_queue, p);
            *queue_size += 2;
        }
        if (hi > p) {
            *moves += 1;
            enqueue(make_queue, p + 1);
            enqueue(make_queue, hi);
            *queue_size += 2;
        }
    }

    queue_delete(&make_queue);
}
