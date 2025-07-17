from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def load_items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            return data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_json_products():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def read_csv_products():
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert string values to appropriate types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except (FileNotFoundError, csv.Error, ValueError):
        return None

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
def items():
    items_list = load_items()
    return render_template('items.html', items=items_list)

@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    
    # Read data based on source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    
    # Handle file reading errors
    if products is None:
        return render_template('product_display.html', 
                               error=f"Error reading {source} file or file not found.")
    
    # Filter by ID if specified
    if product_id is not None:
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html',
                                   error=f"Product with ID {product_id} not found.")
        products = filtered_products
    
    return render_template('product_display.html', products=products, source=source)


if __name__ == '__main__':
    app.run(debug=True, port=5000)