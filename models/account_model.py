from app import db

class Account(db.Model): 

  __tablename__ = 'accounts'

  id = db.Column(db.Integer, primary_key=True)
  token = db.Column(db.String(255))
  username = db.Column(db.String(255))
  
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(
      db.DateTime, default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())

  def __init__(self, token=None, username=None):
    self.token = token
    self.username = username

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return Account.query.all()

  def delete():
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<Account: {} - {}>".format(self.username, self.token)