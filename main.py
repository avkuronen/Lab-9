#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hardware_part = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Integer)

@app.route('/')
def main():
    products_list = Product.query.all()
    return render_template('index.html',
       products_list=products_list,
       products_list_length = len(products_list))


@app.route('/add', methods=['POST'])
def add_product():
    data = request.json
    db.session.add(Product(**data))
    db.session.commit()
    return {'message': 'Product added'}


@app.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    db.session.delete(Product.query.get(product_id))
    db.session.commit()
    return {'message': 'Product deleted'}

@app.route('/delete', methods=['DELETE'])
def delete_all_products():
    db.session.query(Product).delete()
    db.session.commit()
    return {'message': 'Products deleted'}


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
