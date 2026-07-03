from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

order_product = Table(
    'order_product',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True)
)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    # Связь 1-to-Many с заказами
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer {self.first_name} {self.last_name}>"

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)

    # Связь Many-to-Many с заказами
    orders = relationship("Order", secondary=order_product, back_populates="products")

    def __repr__(self):
        return f"<Product {self.name} ({self.price} руб.)>"

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.now)
    status = Column(String(20), nullable=False, default='pending')
    total_amount = Column(Float, nullable=False, default=0.0)

    customer = relationship("Customer", back_populates="orders")

    products = relationship("Product", secondary=order_product, back_populates="orders")

    def __repr__(self):
        return f"<Order #{self.id} ({self.status})>"

if __name__ == "__main__":
    engine = create_engine('sqlite:///shop_extended.db', echo=False)
    Base.metadata.create_all(engine)
    print("Таблицы созданы (или уже существуют).")