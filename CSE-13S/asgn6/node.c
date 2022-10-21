#include "node.h"

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
Node *node_create(uint8_t symbol, uint64_t frequency) {
    Node *n = (Node *) malloc(sizeof(Node));
    if (!n) {
        return NULL;
    }
    n->left = NULL;
    n->right = NULL;
    n->symbol = symbol;
    n->frequency = frequency;
    return n;
}
void node_delete(Node **n) {
    if (*n) {
        free(*n);
        *n = NULL;
    }
    return;
}

Node *node_join(Node *left, Node *right) {
    Node *nn = node_create('$', left->frequency + right->frequency); //nn for new node
    if (!nn) {
        return NULL;
    }
    nn->left = left;
    nn->right = right;
    return nn;
}

void node_print(Node *n) {
    printf("sym: %c, freq: %lu\n", n->symbol, n->frequency);
}
