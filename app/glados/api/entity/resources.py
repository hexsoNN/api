from flask import request
from flask_restful import Resource
from glados.models import Entity

from glados.api.entity.serializers import EntitySerializer, EntitiesRequestSerializer, EntityResponseSerializer
from glados.repositories.entities import get_entities, add_entity, delete_entity, update_entity


class EntitiesAPI(Resource):
    def get(self):
        request_serializer = EntitiesRequestSerializer()
        data = request_serializer.load(request.args)

        entities = get_entities(data)

        serializer = EntityResponseSerializer(many=True)
        return serializer.dump(entities), 200

    def post(self):
        serializer = EntitySerializer()

        if request.json['room'] is None:
            request.json.pop('room')

        data = serializer.load(request.json)

        update_entity(data)

        return {"message": "Modified entity successfully."}, 200


class NewEntityApi(Resource):
    def post(self):
        serializer = EntitySerializer()

        new_entity = serializer.load(request.json)

        new_entity = Entity(**new_entity)
        add_entity(new_entity)

        return {"message": "New entity added successfully."}, 201


class DeleteEntityApi(Resource):
    def get(self):
        request_serializer = EntitiesRequestSerializer()
        data = request_serializer.load(request.args)

        delete_bool = delete_entity(data)
        if delete_bool is True:
            return {"message": "Deleted entity successfully."}, 200
        elif delete_bool is False:
            return {'error': 'Entity not found.'}, 404
