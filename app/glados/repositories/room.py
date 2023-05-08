from glados.models import Room


def get_rooms():
    return Room.query.all()
