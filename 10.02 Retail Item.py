class RetailItem: 
    def __init__(self, Description, UnitOnHand,Price): 
        self.Description = Description 
        self.UnitOnHand = UnitOnHand 
        self.Price = Price 
    def InventoryValue(self): 
        return (self.UnitOnHand * self.Price) 
    def main():
        with open("10.02 Inventory.txt") as file:
            for line in file:
                description, unit_on_hand, price = line.split(",") 
                retail_item = RetailItem(description, int(unit_on_hand), float(price))
                print("Description:", retail_item.Description) 
                print("Units On Hand:", retail_item.UnitOnHand) 
                print("Price:", retail_item.Price) 
                print("Inventory Value:", retail_item.InventoryValue()) 
                    
                print() # Add an extra blank line for readability
                main()