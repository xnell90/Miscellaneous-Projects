package cartSystem;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class TheSystem {
    private HashMap<String, Item> itemCollection;

    protected TheSystem() throws FileNotFoundException {
        itemCollection = new HashMap<String, Item>();

       if (getClass().getSimpleName().equals("AppSystem")) {
    	   File sampleFile = new File("sample.txt");
    	   Scanner scannerFile = new Scanner(sampleFile);

     	   while (scannerFile.hasNextLine()) {
     		   String line = scannerFile.nextLine();
     		   String[] itemAttributes = line.split("  ");

     		   Item item = new Item();
               
     		   item.setItemName(itemAttributes[0]);
     		   item.setItemDesc(itemAttributes[1]);

     		   item.setItemPrice(Double.parseDouble(itemAttributes[2]));
     		   item.setAvailableQuantity(Integer.parseInt(itemAttributes[3]));

     		   itemCollection.put(item.getItemName(), item);
     	   }

    	   scannerFile.close();
       }

    }

    public HashMap<String, Item> getItemCollection(){
    	HashMap<String, Item> systemItemCollection = new HashMap<String, Item>();

    	for(String itemName: this.itemCollection.keySet()) {
    		systemItemCollection.put(itemName, this.itemCollection.get(itemName));
    	}

    	return systemItemCollection;
    }

    public void setItemCollection(HashMap<String, Item> newItemCollection ){
    	this.itemCollection = newItemCollection;
    }

    public Boolean add(Item item) {
      String itemName = item.getItemName();

      for(String currentItemName: itemCollection.keySet()) {

    	  if (currentItemName.equals(itemName)) {

    		  Boolean isAvailable = checkAvailability(itemCollection.get(itemName), 1);

    		  if (isAvailable) {
    			  int quantity = itemCollection.get(itemName).getQuantity();
    			  itemCollection.get(itemName).setQuantity(quantity + 1);
    		  }

    		  return isAvailable;
    	  }

      }
      itemCollection.put(itemName, item);
      return true;
    }

    public Item remove(String itemName) {

        for(String currentItemName: itemCollection.keySet()) {

        	if(currentItemName.equals(itemName)) {
        		Item item = itemCollection.get(itemName);
        		itemCollection.remove(itemName);
        		return item;
        	}

        }

        return null;
    }

    public Boolean checkAvailability(Item item, Integer current) {

    	if (item.getQuantity() + current > item.getAvailableQuantity()) {
    		System.out.print("System is unable to add");
    		System.out.print(" " + (item.getQuantity() + current) + " ");
    		System.out.print(item.getItemName() + "s\n");

    		System.out.print("System can only add " + item.getAvailableQuantity());
    		System.out.print(" " + item.getItemName() + "s\n");

    		return false;
    	}

    	return true;


    }
}
