#include <stdio.h> 

int main(void) {
    int max = 0;
    int second = 0;
    int currGrade;
    for(int i = 1; i <= 10; i++) {
    	printf("Enter grade #%d\n", i);
    	scanf("%d", &currGrade);
    	if(max < currGrade) {
    	    second = max;
    	    max = currGrade;
    	    continue; 
    	}
    	if(second < currGrade) {
    	    second = currGrade;
    	}
    }
    
    printf("\nThe highest grade you entered was %d.\n", max);
    printf("The second highest grade you entered was %d.\n", second);
    return 0;
}


/*int main(void) {
    int max = 0;
    int currGrade;
    for(int i = 1; i <= 10; i++) {
    	printf("Enter grade #%d\n", i);
    	scanf("%d", &currGrade);
    	if(max < currGrade) {
    	    max = currGrade; 
    	}
    }
    
    printf("\nThe highest grade you entered was %d.\n", max);
    return 0;
}*/
