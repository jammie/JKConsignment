from app import db
from models import address_model, billing_model, user_model, purchase_order_model, product_model

class Order(db.Model): 

  __tablename__ = 'orders'

  id = db.Column(db.Integer, primary_key=True) 
  title = db.Column(db.String(40))
  description = db.Column(db.String(255))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
  billing_id = db.Column(db.Integer, db.ForeignKey('billings.id'), nullable=True)
  purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_orders.id'), nullable=True)
  amount = db.Column(db.Integer)
  weight = db.Column(db.String(40))
  itype = db.Column(db.String(40))
  price = db.Column(db.String(40))
  
  user = db.relationship('User', foreign_keys=[user_id])
  product = db.relationship('Product', foreign_keys=[product_id])
  billing = db.relationship('Billing', foreign_keys=[billing_id])
  purchase_order = db.relationship('PurchaseOrder', foreign_keys=[purchase_order_id])
  
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(
      db.DateTime, default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())

  def __init__(self, title=None, description=None, user_id=None, product_id=None, billing_id=None, purchase_order_id=None, amount=None, weight=None, itype=None, price=None):
    self.user_id = user_id
    self.title = title
    self.description = description
    self.product_id = product_id
    self.billing_id = billing_id
    self.purchase_order_id = purchase_order_id
    self.amount = amount
    self.weight = weight
    self.itype = itype
    self.price = price

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return Order.query.all()

  def delete():
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<Order with user_id: {} for product_id {}>".format(self.user_id, self.product_id)