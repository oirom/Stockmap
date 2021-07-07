from models.database import init_db
from models.database import db_session
from models.models import WorkorderContent

init_db()

for i in range(60):
  db_session.add(WorkorderContent(i+1, 143001 + i))

db_session.commit()
