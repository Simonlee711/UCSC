#include "graph.h"

#include "vertices.h"

#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct Graph {
    uint32_t vertices;
    bool undirected;
    bool visited[VERTICES];
    uint32_t matrix[VERTICES][VERTICES];
};
//SOUCRE Eugene's section
Graph *graph_create(uint32_t vertices, bool undirected) {
    Graph *G = (Graph *) malloc(sizeof(Graph));
    if (G) {
        G->vertices = vertices;
        G->undirected = undirected;
        for (uint32_t i = 0; i < vertices; i++) {
            G->visited[i] = false;
            for (uint32_t j = 0; j < vertices; j++) {
                G->matrix[i][j] = 0;
            }
        }
    }
    return G;
}

void graph_delete(Graph **G) {
    if (*G) {
        free(*G);
        *G = NULL;
    }
    return;
}

uint32_t graph_vertices(Graph *G) {
    return G->vertices;
}

bool graph_add_edge(Graph *G, uint32_t i, uint32_t j, uint32_t k) {
    if ((G != NULL) && ((i < G->vertices) && (j < G->vertices))) {
        G->matrix[i][j] = k; //i goes to j
        if (G->undirected == true) {
            G->matrix[j][i] = k; // j goes to i
        }
        return true;
    }
    return false;
}

bool graph_has_edge(Graph *G, uint32_t i, uint32_t j) {
    if (G->matrix[i][j] == 0) {
        return false;
    }
    return true;
}
uint32_t graph_edge_weight(Graph *G, uint32_t i, uint32_t j) {
    if (graph_has_edge(G, i, j)) {
        return G->matrix[i][j];
    }
    return 0;
}

bool graph_visited(Graph *G, uint32_t v) {
    if (v >= G->vertices) {
        return false;
    }
    return G->visited[v];
}

void graph_mark_visited(Graph *G, uint32_t v) {
    if (v >= G->vertices)
        return;
    G->visited[v] = true;
}

void graph_mark_unvisited(Graph *G, uint32_t v) {
    if (v >= G->vertices)
        return;
    G->visited[v] = false;
}

void graph_print(Graph *G) {
    for (uint32_t i = 0; i < G->vertices; i++) {
        for (uint32_t j = 0; j < G->vertices; j++) {
            printf("%u ", G->matrix[i][j]);
        }
        printf("\n");
    }
}
