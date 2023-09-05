from flask import Blueprint
from flask import render_template
from models.order_list import orders

order_blueprint = Blueprint('order', __name__)

@order_blueprint.route('/orders')
def index():
    return render_template('index.html', title='Order list', orders=orders)

@order_blueprint.route('/orders/<int:order_number>')
def get_order_details(order_number):
    for order in orders:
        if order_number == order.order_number:
            return render_template('order.html', title='Order detail', order=order)
    else:
        return 'Error: order not found'
