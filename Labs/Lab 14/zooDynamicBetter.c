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
    char **zoo = malloc(sizeof(char *) * n);
    
    for(int i = 0; i < 3; i++) {
        // allocating memory for the size of each animal
        zoo[i] = (char *)malloc(sizeof(animals[i]) * sizeof(char));
        // coping to the array
        strcpy(zoo[i], animals[i]);
     	
    }
    zoo[n-1] = (char *)malloc(sizeof(animals[3]) * sizeof(char));
    strcpy(zoo[n-1], animals[3]);
    
    
    for(int i = 0; i < n; i++) {
        // printing out every animal of the array in their position
        printf("%d: %s\n", i, zoo[i]);
        
        // I freed up the memory locations of each animal, don't know if this is required
        free(zoo[i]);
        zoo[i]=NULL;
    }
        
        free(zoo);
        zoo = NULL;
    
    return 0;
}


