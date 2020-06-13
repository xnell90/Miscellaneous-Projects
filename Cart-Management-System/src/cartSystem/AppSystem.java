package cartSystem;

import java.io.FileNotFoundException;
import java.util.HashMap;

public class AppSystem extends TheSystem {
    public AppSystem() throws FileNotFoundException {

    }

    public void display() {
        HashMap<String, Item> current = this.getItemCollection();

        System.out.println("Item Name, Available Quantity, Price");

        for(String itemName: current.keySet()) {
        	System.out.print(itemName + ", ");
        	System.out.print(current.get(itemName).getAvailableQuantity() + ", ");
        	System.out.println(current.get(itemName).getItemPrice());
        }

    }

    public Boolean add(Item item) {
    	HashMap<String, Item> current = this.getItemCollection();
    	String itemName = item.getItemName();

    	for(String keyItemName: current.keySet()) {
    		if (keyItemName.equals(itemName)) {
        		System.out.print(itemName + " is already in the ");
        		System.out.println(getClass().getSimpleName());

        		return false;
        	}
    	}

    	return super.add(item);
    }
}
