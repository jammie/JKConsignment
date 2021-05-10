from app import db
from models import user_model

class Address(db.Model): 

  __tablename__ = 'addresses'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  name = db.Column(db.String(255))
  detail = db.Column(db.String(255))
  notes = db.Column(db.String(255))
  lat = db.Column(db.String(255))
  lng = db.Column(db.String(255))

  user = db.relationship('User', foreign_keys=[user_id])

  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(
      db.DateTime, default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())

  def __init__(self, user_id=None, name=None, detail=None, notes=None, lat=None, lng=None): 
    self.name = name
    self.detail = detail
    self.notes = notes
    self.user_id = user_id
    self.lat = lat   
    self.lng = lng

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return Address.query.all()

  def delete():
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<Address: {}>".format(self.name)