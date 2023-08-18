from item import Item
    
class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones: int = 0) -> None:
        
        
        # call super function to access all attributes / methods of parent class
        super().__init__(name=name, price=price, quantity=quantity) 
        
        #validation upon recceive arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} should be greater than or equal to zero!"

        # Assign attributes to self object
        self.broken_phones = broken_phones