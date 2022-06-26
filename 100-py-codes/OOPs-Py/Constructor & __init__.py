class Item:
    def __init__(self, name:str, price:float, quantity=0):
        # Run validation to the received args
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"qty {quantity} is mot greater or equal to zero"

        # Assign to self object
        self.name = name 
        self.price = price
        self.quantity = quantity  
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 2)
item2 = Item("Laptop", 1000, 3)
 
# item2.has_numpad = False

print(item1.calculate_total_price())
print(item2.calculate_total_price())