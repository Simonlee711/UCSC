#include "mathlib.h"

#include <assert.h>
#include <math.h>
#include <stdio.h>

#define EPSILON 1e-10

static inline double Abs(double x) {
    double pos;
    if (x < 0.0) {
        pos = x * -1.0;
    } else {
        pos = x * 1.0;
    }
    return pos;
}

//SOURCE: Piazza Darell Long's Exp Function
static double Exp(double x) {
    double term = 1, sum = 1;
    for (int k = 1; Abs(term) > EPSILON; k += 1) {
        term *= x / k;
        sum += term;
    }
    return sum;
}

//SOURCE: Piazza Darell Long's Sqrt Function
static double Sqrt(double x) {
    double y = 1.0;
    assert(x >= 0);
    for (double guess = 0.0; Abs(y - guess) > EPSILON; y = (y + x / y) / 2.0) {
        guess = y;
    }
    return y;
}

//Taylor Series - followed Euegen's sections thought logic
double arcSin(double x) {
    double summation = x;
    double term = x;
    double approx = x;
    double coefficient = 1.0;
    if (x == 1.0) { //no idea why this isn't triggering
        double arccCos = arcCos(Sqrt(1 - (x * x)));
        summation = arccCos * 1;
    } else if (x == -1.0) {
        double arcos = arcCos(Sqrt(1 - (x * x)));
        summation = arcos * -1;
    } else {
        for (double k = 3; Abs(approx) > EPSILON; k += 2) {
            coefficient = coefficient * ((k - 2) / (k - 1));
            term = term * x * x;
            approx = (term / k) * coefficient;
            summation += approx;
        }
    }
    return summation;
}
/*
//Newtons Method - my approximations were very off as they were going farther away from zero
double arcSin(double x) {
   double guess = x;
   double approx = 0.0;
   double fx = sin(guess) - x;
   double dfx = cos(guess);
      for (double i = 0; Abs(guess) > EPSILON; i++){
         approx = guess - (fx/dfx);
	 guess = approx;
         fx = sin(guess) - x;
         dfx = cos(guess);
   } 
   return guess;
}
*/

// simply used an identity to compute arcCos using arcSin
double arcCos(double x) {
    double solution;
    double arccos;
    if (x == 1) { // no idea why this is not triggering either?
        return arcSin(1 - (x * x));
        if (x == -1) {
            double temp = arcSin(x);
            return arccos = (M_PI_2 + temp);
        }
    } else {
        solution = arcSin(x);
        arccos = (M_PI_2 - solution);
        return arccos;
    }
}
// simply used an identity to compute arcTan using arcSin
double arcTan(double x) {
    double equation = (x / (Sqrt(x * x + 1)));
    double arctan;
    arctan = arcSin(equation);
    return arctan;
}

//Newtons Method - SOURCE: Darell Long's lecture. Changed variable names for readability
double Log(double x) {
    double guess = 1.0;
    double fx = Exp(guess);
    while (Abs(fx - x) > EPSILON) {
        guess = guess + (x - fx) / fx;
        fx = Exp(guess);
    }
    return guess;
}
