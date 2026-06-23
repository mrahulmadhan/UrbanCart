import sqlite3

def get_db():
    conn = sqlite3.connect('urbancart.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            image TEXT NOT NULL,
            category TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            quantity INTEGER DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            product_name TEXT,
            quantity INTEGER,
            total REAL,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    # Seed products only if empty
    if conn.execute('SELECT COUNT(*) FROM products').fetchone()[0] == 0:
        products = [
            ('Wireless Headphones', 1999, 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300', 'Electronics'),
            ('Running Shoes',       1499, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=300', 'Fashion'),
            ('Smart Watch',         2999, 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=300', 'Electronics'),
            ('Backpack',             899, 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=300', 'Accessories'),
            ('Sunglasses',           599, 'https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=300', 'Fashion'),
            ('Laptop Stand',         749, 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=300', 'Electronics'),
        ]
        conn.executemany('INSERT INTO products (name, price, image, category) VALUES (?,?,?,?)', products)

    conn.commit()
    conn.close()