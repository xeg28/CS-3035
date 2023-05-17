#include <stdio.h>

void swap(int *x, int *y);

int main(void) {
    // initializing integer variables
    int x=2;
    int y=3;
    // initializing pointers to the variables' address
    int *ptnX = &x;
    int *ptnY = &y; 
    
    // printing out the values before the swap
    printf("This is x before the swap: %d\n", x);
    printf("This is y before the swap: %d\n\n", y);
    
    //passing in the pointers from the swap
    swap(ptnX, ptnY);
    
    // printing out the values after the swap
    printf("This is x after the swap: %d\n", x);
    printf("This is y after the swap: %d\n", y);
}

void swap(int *x, int *y) {
    // creating a temp variable to store the value of pointer x so it is not lost
    int temp = *x;
    
    // setting the values of pointer x to the value of pointer y
    *x = *y;
    // setting the values of pointer y to the temp variable which contains the value of pointer x
    *y = temp;
}
