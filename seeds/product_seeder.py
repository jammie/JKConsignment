from flask_seeder import Seeder, Faker, generator
from models.product_model import Product

class ProductSeeder(Seeder):
  
  def run(self):
    product1 = {
      "name": "Small Package",
      "description": "Small Package Bla Bla Bla Bla",
      "ptype": "small",
      "base_price": "50"
    }
    
    result1 = Faker(
      cls=Product,
      init=product1
    ).create()
 
    print("Adding product1: %s" % result1[0])
    self.db.session.add(result1[0])
    
    product2 = {
      "name": "Large Package",
      "description": "Large Package Bla Bla Bla Bla",
      "ptype": "large",
      "base_price": "50"
    }
 
    result2 = Faker(
      cls=Product,
      init=product2
    ).create()
 
    print("Adding product2: %s" % result2[0])
    self.db.session.add(result2[0])