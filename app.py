from flask import Flask, render_template, redirect, url_for, request
from database import get_db, init_db

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    conn = get_db()
    existing = conn.execute('SELECT * FROM cart WHERE product_id=?', (product_id,)).fetchone()
    if existing:
        conn.execute('UPDATE cart SET quantity = quantity + 1 WHERE product_id=?', (product_id,))
    else:
        conn.execute('INSERT INTO cart (product_id) VALUES (?)', (product_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    conn = get_db()
    items = conn.execute('''
        SELECT p.name, p.price, p.image, c.quantity, c.id,
               (p.price * c.quantity) AS subtotal
        FROM cart c JOIN products p ON c.product_id = p.id
    ''').fetchall()
    total = sum(item['subtotal'] for item in items)
    conn.close()
    return render_template('cart.html', items=items, total=total)

@app.route('/remove/<int:cart_id>')
def remove(cart_id):
    conn = get_db()
    conn.execute('DELETE FROM cart WHERE id=?', (cart_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    conn = get_db()
    items = conn.execute('''
        SELECT p.name, c.quantity, (p.price * c.quantity) AS subtotal
        FROM cart c JOIN products p ON c.product_id = p.id
    ''').fetchall()
    for item in items:
        conn.execute('INSERT INTO orders (product_name, quantity, total) VALUES (?,?,?)',
                     (item['name'], item['quantity'], item['subtotal']))
    conn.execute('DELETE FROM cart')
    conn.commit()
    conn.close()
    return redirect(url_for('orders'))

@app.route('/orders')
def orders():
    conn = get_db()
    orders = conn.execute('SELECT * FROM orders ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)