#include "ll.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
uint64_t seeks;
uint64_t links;

struct LinkedList {
    uint32_t length;
    Node *head; // Head  sentinel  node.
    Node *tail; // Tail  sentinel  node.
    bool mtf;
};

LinkedList *ll_create(bool mtf) {
    LinkedList *ll = (LinkedList *) malloc(sizeof(LinkedList));
    if (ll) {
        ll->length = 0;
        ll->head = node_create(NULL, NULL);
        ll->tail = node_create(NULL, NULL);
        ll->head->next = ll->tail;
        ll->tail->prev = ll->head;
        ll->mtf = mtf;
    }
    return ll;
}

//Sabrina's section logic but Discord helped me figure out my segmentation fault
void ll_delete(LinkedList **ll) {
    if (*ll) {
        Node *temp = (*ll)->head->next;
        while (temp != NULL) {
            node_delete(&(temp->prev));
            temp = temp->next;
        }
        node_delete(&((*ll)->tail)); //deletes the tail node because it never got freed
        free(*ll);
        *ll = NULL;
    }
}
uint32_t ll_length(LinkedList *ll) {
    return ll->length;
}

//Sabrinas section logic
Node *ll_lookup(LinkedList *ll, char *oldspeak) {
    seeks += 1;
    for (Node *n = ll->head->next; n != ll->tail;
         n = n->next, links += 1) { //Sahiti helped me with the links counter in Office hours
        if (strcmp(n->oldspeak, oldspeak) == 0) {
            if (ll->mtf == 1) {
                n->prev->next = n->next;
                n->next->prev = n->prev;
                n->next = ll->head->next;
                n->prev = ll->head;
                ll->head->next->prev = n;
                ll->head->next = n;
            }
            return n;
        }
    }
    return NULL;
}

//Sabrina's section logic
void ll_insert(LinkedList *ll, char *oldspeak, char *newspeak) {
    if (ll_lookup(ll, oldspeak) != NULL) {
        return;
    }
    Node *nn
        = node_create(oldspeak, newspeak); //nn stands for new node to insert into the linked list
    nn->next = ll->head->next;
    nn->prev = ll->head;
    ll->head->next->prev = nn;
    ll->head->next = nn;
    ll->length += 1;
    return;
}

void ll_print(LinkedList *ll) {
    for (Node *i = ll->head->next; i != ll->tail; i = i->next) { //same iteration as delete ll
        node_print(i);
    }
}
