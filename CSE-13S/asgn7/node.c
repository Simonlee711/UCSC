#include "node.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

//strdup function - Sabrina's section
char *str_dup(char *string) {
    //seg faults if you allocate space for a null value. MUST HAVE THIS CHECK
    //caused me alot of time feeling dumb >:(
    if (string == NULL) {
        return NULL;
    }
    char *pointer; //intializing empty pointer to return
    uint32_t length = strlen(string) + 1; //jloritz from discord helped me here
    pointer = (char *) malloc(length);
    strcpy(pointer, string);
    return pointer;
}

Node *node_create(char *oldspeak, char *newspeak) {
    Node *n = (Node *) malloc(sizeof(Node));
    if (n) {
        n->oldspeak = str_dup(oldspeak);
        n->newspeak = str_dup(newspeak);
        n->next = NULL;
        n->prev = NULL;
    }
    return n;
}

void node_delete(Node **n) {
    if ((*n) && ((*n)->oldspeak) && ((*n)->newspeak)) {
        free((*n)->newspeak);
        free((*n)->oldspeak);
        free(*n);
        *n = NULL;
    }
    return;
}

void node_print(Node *n) {
    if (n->oldspeak != NULL && n->newspeak != NULL) {
        printf("%s -> %s\n", n->oldspeak, n->newspeak);
    } else {
        printf("%s\n", n->oldspeak);
    }
}
