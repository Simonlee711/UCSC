#include "pq.h"

#include "node.h"

#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct PriorityQueue {
    uint32_t capacity;
    uint32_t size;
    Node **arr;
    uint32_t head;
    uint32_t tail;
};

PriorityQueue *pq_create(uint32_t capacity) {
    PriorityQueue *q = (PriorityQueue *) malloc(sizeof(PriorityQueue));
    if (!q) {
        return NULL;
    }
    q->capacity = capacity;
    q->size = 0;
    q->head = 0;
    q->tail = 0;
    q->arr = calloc(capacity, sizeof(Node *));
    if (!q->arr) {
        free(q);
        q = NULL;
    }
    return q;
}
void pq_delete(PriorityQueue **q) {
    if (q) {
        free((*q)->arr);
        free(*q);
        *q = NULL;
    }
}

bool pq_empty(PriorityQueue *q) {
    return q->size == 0;
}

bool pq_full(PriorityQueue *q) {
    return q->size == q->capacity;
}

uint32_t pq_size(PriorityQueue *q) {
    return q->size;
}

//erics pseudocode
bool enqueue(PriorityQueue *q, Node *n) {
    if (pq_full(q)) {
        return false;
    }
    q->size += 1;
    q->arr[q->tail] = n;
    q->tail = (q->tail + 1) % q->capacity;
    int curr = q->tail - 1;
    for (uint32_t i = curr; i > q->head;
         --i) { //should be comparing with 2nd to last element in the pq
        if ((q->arr[curr]->frequency) < (q->arr[curr - 1]->frequency)) {
            Node *temp = q->arr[curr];
            q->arr[curr] = q->arr[curr - 1];
            q->arr[curr - 1] = temp;
        }
    }
    return true;
}

bool dequeue(PriorityQueue *q, Node **n) { //look this over
    if (q->size == 0) {
        return false;
    }
    q->size -= 1;
    *n = q->arr[q->head];
    q->head = (q->head + 1) % q->capacity;
    return true;
}

void pq_print(PriorityQueue *q) {
    for (uint32_t i = 0; i < q->size; i++) {
        printf("symb! %u freq %lu\n", q->arr[i]->symbol, q->arr[i]->frequency);
    }
}
