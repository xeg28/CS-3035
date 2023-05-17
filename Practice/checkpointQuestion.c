#include <stdio.h>
#include <stdlib.h>

void reverse(int*, int*, int*);

int main(void) {
	int val1=10;
	int val2=100;
	int val3=1000;
	
	printf("%d %d %d\n", val1,val2,val3);
	
	reverse(&val1, &val2, &val3);
	
	printf("%d %d %d\n", val1,val2,val3);
	
	return 0;
}

void reverse(int *p1, int *p2, int *p3) {
	int temp = *p1;
	*p1 = *p3;
	*p3 = temp;
}
