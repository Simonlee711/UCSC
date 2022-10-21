#include "code.h"

#include "defines.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

Code code_init(void) {
    Code c;
    c.top = 0;
    for (uint32_t i = 0; i < MAX_CODE_SIZE; i++) {
        c.bits[i] = 0;
    }
    return c;
}

//from asgn5
void set_bit(Code *c, uint32_t i) {
    c->bits[i / 8] |= (1 << (i % 8));
    return;
}

//from asgn5
void clr_bit(Code *c, uint32_t i) {
    c->bits[i / 8] &= ~(1 << (i % 8));
    return;
}

//from asgn5
uint8_t get_bit(Code *c, uint32_t i) {
    return (c->bits[i / 8] >> (i % 8)) & 1;
}

uint32_t code_size(Code *c) {
    return c->top;
}

bool code_empty(Code *c) {
    return c->top == 0;
}

bool code_full(Code *c) {
    return c->top == MAX_CODE_SIZE;
}

bool code_push_bit(Code *c, uint8_t bit) {
    if (c->top == MAX_CODE_SIZE) {
        return false;
    }
    if (bit == 1) {
        set_bit(c, c->top);
        c->top += 1;
    }
    if (bit == 0) {
        clr_bit(c, c->top);
        c->top += 1;
    }
    //c->top += 1;
    return true;
}

bool code_pop_bit(Code *c, uint8_t *bit) {
    if (c->top == 0) {
        return false;
    }
    c->top -= 1;
    *bit = get_bit(c, c->top);
    clr_bit(c, c->top);
    return true;
}

/*
void code_print(Code *c) {
    for (uint32_t i = 0; i < code_size(c); i--) {
        printf("code %u iteration %u", get_bit(c, i), i);
    }
    printf("\n");
}
*/

void code_print(Code *c) {
    printf("[");
    for (uint32_t i = 0; i <= ((c->top) / 8); i++) {
        printf("%x", c->bits[i]);
    }
    printf("]\n");
}
/*
int main(void){
   int bit;
   Code c = code_init();
   Code k = code_init();
   code_push_bit(&c, 1);
   printf("code 1 Push: ");
   code_print(&c);
   code_push_bit(&c, 0);
   printf("code 1 Push: ");
   code_print(&c);
   code_push_bit(&k, 1);
   printf("code 2 Push: ");
   code_print(&k);
   code_push_bit(&k, 1);
   printf("code 2 Push: ");
   code_print(&k);
}*/
