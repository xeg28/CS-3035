import java.util.Random;
import java.util.Scanner;

public class JaggedArray {
    public static void main(String[] args) {
        Random rand = new Random();
        
        /* Getting user input for number of rows.
           Look at the integerInput method.*/
        System.out.print("Enter the number of rows for the jagged array: ");
        int rows = integerInput(); 
        int[][] jaggedArray = new int[rows][];  
        
        int index = 1;
        
        /* A loop will go through each row and assign a 
           random number of columns to each row. 
        */
        for(int row = 0; row < rows; row++) {
            int columns = rand.nextInt(10);
            jaggedArray[row] = new int[columns];
            
            /* A loop that will go through each item of the 
               array and add the index value. The index value 
               incremented and then the value is printed out.
            */ 
            for(int j = 0; j < columns; j++) {
                jaggedArray[row][j] = index++;
                System.out.print(jaggedArray[row][j] + " ");
            }
            System.out.println();
        }
        
    }   
    
    
    
    public static int integerInput() {
        Scanner input = new Scanner(System.in);
        
        /* Checks if user inputs an integet. If user fails to do so
           it will prompt the user again until an integer until it 
           reads an integer.
        */
        
        while(!input.hasNextInt()) {
            System.out.print ("Enter an integer: ");
            input.next();
        }
        int userInput = input.nextInt(); 
        input.close();
        
        return userInput;
    }

}


/*
  ----- Output 1 -----
    Enter the number of rows for the jagged array: 5
    1 2 3 4 5 6 
    7 8 9 10 11 12 13 14 15 
    16 17 18 19 
    20 21 22 23 24 25 26 
    27 28 29 30 31 32 33 34 35 
    
  ----- Output 2 -----
    Enter the number of rows for the jagged array: 3
    1 2 
    3 
    4 5 6 

*/



