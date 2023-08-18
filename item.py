import csv


class Item:
    
    #class attribute
    pay_net = 0.8 #This pay after 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        """This is a constructor

        Args:
            name (str): Product Name
            price (float): Product Price
            quantity (int, optional): Product Quantity. Defaults to 0.
        """
        #validation upon recceive arguments
        assert price >=0, f"Price {price} should be greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} should be greater than or equal to zero!"

        # Assign attributes to self object
        self.__name = name  #private attribute (Encapsulation)
        self.__price = price
        self.quantity = quantity
        
        #actions to execute
        Item.all.append(self)

    @property # Property Decorator = Read-Only Attribute
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> str | None:
        # sourcery skip: raise-specific-error
        """This is a setter method 

        Args:
            value (str): Any String less than 10 Character

        Returns:
            str | None: Error or 
        """
        if len(value) > 10:
            raise Exception(f"{value} can not be exceed 10 characters")
        else:
            self.__name = value
    
    @property
    def price(self) -> float:
        return self.__price
    
    def apply_discount(self) -> float:
        """This is method to update the price after discount

        Returns:
            float: return dicounted price
        """
        self.__price = self.__price * self.pay_net
    
    def apply_increment(self, increment_value: float) -> None:
        """This is method to increase price based on increment value

        Args:
            increment_value (float): increment value
        """
        
        self.__price = self.__price + self.__price * increment_value
        
        
    def calculation_price(self) -> float:
        """This is a method to calculate total price

        Returns:
            float: total price based on quantity and price
        """
        return self.price * self.quantity
    
    
    
    @classmethod
    def instantiate_from_csv(cls) -> None:
        """This is a classmethod by using decorator which is create object from the csv file
        """
        with open(file='items.csv', mode='r') as f:
            reader = csv.DictReader(f=f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')), 
                quantity=int(item.get('quantity'))
                )
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False  

    def __repr__(self) -> str:
        """This is a magic method to display all the objects 

        Returns:
            str: display all the objects
        """
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"
 