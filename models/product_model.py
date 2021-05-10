from app import db

class Product(db.Model): 

  __tablename__ = 'products'

  id = db.Column(db.Integer, primary_key=True)  
  name = db.Column(db.String(40))
  description = db.Column(db.String(40))
  ptype = db.Column(db.String(40))
  base_price = db.Column(db.String(40))
  
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(
      db.DateTime, default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())

  def __init__(self, name=None, description=None, ptype=None, base_price=None):
    self.name = name
    self.description = description
    self.ptype = ptype
    self.base_price = base_price

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return Product.query.all()

  def delete():
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<Product: {}>".format(self.name)