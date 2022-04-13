class RetailItem: 
    def __init__(self, Description='', UnitOnHand=0, Price=0): 
        self.Description = Description 
        self.UnitOnHand = UnitOnHand 
        self.Price = Price 
    def InventoryValue(self): 
        return (self.UnitOnHand * self.Price) 
inventoryfile = open("10.02 Inventory.txt","r")
inventorylist = []
x = inventoryfile.readline()
while x !="":
    description, unit_on_hand, price = x.split(",")
    item = RetailItem(description, int(unit_on_hand), float(price))
    inventorylist.append(item)
    x = inventoryfile.readline()
print("{:>20s}{:>20s}{:>20s}{:>20s}".format("Description","Units On Hand","Price","Inventory Value"))
for i in range(len(inventorylist)):
    print("{:>20s}{:>20d}{:>20.2f}{:>20.2f}".format(inventorylist[i].Description,inventorylist[i].UnitOnHand,inventorylist[i].Price,inventorylist[i].InventoryValue()))

print() # Add an extra blank line for readability