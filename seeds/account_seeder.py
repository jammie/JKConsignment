from flask_seeder import Seeder, Faker, generator
from models.account_model import Account

class AccountSeeder(Seeder):
  
  def run(self):
    account = {
      "token": generator.String('abc[5-9]{4}\c[xyz]'),
      "username": generator.String('[abcdefgklmn][0-9]{2}\c[XYZ]')
    }
    result1 = Faker(
      cls=Account,
      init=account
    ).create()
 
    print("Adding account: %s" % result1[0])
    self.db.session.add(result1[0])