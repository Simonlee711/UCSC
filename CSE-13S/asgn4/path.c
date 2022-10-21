//SOURCES: Tutor Eric Hernandez's section
#include "path.h"

#include "graph.h"
#include "stack.h"
#include "vertices.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct Path {
    Stack *vertices;
    uint32_t length;
};

Path *path_create(void) {
    Path *p = (Path *) malloc(sizeof(Path));
    if (p) {
        p->length = 0;
        p->vertices = stack_create(VERTICES);
    }
    return p;
}

void path_delete(Path **p) {
    if (*p) {
        stack_delete(&((*p)->vertices));
        free(*p);
        *p = NULL;
    }
    return;
}
bool path_push_vertex(Path *p, uint32_t v, Graph *G) {
    if (stack_full(p->vertices)) {
        return false;
    } else {
        if (stack_empty(p->vertices) == false) {
            uint32_t w;
            stack_peek(p->vertices, &w);
            p->length += graph_edge_weight(G, w, v);
        }
        stack_push(p->vertices, v);
        return true;
    }
}

bool path_pop_vertex(Path *p, uint32_t *v, Graph *G) {
    if (stack_empty(p->vertices)) {
        return false;
    } else {
        stack_pop(p->vertices, v);
        if (stack_empty(p->vertices) == false) {
            uint32_t w;
            stack_peek(p->vertices, &w);
            p->length -= graph_edge_weight(G, w, *v);
        }
        return true;
    }
}

uint32_t path_vertices(Path *p) {
    return stack_size(p->vertices);
}

uint32_t path_length(Path *p) {
    return p->length;
}
//Tutor Eric hernandez, gave us code
void path_copy(Path *dst, Path *src) {
    if (src != NULL && dst != NULL) {
        stack_copy(dst->vertices, src->vertices);
        dst->length = src->length;
    }
    return;
}

void path_print(Path *p, FILE *outfile, char *cities[]) {
    stack_print(p->vertices, outfile, cities);
}
