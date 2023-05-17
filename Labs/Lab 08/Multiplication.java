public class Multiplication {
    public static void main(String[] args) {
        System.out.println(multiply(4, 7)); // demonstrating method overloading
        System.out.println(multiply(3.14, 10.0)); // demonstrating method overloading
        System.out.println(multiply(4,7, 2)); // demonstrating method overloading
        System.out.println(multiply(3.14, 10.0, 2.0)); // demonstrating method overloading
    }
    
    public static int multiply(int x, int y) { // multiplies two integers
        return x * y;  
    }
    
    public static int multiply(int x, int y, int z) { // multiplies three integers
    	return x * y * z;
    }
    
    public static double multiply(double x, double y) { // multiplies two doubles
    	return x * y; 
    }
    
    public static double multiply(double x, double y, double z) { // multiplies three doubles
    	return x * y * z;
    }
}
