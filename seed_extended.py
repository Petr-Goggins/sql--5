from models_extended import Base, Customer, Product, Order, order_product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///shop_extended.db', echo=False)
Base.metadata.create_all(engine)  
Session = sessionmaker(bind=engine)
session = Session()

session.query(Order).delete()
session.query(Customer).delete()
session.query(Product).delete()
session.commit()

products_data = [
    {"name": "Ноутбук", "price": 50000, "category": "Электроника"},
    {"name": "Смартфон", "price": 30000, "category": "Электроника"},
    {"name": "Книга", "price": 500, "category": "Литература"},
    {"name": "Футболка", "price": 1500, "category": "Одежда"},
    {"name": "Кофе", "price": 400, "category": "Продукты"},
]
products = []
for p in products_data:
    product = Product(**p)
    products.append(product)
    session.add(product)
session.commit()

# 2. Создаём клиентов
customers_data = [
    {"first_name": "Иван", "last_name": "Петров", "email": "ivan@example.com"},
    {"first_name": "Мария", "last_name": "Иванова", "email": "maria@example.com"},
    {"first_name": "Алексей", "last_name": "Сидоров", "email": "alex@example.com"},
]
customers = []
for c in customers_data:
    customer = Customer(**c)
    customers.append(customer)
    session.add(customer)
session.commit()

customer_ivan = session.query(Customer).filter_by(first_name="Иван", last_name="Петров").first()
customer_maria = session.query(Customer).filter_by(first_name="Мария", last_name="Иванова").first()
customer_alex = session.query(Customer).filter_by(first_name="Алексей", last_name="Сидоров").first()

product_notebook = session.query(Product).filter_by(name="Ноутбук").first()
product_smartphone = session.query(Product).filter_by(name="Смартфон").first()
product_book = session.query(Product).filter_by(name="Книга").first()
product_tshirt = session.query(Product).filter_by(name="Футболка").first()
product_coffee = session.query(Product).filter_by(name="Кофе").first()

order1 = Order(
    customer=customer_ivan,
    status="completed",
    total_amount=50500,
    order_date=datetime.now()
)
order1.products = [product_notebook, product_book]

order2 = Order(
    customer=customer_maria,
    status="pending",
    total_amount=1500,
    order_date=datetime.now()
)
order2.products = [product_tshirt]

order3 = Order(
    customer=customer_alex,
    status="shipped",
    total_amount=400,
    order_date=datetime.now()
)
order3.products = [product_coffee]

order4 = Order(
    customer=customer_ivan,
    status="pending",
    total_amount=30000,
    order_date=datetime.now()
)
order4.products = [product_smartphone]

session.add_all([order1, order2, order3, order4])
session.commit()

print("База данных заполнена связанными данными.")
session.close()