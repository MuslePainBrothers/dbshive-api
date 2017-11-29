from flaskr import db
from sqlalchemy import *


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(Text)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
