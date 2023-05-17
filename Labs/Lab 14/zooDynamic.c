#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void) {
    int n;
    //prompting user input
    printf("Enter the number of animals for the zoo. \n");
    scanf("%d", &n);
    
    // input validation
    while(n < 4) {
    	printf("Enter a integer greater than 3.\n");
    	scanf("%d", &n);
    }
    // aimmals in the zoo
    char *animals[4] = {"Monkey", "Tiger", "Gorilla", "Giraffe"};
    
    // initializing the pointer to the array of size n
    char *zoo[n];
    
    for(int i = 0; i < 4; i++) {
        // allocating memory for the size of each animal
        zoo[i] = (char *)malloc(sizeof(animals[i]) * sizeof(char));
        // coping to the array
        strcpy(zoo[i], animals[i]);
     	
    }
    
    for(int i = 0; i < 4; i++) {
        // printing out every animal of the array in their position
        printf("%d: %s\n", i, zoo[i]);
        
        // I freed up the memory locations of each animal, don't know if this is required
        free(zoo[i]);
        zoo[i]=NULL;
    }
    
    return 0;
}


