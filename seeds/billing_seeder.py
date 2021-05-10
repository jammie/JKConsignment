from flask_seeder import Seeder, Faker, generator
from models.billing_model import Billing

class BillingSeeder(Seeder):
  
  def run(self):
    bill1 = {
      "user_id": 1,
      "billingref": str(generator.UUID()),
      "totalprice": "100"
    }
 
    result1 = Faker(
      cls=Billing,
      init=bill1
    ).create()
 
    print("Adding bill1: %s" % result1[0])
    self.db.session.add(result1[0])