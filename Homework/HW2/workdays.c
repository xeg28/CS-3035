#include <stdio.h>

// Creating an enum for the days of the week.
enum daysOfWeek{MON, TUES, WED, THURS, FRI, SAT, SUN};

int main(void) {
    
    int input;
    enum daysOfWeek;
    
    // Asking for user input.
    printf("Enter a day of the week as 0-6: ");
    scanf("%d", &input);
    
    // This switch statement prints out a sentece describing the user input.
    switch(input) {
        case MON:
        case TUES:
        case WED:
        case THURS:
        case FRI:
            printf("It is a workday.\n");
            break;
        case SAT:
        case SUN:
            printf("It is the weekend.\n");
            break;
        default:
            printf("You did not enter one of the correct numbers.\n");
    }
    return 0;
}

/* ----- Output 1 -----
    Enter a day of the week as 0-6: 0
    It is a workday.
    
    ----- Output 2 -----
    Enter a day of the week as 0-6: 5
    It is the weekend.
    
    ----- Output 3 -----
    Enter a day of the week as 0-6: 8
    You did not enter one of the correct numbers.

*/
