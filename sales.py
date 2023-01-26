class Sale():
    def __init__(self, id_sales, product_id, product_name, model, description, quantity_in_stock, price, date_of_sale):
        self.id_sales = id_sales  
        self.product_id = product_id  
        self.product_name = product_name  
        self.model = model   
        self.description = description  
        self.quantity_in_stock = quantity_in_stock  
        self.price = price   
        self.date_of_sale = date_of_sale    
        
    def toDBCollection(self):
        return{
            'id_sales': self.id_sales,
            'product_id': self.product_id,
            'product_name': self.product_name,
            'model': self.model,
            'description': self.description,
            'quantity_in_stock': self.quantity_in_stock,  
            'price': self.price,
            'date_of_sale': self.date_of_sale
        }  