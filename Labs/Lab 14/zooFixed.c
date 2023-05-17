#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // pointer to the zoo array
    char *zoo[5] = {"Monkey", "Zebra", "Lion", "Elephant", "Snake"};
    
    //prints out animals in the zoo array.
    for(int i = 0; i < 5;i++) {
    	printf("%s ", zoo[i]);
    }
    printf("\n");
  	
    return 0;
}
