from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin 
from instance.config import app_config 
from flask import Flask, redirect, url_for, request, jsonify, abort
from flask_seeder import FlaskSeeder 
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json

db = SQLAlchemy()
 
def create_app(config_name):
  app = FlaskAPI(__name__, instance_relative_config=True)
  app.config.from_object(app_config['development'])
  app.config.from_pyfile('config.py')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  seeder = FlaskSeeder()
  seeder.init_app(app, db)
   
  
  cors_config = {
    "CORS_HEADERS": 'Content-Type',
    "origins": "*",
    "methods": ["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"],
    "allow_headers": "*"
  }
  cors = CORS(app, resource=cors_config, supports_credentials=True ) 
 
  flask_json = FlaskJSON(app)
  
  from models.consignment_model import Consignment 
  
  def get_consignment_obj(consignment):
    sender_address = {
        'name': consignment.pickup_address.name,
        'latitude': consignment.pickup_address.lat,
        'longitude': consignment.pickup_address.lng,
        'detail': consignment.pickup_address.detail
      }
    sender_contact = {
      'name': consignment.sender.name,
      'phone_number': consignment.sender.phone_number
    }
    sender_object = {
      'address': sender_address,
      'contact': sender_contact
    }
    receiver_address = {
      'name': consignment.delivery_address.name,
      'latitude': consignment.delivery_address.lat,
      'longitude': consignment.delivery_address.lng,
      'detail': consignment.delivery_address.detail
    }
    receiver_contact = {
      'name': consignment.receiver.name,
      'phone_number': consignment.receiver.phone_number
    }
    receiver_object = {
      'address': receiver_address,
      'contact': receiver_contact
    }
    courier_object = {
      'courier_name': consignment.courier.name,
      'courier_phone_number': consignment.courier.phone_number
    }
    billing_object = {
      'billingref': consignment.billing.billingref,
      'totalprice': consignment.billing.totalprice
    }
    purchase_order_object = {
      'order_ref': consignment.purchase_order.order_ref,
      'order_status': consignment.purchase_order.order_status,
      'order_from': consignment.purchase_order.order_from,
      'payment_status': consignment.purchase_order.payment_status,
      'payment_type': consignment.purchase_order.payment_type,
    }
    pickup_object = {
      'pickup_date': consignment.pickup_date,
      'pickup_time_from': consignment.pickup_time_from,
      'pickup_time_to': consignment.pickup_time_to,
      'pickup_address': sender_address
    }
    delivery_object = {
      'delivery_date': consignment.delivery_date,
      'delivery_time_from': consignment.delivery_time_from,
      'delivery_time_to': consignment.delivery_time_to,
      'delivery_address': receiver_address
    }
    obj = {
      'id': consignment.id,
      'name': consignment.name,
      'sender': sender_object,
      'receiver': receiver_object,
      'courier': courier_object,
      'pickup': pickup_object,
      'delivery': delivery_object,
      'service_type': consignment.service_type,
      'vehicle_type': consignment.vehicle_type,
      'billing': billing_object,
      'purchase_order': purchase_order_object,
      'date_created': consignment.date_created,
      'date_modified': consignment.date_modified
    }
    return obj
    
  @app.route('/consignments/', methods=["GET", "POST"]) 
  def consignments():  
    if request.method == "POST": 
      data = json.loads(request.get_json(force=True))  
      name = data['name']
      vehicle_type = data['vehicle_type']
      service_type = data['service_type']
      consignment = Consignment(name=name, 
                                vehicle_type=vehicle_type, 
                                service_type=service_type, 
                                sender_id=1,
                                receiver_id=2,
                                courier_id=3,
                                billing_id=1,
                                address_id=1,
                                purchase_order_id=1,
                                delivery={
                                  "delivery_date": "2021-1-20",
                                  "delivery_time_from": "08:45",
                                  "delivery_time_to": "10:45",
                                  "delivery_address_id": 2
                                },
                                pickup={
                                  "pickup_date": "2021-1-20",
                                  "pickup_time_from": "08:00",
                                  "pickup_time_to": "08:30",
                                  "pickup_address_id": 1
                                }
                                )
      consignment.save()
      response = jsonify(get_consignment_obj(consignment))
      response.status_code = 200 
      return response
    if request.method == 'GET':
      page = request.args.get('page')
      per_page = request.args.get('per_page')
      name_filter = request.args.get('filter_by_name')
      vehicle_filter = request.args.get('filter_by_vehicle')
      service_filter = request.args.get('filter_by_service')
      
      if not page or page == 0 or page is None:
        page = 1
      if not per_page or per_page == 0 or per_page is None:
        per_page = 1
      if not name_filter or name_filter == 0 or name_filter is None:
        name_filter = ""
      if not vehicle_filter or vehicle_filter == 0 or vehicle_filter is None:
        vehicle_filter = ""
      if not service_filter or service_filter == 0 or service_filter is None:
        service_filter = ""
        
      page = int(page)
      per_page = int(per_page)
      name_filter = str(name_filter)
      service_filter = str(service_filter)
      vehicle_filter = str(vehicle_filter)
      
      consignments = Consignment.get_as_paginated(page, per_page, name_filter, service_filter, vehicle_filter)
      results = []
      
      for consignment in consignments.items:
        obj = get_consignment_obj(consignment)
        results.append(obj)
      data = {
        'items': results,
        'page': consignments.page,
        'per_page': consignments.per_page,
        'next_page': consignments.next_num,
        'prev_page': consignments.prev_num,
        'total_pages': consignments.pages,
        'no_of_items': consignments.total
      }
      response = jsonify(data)
      response.status_code = 200 
      return response
      
  
  @app.route('/consignments/<int:id>', methods=['GET', 'PUT', 'DELETE']) 
  def consignment_manipulation(id, **kwargs):
    # retrieve bucketlist using it's id
    consignment = Consignment.query.filter_by(id=id).first()
    if not consignment:
      abort(404)
    
    if request.method == 'DELETE':
      consignment.delete()
      response = jsonify({
        "message": "consignment {} deleted successfully".format(consignment.id)
      })
      response.status_code = 200
      
      return response
    elif request.method == "PUT":
      data = json.loads(request.get_json(force=True))
      
      name = data['name']
      vehicle_type = data['vehicle_type']
      service_type = data['service_type']
      
      consignment.name = name
      consignment.vehicle_type = vehicle_type
      consignment.service_type = service_type
      
      consignment.save()
      response = jsonify({
        "message": "consignment {} updated successfully".format(consignment.id)
      })
      response.status_code = 200
      return response
    else:
      # GET
      response = jsonify(get_consignment_obj(consignment))
      response.status_code = 200 
      return response
  
  
  return app