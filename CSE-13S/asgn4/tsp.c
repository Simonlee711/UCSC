//Sources: Eric Hernandez Section
#include "graph.h"
#include "path.h"
#include "vertices.h"

#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define OPTIONS "hvui:o:"

//dfs algorithm based on Professor's pseudocode
void dfs(Graph *G, uint32_t v, Path *curr, Path *shortest, char *cities[], FILE *out, bool verbose,
    uint32_t *recur_count) {
    path_push_vertex(curr, v, G);

    if (path_vertices(curr) == graph_vertices(G)) { // checking to see if it is shortest path
        if ((path_length(curr) < path_length(shortest)) || (path_length(shortest) == 0)) {
            path_copy(shortest, curr);
        }
    }

    if (path_vertices(curr) == graph_vertices(G)) { //checking if verbose
        if (verbose) {
            fprintf(out, "Path length: %u\n", path_length(curr));
            fprintf(out, "Path: ");
            path_push_vertex(curr, START_VERTEX, G);
            path_print(curr, out, cities);
        }
    }
    graph_mark_visited(G, v);
    for (uint32_t w = 0; w < graph_vertices(G); w += 1) {
        if (graph_has_edge(G, v, w)) {
            if (graph_visited(G, w) == false) {
                *recur_count += 1;
                dfs(G, w, curr, shortest, cities, out, verbose, recur_count);
            }
        }
    }
    graph_mark_unvisited(G, v);
    path_pop_vertex(curr, &v, G);
}

int main(int argc, char **argv) {
    FILE *in = stdin, *out = stdout; //source Eugene
    int opt = 0;
    uint32_t vertices;
    bool undirected = false;
    bool verbose = false;

    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {
        case 'h':
            printf("SYNOPSIS\n");
            printf("  Traveling Salesman Problem using DFS.\n\n");
            printf("USAGE\n");
            printf("  ./tsp [-u] [-v] [-h] [-i infile] [-o outfile]\n\n");
            printf("OPTIONS\n");
            printf("  -u             Use undirected graph.\n");
            printf("  -v             Enable verbose printing.\n");
            printf("  -h             Program usage and help.\n");
            printf("  -i infile      Input containing graph (default: stdin)\n");
            printf("  -o outfile     Output of computed path (default: stdout)\n");
            return 0;
        case 'u': undirected = true; break;
        case 'v': verbose = true; break;

        case 'i':
            //SOURCE Eric Hernandez section
            if ((in = fopen(optarg, "r")) == NULL) {
                fprintf(stderr, "failed to open infile\n");
                exit(1);
            }
            break;
        case 'o':
            //SOURCE Eric Hernandez section
            if ((out = fopen(optarg, "w")) == NULL) {
                fprintf(stderr, "failed to write outfile\n");
                exit(1);
            }
            break;
        }
    }
    //Tutor Eric Hernandez code
    fscanf(in,
        "%u"
        " ",
        &vertices);
    char buffer[1024];
    char *cities[vertices];

    for (uint32_t c_count = 0; c_count < vertices; c_count += 1) {
        fgets(buffer, 1024, in);
        cities[c_count] = strdup(buffer);
    }
    Graph *G = graph_create(vertices, undirected);
    uint32_t i, j, k;
    while (fscanf(in, "%u %u %u", &i, &j, &k) != EOF) {
        graph_add_edge(G, i, j, k);
    }

    //creating two paths
    Path *curr = path_create();
    Path *shortest = path_create();
    uint32_t recur_count = 1;
    dfs(G, START_VERTEX, curr, shortest, cities, out, verbose, &recur_count);
    path_push_vertex(shortest, START_VERTEX, G);
    fprintf(out, "Path length: %u\n", path_length(shortest));
    fprintf(out, "Path: ");
    path_print(shortest, out, cities);
    fprintf(out, "Total Recursive Calls: %u\n", recur_count);
}
