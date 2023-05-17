#include <stdio.h>
//const int a = 1;
int a = 25;
int b = 100;

//Calculates the percentage of b that a represents.
double whatPercentage(void) {
    //Uses the global variables a and b
    return 100.0 * (double)a / (double)b; 
}

int main(void) {
    //Prints out the result of the whatPercentage method.
    printf("%d is %lf%% of %d.\n",a, whatPercentage(), b);
    a = 13;
    b = 20;
    //Printing out gives a different result because I changed values of the global variables.
    printf("%d is %lf%% of %d.\n",a, whatPercentage(), b);
    
    /*Trying to run the code with const int a = 1, it gives an error because I try to redefine a
    in the main method*/
    return 0;
}
