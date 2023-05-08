from flask_restful import Resource

from glados.api.room.serializers import RoomSerializer
from glados.repositories.room import get_rooms


class RoomsApi(Resource):
    def get(self):
        room_serializer = RoomSerializer(many=True)
        rooms = get_rooms()

        response = room_serializer.dump(rooms), 200

        return response
