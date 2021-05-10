from flask_seeder import Seeder, Faker, generator
from models.consignment_model import Consignment

class ConsignmentSeeder(Seeder):
  
  def run(self):
    pickup1 = {
      "pickup_date": "2021-1-20",
      "pickup_time_from": "08:00",
      "pickup_time_to": "08:30",
      "pickup_address_id": 1
    }
    delivery1 = {
      "delivery_date": "2021-1-20",
      "delivery_time_from": "08:45",
      "delivery_time_to": "10:45",
      "delivery_address_id": 2
    }
    cons1 = {
      "name": "sample1-consignments",
      "sender_id": 1,
      "receiver_id": 2,
      "courier_id": 3,
      "billing_id": 1,
      "address_id": 1,
      "purchase_order_id": 1,
      "delivery": delivery1,
      "pickup": pickup1,
      "vehicle_type": "car",
      "service_type": "express",
    }
 
    result1 = Faker(
      cls=Consignment,
      init=cons1
    ).create()
 
    print("Adding consignment1: %s" % result1[0])
    self.db.session.add(result1[0])