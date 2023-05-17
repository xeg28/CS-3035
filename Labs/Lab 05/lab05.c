#include <stdio.h>

int main(void) {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);
    
    printf("\n");
    if(num % 2 == 0) {
    	printf("You entered an even number.\n");
    }
    else {
        printf("You entered an odd number.\n");
    }
    
    return 0;
}
