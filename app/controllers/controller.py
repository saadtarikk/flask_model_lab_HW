from flask import render_template
from app import app
from app.models.order_list import orders


@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)


@app.route('/orders/<index>')
def order_page(index):
    order = orders[int(index)]
    return render_template('order.html', title='Customer Order', order=order)
