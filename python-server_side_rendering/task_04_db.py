from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def itemps():
    with open('items.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        items = donnees["items"]
        return render_template('items.html', items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == "json":
        products = load_from_json()
    elif source == "csv":
        products = load_from_csv()
    elif source == "sql":
        products = load_from_db()
    else:
        error = ("Wrong source")

    if product_id is not None:
        p_id = int(product_id)
        filtered = [p for p in products if p["id"] == p_id]
        if not filtered:
            error = "Product not found"
            products = []
        else:
            products = filtered

    return render_template('product_display.html',
                           products=products,
                           error=error)


def load_from_json(path="products.json"):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return (data)


def load_from_csv(path="products.csv"):
    products = []
    with open(path, 'r', newline="", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            id = int(row["id"])
            price = float(row["price"])
            name = row["name"]
            category = row["category"]
            products.append({"id": id, "price": price,
                            "name": name, "category": category})

    return products


def load_from_db(path="products.db"):
    conn = None
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        products = []
        for row in rows:
            id = int(row[0])
            name = row[1]
            category = row[2]
            price = float(row[3])
            products.append({"id": id, "price": price,
                             "name": name, "category": category})

        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
