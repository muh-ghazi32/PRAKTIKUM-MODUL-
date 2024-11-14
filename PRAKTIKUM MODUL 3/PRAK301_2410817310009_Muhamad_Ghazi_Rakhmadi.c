#include <stdio.h>

int main (){
    int a, b; 

    printf ("Input: ");
    scanf ("%d %d", &a, &b);

    if (a < b) {
        printf("Output: %d %d", a, b);
    } else if (a > b) {
        printf("Output: %d %d", b, a);
    }
    return 0;
    
}