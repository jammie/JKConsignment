from dotenv import load_dotenv
load_dotenv()

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from models import account_model, address_model, billing_model, consignment_model, order_model, product_model, purchase_order_model, user_model

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()