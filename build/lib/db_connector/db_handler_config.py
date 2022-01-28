from schematics.models import Model
from schematics.types import StringType


class DbAccess(Model):
    host = StringType(required=True)
    user = StringType(required=True)
    password = StringType(required=True)
    table = StringType(required=True)