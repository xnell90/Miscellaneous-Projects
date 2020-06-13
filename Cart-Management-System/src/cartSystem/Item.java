package cartSystem;

public class Item{

    private String itemName;
    private String itemDesc;
    private Double itemPrice;
    private Integer quantity;
    private Integer availableQuantity;
    /**
     * @return the itemName
     */
    public Item() {
    	this.quantity = 1;
    }

    public void setItemName(String itemName) {
    	this.itemName = itemName;
    }

    public void setItemDesc(String itemDesc) {
    	this.itemDesc = itemDesc;
    }

    public void setItemPrice(Double itemPrice) {
    	this.itemPrice = itemPrice;
    }

    public void setQuantity(Integer quantity) {
    	this.quantity = quantity;
    }

    public void setAvailableQuantity(Integer availableQuantity) {
    	this.availableQuantity = availableQuantity;
    }

    public String getItemName() {
    	return this.itemName;
    }

    public String getItemDesc() {
    	return this.itemDesc;
    }

    public Double getItemPrice() {
    	return this.itemPrice;
    }

    public Integer getQuantity() {
    	return this.quantity;
    }

    public Integer getAvailableQuantity() {
    	return this.availableQuantity;
    }




}
