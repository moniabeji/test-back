from src.entities.address import Address
from src.entities.delivery import Delivery
from src.entities.mission import Mission
from datetime import date

from src.entities.moto import Moto


def fetch_missions(session):
    '''
    fetch missions from table moto
    :param session: object sqlachemy
    :return: object non serialiseable
    '''
    return session.query(Mission).all()


def get_missions_today(session):
    today = date.today()
    num_missions = session.query(Mission).filter(Mission.creationDate == today).count()
    return num_missions

def get_missions_after(session):
    today = date.today()
    num_missions = session.query(Mission).filter(Mission.creationDate > today).count()
    return num_missions

def create_mission(session, mission):
    mission = Mission(mission["creationDate"],mission["delivery"]["id"],mission["moto"]["id"], mission["address"]["id"])
    session.add(mission)
    session.commit()
