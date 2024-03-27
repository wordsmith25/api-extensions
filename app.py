from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL Configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'laravel-test-wordsmith'

mysql = MySQL(app)
CORS(app)

@app.route('/add-product', methods=['POST'])
def add_product():
    data = request.json
    asin = data.get('asin')
    title = data.get('title')
    author = data.get('author')
    publisher = data.get('publisher')
    isbn10 = data.get('isbn10')
    isbn13 = data.get('isbn13')
    description = data.get('description')
    binding = data.get('binding')
    edition = data.get('edition')
    numberOfPages = data.get('numberOfPages')
    dimensions = data.get('dimensions')
    weight = data.get('weight')
    publishDate = data.get('publishDate')
    language = data.get('language')
    customerRating = data.get('customerRating')
    numberOfReviews = data.get('numberOfReviews')
    rankNumber = data.get('rankNumber')
    category1 = data.get('category1')
    category2 = data.get('category2')
    category3 = data.get('category3')
    lexileLevel = data.get('lexileLevel')
    image = data.get('image')
    
    cur = mysql.connection.cursor()
    query = """
    INSERT INTO AsinFetch 
    (asin, title, edition, category1, category2, category3, lexileLevel, author, publisher, isbn10, isbn13, description, customerRating, numberOfReviews, publishDate, language, dimensions, weight, binding, numberOfPages, rankNumber, image) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(query, (asin, title, edition, category1, category2, category3, lexileLevel, author, publisher, isbn10, isbn13, description, customerRating, numberOfReviews, publishDate, language, dimensions, weight, binding, numberOfPages, rankNumber, image))
    mysql.connection.commit()
    cur.close()
    # print(data)
    
    return jsonify({'message': 'Ürün başarıyla eklendi'}), 201


if __name__ == '__main__':
    app.run(debug=True)

