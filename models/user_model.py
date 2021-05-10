from app import db
from models import account_model

class User(db.Model):
  """This class represents the users table."""

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=True)
  name = db.Column(db.String(255))
  utype = db.Column(db.String(255))
  phone_number = db.Column(db.String(255))
  account = db.relationship('Account', foreign_keys=[account_id])
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(
      db.DateTime, default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())

  def __init__(self, name=None, utype=None, phone_number=None):
    self.name = name
    self.utype = utype
    self.phone_number = phone_number

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return User.query.all()

  def delete():
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<User: {}>".format(self.name)