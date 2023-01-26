class Product:
    def __init__(self, product_id, product_name, model, description, quantity_in_stock, state, price):
        self.product_id = product_id  
        self.product_name = product_name  
        self.model = model   
        self.description = description  
        self.quantity_in_stock = quantity_in_stock 
        self.state = state 
        self.price = price    
        
    def toDBCollection(self):
        return{
            'product_id': self.product_id,
            'product_name': self.product_name,
            'model': self.model,
            'description': self.description,
            'quantity_in_stock': self.quantity_in_stock,
            'state': self.state,
            'price': self.price
        }  





 