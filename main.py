from item import Item
#creating object
# item1 = Item(name='Egg', price=2, quantity=10)
# item2 = Item(name='Milk', price=1.19, quantity=4)

# print(item1.calculation_price())
# print(item2.calculation_price())

# print all attributes of class and objects 
# print(Item.__dict__)
# print(item1.__dict__)

# Item.instantiate_from_csv()

# phone1 = Phone(name='Iphone14',price=1000, quantity=4, broken_phones=1)
item1 = Item(name='hi', price=10)

# setting an atrribute value
item1.name = 'hello'
item1.apply_increment(increment_value=0.2)

# getting attribute
print(item1.name)
print(item1.price)
# print(Item.all)
# print(Phone.all)  