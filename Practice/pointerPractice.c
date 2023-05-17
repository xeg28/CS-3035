#include <stdio.h>
#include <stdlib.h>

void pointer(int*);

int main() {
    int **p;
    int a[10] = {1,2,3,4,5,6,7,8,9,10};
    p = (int**) malloc(sizeof(int*)*10);
    
    for(int i = 0; i < 10; i++) {
        p[i] = (int*)malloc(sizeof(int));
        *p[i] = a[i];
        printf("%d\n", *p[i]);
        free(p[i]);
        p[i] = NULL;
    }
    
    
    free(p);
    p=NULL;
    return 0;
}

void pointer(int *pointer) {
    *pointer = 100;
}
