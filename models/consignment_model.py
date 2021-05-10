from app import db
import string
import random
from sqlalchemy import or_

from models import address_model, billing_model, user_model, purchase_order_model

class Consignment(db.Model): 

  __tablename__ = 'consignments'

  id = db.Column(db.Integer, primary_key=True)
  sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  courier_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  billing_id = db.Column(db.Integer, db.ForeignKey('billings.id'), nullable=True)
  purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_orders.id'), nullable=True)
  vehicle_type = db.Column(db.String(40))
  service_type = db.Column(db.String(40))
  pickup_date = db.Column(db.String(255))
  pickup_time_from = db.Column(db.String(255))
  pickup_time_to = db.Column(db.String(255))
  pickup_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=True)
  delivery_date = db.Column(db.String(255))
  delivery_time_from = db.Column(db.String(255))
  delivery_time_to = db.Column(db.String(255))
  delivery_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=True)
  name = db.Column(db.String(255))
  cref = db.Column(db.String(255))
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  date_modified = db.Column(
      db.DateTime, default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())
   
  pickup_address = db.relationship('Address', foreign_keys=[pickup_address_id])
  delivery_address = db.relationship('Address', foreign_keys=[delivery_address_id])
  sender = db.relationship('User', foreign_keys=[sender_id])
  receiver = db.relationship('User', foreign_keys=[receiver_id])
  courier = db.relationship('User', foreign_keys=[courier_id])
  billing = db.relationship('Billing', foreign_keys=[billing_id])
  purchase_order = db.relationship('PurchaseOrder', foreign_keys=[purchase_order_id])


  def __init__(self, 
               sender_id=None, 
               receiver_id=None, 
               courier_id=None, 
               billing_id=None, 
               purchase_order_id=None,
               vehicle_type=None, 
               service_type=None,
               address_id=None, 
               pickup=None,
               delivery=None,
               name=None
               ): 
    self.sender_id = sender_id
    self.receiver_id = receiver_id
    self.courier_id = courier_id
    self.billing_id = billing_id
    self.purchase_order_id = purchase_order_id
    self.vehicle_type = vehicle_type
    self.service_type = service_type
    self.pickup_address_id = pickup['pickup_address_id']
    self.pickup_date = pickup['pickup_date']
    self.pickup_time_from = pickup['pickup_time_from']
    self.pickup_time_to = pickup['pickup_time_to']
    self.delivery_address_id = delivery['delivery_address_id']
    self.delivery_date = delivery['delivery_date']
    self.delivery_time_from = delivery['delivery_time_from']
    self.delivery_time_to = delivery['delivery_time_to']
    self.name = name
    chars=string.ascii_uppercase + string.digits
    self.cref = ''.join(random.choice(chars) for _ in range(8))

  def save(self): 
      db.session.add(self)
      db.session.commit() 

  @staticmethod 
  
  def get_all():
    return Consignment.query.all()
  
  def get_as_paginated(page, per_page, filter_by_name, filter_by_service, filter_by_vehicle):
    filter_args = []
    if filter_by_name:
      name = '%%'
      if '*' in filter_by_name or '_' in filter_by_name: 
          name = filter_by_name.replace('_', '__')\
                          .replace('*', '%')\
                          .replace('?', '_')
      else:
          name = '%{0}%'.format(filter_by_name)
          
      filter_args.append(Consignment.name.ilike(name))
    if filter_by_service:
      service = '%%'
      if '*' in filter_by_service or '_' in filter_by_service: 
          service = filter_by_service.replace('_', '__')\
                          .replace('*', '%')\
                          .replace('?', '_')
      else:
          service = '%{0}%'.format(filter_by_service)
          
      filter_args.append(Consignment.service_type.ilike(service))
    if filter_by_vehicle:
      vehicle = '%%'
      if '*' in filter_by_vehicle or '_' in filter_by_vehicle: 
          vehicle = filter_by_vehicle.replace('_', '__')\
                          .replace('*', '%')\
                          .replace('?', '_')
      else:
          vehicle = '%{0}%'.format(filter_by_vehicle)
          
      filter_args.append(Consignment.vehicle_type.ilike(vehicle))
     
    if not filter_args:
      return Consignment.query.order_by(Consignment.date_modified.asc()).paginate(page, per_page, error_out=False)
    else:
      return Consignment.query.filter(or_(*filter_args)).order_by(Consignment.date_modified.asc()).paginate(page, per_page, error_out=False)

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return "<Consignment: {}>".format(self.cref)