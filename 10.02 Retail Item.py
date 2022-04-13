class RetailItem:
    def __init__(self, Description="", UnitsOnHand=0, Price=0):
        self.Description = Description self. Units On Hand = Units On Hand
        self.Price = Price

    def InventoryValue(self):
        return self. UnitsOnHand * self. Price  
    def main():
        with open("10.02 Inventory.txt") as file:
            for line in file: 
                description, units_on_hand, price = line.split(","), retailitem = RetailItem(description, int(units_on_hand), float(price))

print("Description:", retail_item. Description) 
print("Units On Hand:", retail_item. UnitsOnHand) 
print("Price:", retail_item.Price) 
print("Inventory Value:", retail_item.InventoryValue()) 
print() # Add an extra blank line for readability

main()