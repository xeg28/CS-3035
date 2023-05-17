#include <stdio.h>

int yearsBetween(int, int);

int main(void) {
    int year1;
    int year2;
    
    printf("Enter two years: ");
    
    // Takes to integers as input
    scanf("%d %d", &year1, &year2);
    
    printf("The years between is %d.\n", yearsBetween(year1, year2));

    return 0;       
}

int yearsBetween(int year1, int year2) {
         // Decides which year to subtract first
    return (year1>year2) ? year1 - year2 : year2 - year1;
}


