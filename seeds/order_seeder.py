from flask_seeder import Seeder, Faker, generator
from models.order_model import Order

class OrderSeeder(Seeder):
  
  def run(self):
    order1 = {
      "user_id": 1,
      "amount": 2,
      "itype": "small",
      "weight": "100",
      "price": "100",
      "product_id": 1,
      "billing_id": 1,
      "purchase_order_id": 1,
      "title": "Small Package",
      "description": "a small package 2x"
    }
    result1 = Faker(
      cls=Order,
      init=order1
    ).create()
 
    print("Adding order1: %s" % result1[0])
    self.db.session.add(result1[0])