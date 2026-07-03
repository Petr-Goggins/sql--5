# queries_extended.py
from models_extended import Base, Customer, Product, Order, order_product
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///shop_extended.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


print("\n1. Все заказы клиента 'Иван Петров' (ID, дата, статус, сумма):")
customer_ivan = session.query(Customer).filter_by(first_name="Иван", last_name="Петров").first()
if customer_ivan:
    for order in customer_ivan.orders:
        print(f"   Заказ #{order.id} от {order.order_date.strftime('%Y-%m-%d %H:%M')}, "
            f"статус: {order.status}, сумма: {order.total_amount} руб.")
else:
    print("   Клиент не найден.")

print("\n2. Все товары в заказах со статусом 'pending' (название, цена, категория):")
pending_orders = session.query(Order).filter_by(status="pending").all()
if pending_orders:
    products_set = set()
    for order in pending_orders:
        for product in order.products:
            products_set.add((product.name, product.price, product.category))
    for name, price, category in products_set:
        print(f"   {name} — {price} руб., категория: {category}")
else:
    print("   Нет заказов со статусом 'pending'.")

print("\n3. Клиенты, заказавшие товары из категории 'Электроника' (имя, фамилия, email):")
electronics_customers = (
    session.query(Customer)
    .join(Customer.orders)          
    .join(Order.products)           
    .filter(Product.category == "Электроника")
    .distinct()
    .all()
)
if electronics_customers:
    for c in electronics_customers:
        print(f"   {c.first_name} {c.last_name} — {c.email}")
else:
    print("   Нет клиентов, заказавших электронику.")

print("\n4. Все заказы, в которых есть товар 'Смартфон' (ID заказа, дата, статус, имя клиента):")
product_smartphone = session.query(Product).filter_by(name="Смартфон").first()
if product_smartphone:
    for order in product_smartphone.orders:
        print(f"   Заказ #{order.id} от {order.order_date.strftime('%Y-%m-%d %H:%M')}, "
            f"статус: {order.status}, клиент: {order.customer.first_name} {order.customer.last_name}")
else:
    print("   Товар 'Смартфон' не найден.")

print("\n5. Общая сумма всех заказов для каждого клиента (имя, фамилия, общая сумма):")
result = (
    session.query(
        Customer.first_name,
        Customer.last_name,
        func.sum(Order.total_amount).label("total_spent")
    )
    .join(Customer.orders)  
    .group_by(Customer.id)
    .all()
)
for first_name, last_name, total in result:
    print(f"   {first_name} {last_name} — {total:.2f} руб.")

session.close()
print("\nВсе запросы выполнены.")