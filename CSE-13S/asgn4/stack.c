//Stack implementation
//Sources: Darrell Long's Lecture Slides and Assignment Document
//Sources: Eugene's Section most functions are imported from asgn3 stack.c
//Sources: Sahiti's Section most functions are imported from asgn3 stack.c

#include "stack.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct Stack {
    uint32_t top;
    uint32_t capacity;
    uint32_t *items;
};

Stack *stack_create(uint32_t capacity) {
    Stack *s = (Stack *) malloc(sizeof(Stack));
    if (s) {
        s->top = 0;
        s->capacity = capacity;
        s->items = (uint32_t *) malloc(capacity * sizeof(uint32_t));
        if (!s->items) {
            free(s);
            s = NULL;
        }
    }
    return s;
}

void stack_delete(Stack **s) {
    if (*s && (*s)->items) {
        free((*s)->items);
        free(*s);
        *s = NULL;
    }
    return;
}

uint32_t stack_size(Stack *s) {
    return s->top;
}

bool stack_empty(Stack *s) {
    return s->top == 0;
}

bool stack_full(Stack *s) {
    return s->top == s->capacity;
}

bool stack_push(Stack *s, uint32_t x) {
    s->items[s->top] = x;
    s->top += 1;
    return true;
}

bool stack_pop(Stack *s, uint32_t *x) {
    s->top -= 1;
    *x = s->items[s->top];
    return true;
}
//tutor Eric Hernandez gave us code
bool stack_peek(Stack *s, uint32_t *x) {
    if (stack_empty(s)) {
        return false;
    }
    *x = s->items[s->top - 1];
    return true;
}
//tutor Eric's Hernandez gave us code
void stack_copy(Stack *dst, Stack *src) {
    if (dst != NULL && src != NULL) {
        uint32_t len = src->top;
        for (uint32_t i = 0; i < len; i++) {
            dst->items[i] = src->items[i];
        }
        dst->top = len;
    }
}

void stack_print(Stack *s, FILE *outfile, char *cities[]) {
    for (uint32_t i = 0; i < s->top; i += 1) {
        fprintf(outfile, "%s", cities[s->items[i]]);
        if (i + 1 != s->top) {
            fprintf(outfile, "->");
        }
    }
    fprintf(outfile, "\n");
}
