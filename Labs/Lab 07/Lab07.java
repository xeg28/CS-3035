public class Lab07 {
    public static void main(String[] args) {
	FlowerBouquet flower1 = new FlowerBouquet("Lily", "white");
	FlowerBouquet flower2 = flower1;
	FlowerBouquet flower3 = new FlowerBouquet("Rose", "red");
	
	System.out.println(flower1.whichFlower() + "\n");
	
	System.out.println("Flower1 equals flower2: " + flower1.sameFlower(flower2)); 
	System.out.println("Flower1 equals flower3: " + flower1.sameFlower(flower3)); 
    }
}

class FlowerBouquet {
    String flowerName;
    String flowerColor;
    
    public FlowerBouquet(String name, String color) {
    	flowerName = name;
    	flowerColor = color;
    }
    
    public String whichFlower() {
    	return "This flower is a " + flowerColor + " colored " + flowerName + ".";
    }
    
    public boolean sameFlower(FlowerBouquet flower) {
    	return (flowerName == flower.flowerName && flowerColor == flower.flowerColor);
    }
}

