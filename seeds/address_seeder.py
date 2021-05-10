from flask_seeder import Seeder, Faker, generator
from models.address_model import Address

class AddressSeeder(Seeder):
  
  def run(self):
    address1 = {
      "user_id": 1,
      "name": "Sunway Lagoon",
      "detail": "3, Jalan PJS 11/11, Bandar Sunway, 47500 Subang Jaya, Selangor, Malaysia",
      "notes": "pickup near the security post",
      "lat": "3.0697",
      "lng": "101.60687"
    }
    result1 = Faker(
      cls=Address,
      init=address1
    ).create()
 
    print("Adding address: %s" % result1[0])
    self.db.session.add(result1[0])
    
    address2 = {
      "user_id": 1,
      "name": "Temple",
      "detail": "Temple, Alma, Bukit Mertajam, Central Seberang Perai District, Seberang Perai, Penang, 14000, Malaysia",
      "notes": "deliver to the security post",
      "lat": "5.329132899999999",
      "lng": "100.48077345323833"
    }
    result2 = Faker(
      cls=Address,
      init=address2
    ).create()
 
    print("Adding address: %s" % result2[0])
    self.db.session.add(result2[0])