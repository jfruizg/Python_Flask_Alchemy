from app import local, prod
from utils.db import db

with prod.app_context():
    db.create_all()

if __name__ == "__main__":
  prod.run(debug=True)



