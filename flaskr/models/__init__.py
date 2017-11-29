from flaskr import db
from flaskr.models import item, user


def create_all():
    db.create_all()
