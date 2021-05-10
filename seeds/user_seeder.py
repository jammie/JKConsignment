from flask_seeder import Seeder, Faker, generator
from models.user_model import User

class UserSeeder(Seeder):
  
  def run(self):
    sender1 = {  
        "utype": "sender",
        "name": generator.Name(),
        "phone_number": generator.String("+628[0-9]{10}")
    }
    result1 = Faker(
      cls=User,
      init=sender1
    ).create()
 
    print("Adding sender1: %s" % result1[0])
    self.db.session.add(result1[0])
    
    receiver1 = {  
        "utype": "receiver",
        "name": generator.Name(),
        "phone_number": generator.String("+628[0-9]{10}")
    }
    result2 = Faker(
      cls=User,
      init=receiver1
    ).create()
 
    print("Adding receiver1: %s" % result2[0])
    self.db.session.add(result2[0])
    
    courier1 = {  
        "utype": "courier",
        "name": generator.Name(),
        "phone_number": generator.String("+628[0-9]{10}")
    }
    result3 = Faker(
      cls=User,
      init=courier1
    ).create()
 
    print("Adding courier1: %s" % result3[0])
    self.db.session.add(result3[0])