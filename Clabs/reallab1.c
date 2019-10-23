#include <stdio.h>
#include <math.h>

int main(void) {
    float a, x, g, f, y;
    printf("Vvedite a: ");
    scanf("%f", &a);
    printf("Vvedite x: ");
    scanf("%f", &x);
    g = -10*(18*a*a+11*a*x-24*x*x)/(-a*a+a*x+6*x*x);
    printf("G=%f\n\n", g);

    printf("Vvedite a: ");
    scanf("%f", &a);
    printf("Vvedite x: ");
    scanf("%f", &x);
    f = cos(21*a*a-34*a*x+9*x*x);
    printf("F=%f\n\n", f);

    printf("Vvedite a: ");
    scanf("%f", &a);
    printf("Vvedite x: ");
    scanf("%f", &x);
    y = log(3*a*a-25*a*x+8*x*x+1)/log(10);
    printf("Y=%f\n\n", y);
}
