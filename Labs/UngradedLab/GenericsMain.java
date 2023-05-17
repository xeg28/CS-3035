
public class GenericsMain {
    public static void main(String[] args) {
        PublicIdentifier<String> stringID = new PublicIdentifier<>("Emmanuel");
        PublicIdentifier<Integer> integerID = new PublicIdentifier<>(314159265);
        
        stringID.printUser();
        integerID.printUser();
           
    }    
}

class PublicIdentifier<E> {
    private E id;
    
    public PublicIdentifier(E id) {
        this.id = id;
    }
    
    public void printUser() {
        System.out.println("User ID: " + this.id);
    } 
}
