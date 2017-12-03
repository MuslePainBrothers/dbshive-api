from dbshive_api import db

from sqlalchemy import Column, Integer, Text, Table, ForeignKey
from sqlalchemy.orm import relation


item_user_table = Table(
    'items_users',
    db.Model.metadata,
    Column('item_id', Integer, ForeignKey('item.id')),
    Column('user_id', Integer, ForeignKey('user.id')),
)


class Item(db.Model):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    description = Column(Text)
    developer = relation(
        "User",
        order_by='User.id',
        secondary=item_user_table
    )

    def to_json(self):
        developers = [user.name for user in self.developer]
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'developers': developers
        }
