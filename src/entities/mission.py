from sqlalchemy.orm import relationship
from src.entities.moto import MotoSchema
from src.entities.delivery import DeliverySchema
from src.entities.address import AddressSchema

from ..repositories.connexion import Base
from .entity import Entity

from sqlalchemy import Column, DateTime, Integer, ForeignKey
from marshmallow import Schema, fields

class Mission(Entity, Base):
    __tablename__ = 'missions'
    creationDate = Column('creation_date', DateTime, nullable=False)
    address_id = Column(Integer, ForeignKey('address.id'), nullable=False)
    delivery_id = Column(Integer, ForeignKey('delivery.id'), nullable=False)
    moto_id = Column(Integer, ForeignKey('moto.id'), nullable=False)
    address = relationship("Address", back_populates="mission")
    delivery = relationship("Delivery", back_populates="mission")
    moto = relationship("Moto", back_populates="mission")

    def __init__(self,  creationDate, address, delivery, moto):
        self.creationDate = creationDate
        self.address = address
        self.delivery = delivery
        self.moto = moto
print("yes")
class MissionSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    creationDate = fields.DateTime('%Y-%m-%d')
    address = fields.Nested(AddressSchema)
    delivery = fields.Nested(DeliverySchema)
    moto = fields.Nested(MotoSchema)
