

public class HelpfulJohn {
	public static void main(String[] args) {
	//  Creating new instance of the John class
		John john = new John();
		
	//  Calling all the methods from the John class
	/*	john.mowLawn("Tom");
		john.fixCar("Eric", "Corolla");
		john.paintHouse("Emily");
	*/
		john.privateTasks();	
		
	}
}

// A class containing the methods that print out a sentence about what john is doing
// and who he's doing for.
class John {
	
	public void mowLawn(String neighbor) {
		System.out.println("John is mowing "+ neighbor +"'s lawn.");
	}
	
	public void fixCar(String neighbor, String carModel) {
		System.out.println("John is fixing "+ neighbor +"'s " + carModel + ".");
	}
	
	public void paintHouse(String neighbor) {
		System.out.println("John is painting " + neighbor + "'s house.");
	}
	
    // callling the private methods
	public void privateTasks() {
		laundry();
		cook("pizza");
		research();
	}
	
	private void laundry() {
		System.out.println("John is doing laundry.");
	}
	
	private void cook(String food) {
		System.out.println("John is making " + food + '.');
	}
	
	private void research() {
		System.out.println("John is doing research");
	}
	
}
