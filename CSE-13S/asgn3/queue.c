//Queue implementation
//SOURCES: Darrell Long's slides and assignment doc
//Sources: Eugene's section
//Sources: Sahiti's Section

#include "queue.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct Queue {
    uint32_t head;
    uint32_t tail;
    uint32_t size;
    uint32_t capacity;
    int64_t *items;
};

Queue *queue_create(uint32_t capacity) {
    Queue *q = (Queue *) malloc(sizeof(Queue));
    if (q) {
        q->head = 0; //remove
        q->tail = 0; // insert
        q->size = 0;
        q->capacity = capacity;
        q->items = (int64_t *) malloc(capacity * sizeof(int64_t));
        if (!q->items) {
            free(q);
            q = NULL;
        }
    }
    return q;
}

void queue_delete(Queue **q) {
    if (q) {
        free((*q)->items);
        free(*q);
        *q = NULL;
    }
}

bool queue_empty(Queue *q) {
    return q->size == 0;
}

bool queue_full(Queue *q) {
    return q->size == q->capacity;
}

uint32_t queue_size(Queue *q) {
    return q->size;
}

bool enqueue(Queue *q, int64_t x) {
    if (q) {
        if (queue_full(q)) {
            return false;
        }
        q->size += 1;

        q->items[q->tail] = x;
        q->tail = (q->tail + 1) % q->capacity;
        return true;
    }
    return false;
}

bool dequeue(Queue *q, int64_t *x) {
    if (q->size == 0) {
        return false;
    }
    q->size -= 1;
    *x = q->items[q->head];
    q->head = (q->head + 1) % q->capacity;
    return true;
}

void queue_print(Queue *q) {
    uint32_t index = q->head; //index is head
    while (
        &(q->items[index])
        != &(
            q->items
                [q->tail])) { //while this address of index of the address of tail your gonna keep going
        printf("%" PRId64, q->items[index]); //print current index in the queue
        index = (index + 1) % q->capacity; //increment the index
    }
    printf("%" PRId64, q->items[q->tail]); //prints tail
}
