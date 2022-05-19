from app import local
from utils.db import db

with local.app_context():
    db.create_all()

if __name__ == "__main__":
  local.run(debug=True)