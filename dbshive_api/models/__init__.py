from dbshive_api import db
from dbshive_api.models import item, user


def create_all():
    db.create_all()
