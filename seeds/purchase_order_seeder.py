from flask_seeder import Seeder, Faker, generator
from models.purchase_order_model import PurchaseOrder

class PurchaseOrderSeeder(Seeder):
  
  def run(self):
    po1 = {
      "user_id": 1,
      "order_status": "completed",
      "order_from": "website",
      "payment_type": "online-payment",
      "payment_status": "completed"
    }
 
    result1 = Faker(
      cls=PurchaseOrder,
      init=po1
    ).create()
 
    print("Adding po1: %s" % result1[0])
    self.db.session.add(result1[0])