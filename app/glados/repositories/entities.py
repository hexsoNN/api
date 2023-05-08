from glados import db
from glados.models import Entity, Room


def get_entities(filters):
    query = Entity.query

    type = filters.get("type", None)
    status = filters.get("status", None)
    room = filters.get("room", None)
    id = filters.get("id", None)

    if type is not None:
        query = query.filter(Entity.type == type)

    if status is not None:
        query = query.filter(Entity.status == status)

    if room is not None:
        query = query.join(Room).filter(Room.name == room)

    if id is not None:
        query = query.filter(Entity.id == id)

    return query


def add_entity(new_entity):
    db.session.add(new_entity)
    db.session.commit()


def delete_entity(id):
    entity = Entity.query.get(id)
    if entity is not None:
        db.session.delete(entity)
        db.session.commit()
        return True
    else:
        return False


def update_entity(data):
    entity = Entity.query.get(data['id'])

    entity.name = data['name']
    entity.status = data['status']
    entity.type = data['type']
    if 'value' in data.keys():
        entity.value = data['value']
    if 'room_id' in data.keys():
        entity.room_id = data['room_id']

    db.session.commit()
