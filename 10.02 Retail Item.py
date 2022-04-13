class RetailItem: 
    def __init__(self, Description, UnitOnHand,Price): 
        self.Description = Description 
        self.UnitOnHand = UnitOnHand 
        self.Price = Price 
    def InventoryValue(self): 
        return (self.UnitOnHand * self.Price) 
    def main():
        file1 = open("10.02 Inventory.txt", "r")
        for line in file1:
            Description, UnitOnHand, Price = line.split(",") 
            retail_item = RetailItem(Description, int(UnitOnHand), float(Price)
           
print("{:>13}{:>13}{:>13}".format("Description", "Units On Hand", "Price", "Inventory Value"))
print("{:>13}{:>13}{:>13}".format(retail_item.Description, retail_item.UnitOnHand, retail_item.Price, retail_item.InventoryValue))

print() # Add an extra blank line for readability

