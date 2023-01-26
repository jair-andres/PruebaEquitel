from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from product import Product
from sales import Sale
from datetime import date, datetime
import random

db = dbase.dbConnection()

app = Flask(__name__)

"""@app.route('/')
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)

@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']
    
    if name and price and quantity:
        product = Product(name, price, quantity)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'price' : price,
            'quantity' : quantity,
        })
        return redirect(url_for('home'))
    else:
        return notFound()

@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('home'))

@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']
    
    if name and price and quantity:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'price' : price, 'quantity' : quantity}})
        response = jsonify({'message' : 'Producto ' + product_name + ' actualizada correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()
"""
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }      
    response = jsonify(message)
    response.status_code = 404
    return response

@app.route('/sales')
def showSales():
    products = db['products']
    productsReceived = products.find()
    return render_template('sales.html', products = productsReceived)

@app.route('/sale/<string:product_id>')
def salesNew(product_id):
    products = db['products']
    result = products.find_one({"product_id" : product_id})
    
    id_sales = str(random.randint(1, 101)) + "_" + product_id
    product_id = result["product_id"]
    product_name = result["product_name"]
    model = result["model"]
    description = result["description"]
    quantity_in_stock = result["quantity_in_stock"]
    price = result["price"]
    state = result["state"]
    date_of_sale = datetime.now()
    
    sales = db['sales']
    
    if id_sales and product_id and product_name and product_name and model and description and quantity_in_stock and price and date_of_sale:
        sale = Sale(id_sales, product_id, product_name, model, description, quantity_in_stock, price, date_of_sale)
        sales.insert_one(sale.toDBCollection())
        response = jsonify({
            'id_sales': id_sales,
            'product_id' : product_id,
            'product_name' : product_name,
            'model' : model,
            'description' : description,
            'quantity_in_stock' : quantity_in_stock,
            'price' : price,
            'date_of_sale': date_of_sale
        })
        
    quantity_in_stock_update = int(quantity_in_stock) - 1
    
    if quantity_in_stock_update < 1:
        state = "OUT OF STOCK"
    
    if product_id and product_name and model and description and quantity_in_stock and state and price:
        products.update_one({'product_id' : product_id}, {
            '$set' : 
                {
                    'quantity_in_stock' : quantity_in_stock_update, 
                    'state' : state
                }
            })
        return redirect(url_for('showSales'))
    else:
        return notFound()

@app.route('/')
def showProduct():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)

@app.route('/report')
def showReport():
    sales = db['sales']
    reportReceived = sales.find()
    return render_template('report.html', reports = reportReceived)
    
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    product_id = request.form['product_id']
    product_name = request.form['product_name']
    model = request.form['model']
    description = request.form['description']
    quantity_in_stock = request.form['quantity_in_stock']
    state = "AVAILABLE"
    price = request.form['price']
    
    if product_id and product_name and model and description and quantity_in_stock and state and price:
        product = Product(product_id, product_name, model, description, quantity_in_stock, state, price)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'product_id' : product_id,
            'product_name' : product_name,
            'model' : model,
            'description' : description,
            'quantity_in_stock' : quantity_in_stock,
            'state' : state,
            'price' : price
        })
        return redirect(url_for('showProduct'))
    else:
        return notFound()

@app.route('/delete/<string:product_id>')
def deleteProduct(product_id):
    products = db['products']
    products.delete_one({'product_id' : product_id})
    return redirect(url_for('showProduct'))

@app.route('/edit/<string:product_id>', methods=['POST'])
def editProduct(product_id):
    products = db['products']
    product_name = request.form['product_name']
    model = request.form['model']
    description = request.form['description']
    quantity_in_stock = request.form['quantity_in_stock']
    price = request.form['price']
    
    if int(quantity_in_stock) == 0:
        state = "OUT OF STOCK"
    else:
        state = "AVAILABLE"
    
    if product_name and model and model and description and price:
        products.update_one({'product_id' : product_id}, {
            '$set' : 
                {
                    'product_name' : product_name, 
                    'model' : model, 
                    'description' : description,
                    'quantity_in_stock' : quantity_in_stock, 
                    'state' : state, 
                    'price' : price,
                }
            })
        response = jsonify({'message' : 'Producto ' + product_id + ' actualizada correctamente'})
        return redirect(url_for('showProduct'))
    else:
        return notFound()

if __name__ == '__main__':
    app.run(debug=True, port=4000)