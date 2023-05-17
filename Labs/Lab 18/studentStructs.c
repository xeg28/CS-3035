#include <stdio.h>
#include<stdlib.h>

// Initializing the struct for student with its required data types
struct Student {
    char *name;
    int age;
    float gpa;
};

// Creating a funciton prototype 
void printStudents(struct Student *ptr, int size);

int main(void) {
    // initializing an array of Students   
    struct Student students[5] = {
        {"Joe", 20, 3.12},
        {"Jack", 21, 3.5}, 
        {"Emily", 19, 3.9},
        {"Thomas", 23, 3.5},
        {"Maria", 22, 3.2}
    };
    
    // creating a pointer for the students variable
    struct Student *studentsPtr;
    studentsPtr = students;
    
    // Passing in the pointer to the print function
    printStudents(studentsPtr, 5);
    return 0;  
}

void printStudents(struct Student *ptr, int size) {
    for(int i = 0; i < size; i++) {
    //  printing out all of the students with the pointer
        printf("Record: %d\n", i+1);
        printf("Student Name: %s\n", ptr->name);
        printf("Student Age: %d\n", ptr->age);
        printf("Student GPA: %f\n\n", ptr->gpa);
    
    // incrementing the pointer to point to the next student in the array.
        ptr++;
    }
}
