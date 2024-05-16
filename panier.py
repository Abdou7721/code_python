class Panier:
    def __init__(self, id):
        self.cart = []
        self.id = id
    
    def __str__(self) -> str:
        return f"{self.id}, {self.cart}"