from app import db
import string
import random
from models import user_model


class Billing(db.Model): 

  __tablename__ = 'billings'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  billingref = db.Column(db.String(255))
  totalprice = db.Column(db.String(255)) 
  
  user = db.relationship('User', foreign_keys=[user_id])
  
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(
      db.DateTime, default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())

  def __init__(self, user_id=None, totalprice=None, billingref=None): 
    self.user_id = user_id
    self.totalprice = totalprice
    chars=string.ascii_uppercase + string.digits
    self.billingref = ''.join(random.choice(chars) for _ in range(12)) 

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return Billing.query.all()

  def delete():
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<Billing: {}>".format(self.billingref)