import app.core.models.database as db
from app.core.models.user import User


db.Base.metadata.create_all(bind=db.engine, checkfirst=True)

next(db.get_db()).commit()
