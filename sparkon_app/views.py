# Import necessary libraries and set up Flask app
from flask import Flask, render_template, request, redirect
import stripe
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'super-secret-key')
stripe.api_key = ''

# Define routes
@app.route('/')
def menu():
    # Display menu items
    menu_items = [
        {'name': 'Pizza', 'price': 10000},
        {'name': 'Burger', 'price': 8.00},
        {'name': 'Salad', 'price': 6.00},
        # add more menu items as needed
    ]
    return render_template('menu.html', menu_items=menu_items)

@app.route('/order/<item_name>/<item_price>')
def order(item_name,item_price):
    # Display order form for selected item
    return render_template('order.html', item_name=item_name,item_price=item_price)

@app.route('/charge', methods=['POST'])
def charge():
    # Process payment using Stripe
    item_name = request.form['item_name']
    amount = request.form['amount']
    

    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Order for ' + item_name
    )
    # Mark order as fulfilled
    # Send notification to customer
    return redirect('/status')

@app.route('/status')
def status():
    # Display order status
    return render_template('status.html')

# Set up websockets to listen for Stripe notifications
# When an order is fulfilled, push notification to customer's browser

if __name__ == '__main__':
    app.run(debug=True)
