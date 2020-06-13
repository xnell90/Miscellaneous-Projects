package cartSystem;

import java.io.FileNotFoundException;
import java.util.HashMap;

public class CartSystem extends TheSystem {

	public CartSystem() throws FileNotFoundException {

	}

	public void display() {
		HashMap<String, Item> current = this.getItemCollection();
		Double subTotal = 0.00;

		System.out.println("Item Name, Quantity, Price");
		System.out.println();
		for (String itemName: current.keySet()) {
			System.out.print(itemName + ", ");

			double quantity = (double)current.get(itemName).getQuantity();
			double price = current.get(itemName).getItemPrice();
			System.out.println(quantity + ", " + price);

			subTotal += price * quantity;
		}
		System.out.println();

		System.out.println("SubTotal: " + subTotal);
		System.out.println("Tax: " + (subTotal * 0.05));
		System.out.println("Total: " + (subTotal * 1.05));

	}
}
