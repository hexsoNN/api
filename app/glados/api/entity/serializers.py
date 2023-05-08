from marshmallow import fields, validate

from glados import ma, constants
from glados.models import Entity


class EntitiesRequestSerializer(ma.Schema):
    type = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityType]))
    status = fields.String(required=False, validate=validate.OneOf([x.name for x in constants.EntityStatus]))
    room = fields.String(required=False)
    id = fields.String(required=False)


class EntitySerializer(ma.Schema):
    created_at = fields.DateTime("%Y-%m-%dT%H:%M")
    room = fields.Method("get_room_name")

    def get_room_name(self, obj):
        return obj.room.name if obj.room else None

    class Meta:
        model = Entity
        ordered = True
        fields = [
            "id",
            "name",
            "type",
            "status",
            "value",
            "created_at",
            "room",
            "room_id"
        ]


class EntityResponseSerializer(EntitySerializer):
    pass
