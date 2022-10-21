#include "mathlib.h"

#include <math.h>
#include <stdio.h>
#include <unistd.h>

#define OPTIONS "asctl"

int main(int argc, char **argv) {
    int opt = 0;
    int arSin = 0;
    int arCos = 0;
    int arTan = 0;
    int Log_c = 0;

    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {
        case 'a':
            arSin = 1;
            arCos = 1;
            arTan = 1;
            Log_c = 1;
            break;
        case 's': arSin = 1; break;
        case 'c': arCos = 1; break;
        case 't': arTan = 1; break;
        case 'l': Log_c = 1; break;
        default:
            printf("correct usage %s -[asctl]", argv[0]);
            return 1;
            break;
        }
    }

    if (arSin == 1) {
        printf(" x            arcSin           Library        Difference \n");
        printf(" -            ------           -------        ---------- \n");
        for (double x = -1.0000; x <= 1.0; x += 0.10000) {
            printf("% 7.4lf % 16.8lf % 16.8lf % 16.10lf\n", x, arcSin(x), asin(x),
                arcSin(x) - asin(x));
        }
    }
    if (arCos == 1) {
        printf(" x            arcCos           Library        Difference \n");
        printf(" -            ------           -------        ---------- \n");
        for (double i = -1.0; i < 1.0; i += 0.1) {
            printf("% 7.4lf % 16.8lf % 16.8lf % 16.10lf\n", i, arcCos(i), acos(i),
                arcCos(i) - acos(i));
        }
    }
    if (arTan == 1) {
        printf(" x            arcTan           Library        Difference \n");
        printf(" -            ------           -------        ---------- \n");
        for (double i = 1.0; i < 10.0; i += 0.1) {
            printf("% 7.4lf % 16.8lf % 16.8lf % 16.10lf\n", i, arcTan(i), atan(i),
                arcTan(i) - atan(i));
        }
    }
    if (Log_c == 1) {
        printf(" x            Log              Library        Difference \n");
        printf(" -            ------           -------        ---------- \n");
        for (double x = 1.0; x < 10.0; x += 0.1) {
            printf("% 7.4lf % 16.8lf % 16.8lf % 16.10lf\n", x, Log(x), log(x), Log(x) - log(x));
        }
    }
    return 0;
}
