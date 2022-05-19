from app import local, prod
from utils.db import db

with prod.app_context():
    db.create_all()

with local.app_context():
    db.create_all()

if __name__ == "__main__":
  variable = input()
  if variable == "local":
      local.run(debug=True)
  else:
      prod.run(debug=True)



