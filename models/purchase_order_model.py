from app import db
import string
import random
from models import user_model

class PurchaseOrder(db.Model): 

  __tablename__ = 'purchase_orders'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  order_ref = db.Column(db.String(40))
  order_status = db.Column(db.String(40))
  order_from = db.Column(db.String(40))
  payment_type = db.Column(db.String(40)) 
  payment_status = db.Column(db.String(40))
  
  user = db.relationship('User', foreign_keys=[user_id])
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(
      db.DateTime, default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())

  def __init__(self, user_id=None, order_status=None, order_from=None, payment_type=None, payment_status=None): 
    self.user_id = user_id
    chars=string.ascii_uppercase + string.digits
    self.order_ref = ''.join(random.choice(chars) for _ in range(12)) 
    self.order_status = order_status
    self.order_from = order_from
    self.payment_type = payment_type
    self.payment_status = payment_status

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return PurchaseOrder.query.all()

  def delete():
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<PurchaseOrder: {}>".format(self.order_ref)