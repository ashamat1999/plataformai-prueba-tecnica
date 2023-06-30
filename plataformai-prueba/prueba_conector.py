from chalicelib.models.models import UnitMeasure, Products, Base
from chalicelib.helpers.AuroraConector import AuroraConector
from sqlalchemy import select



connector = AuroraConector()
conexion = connector.create_engine()

sesion = connector.create_session(conexion)

select_req = sesion.query(Products).all()
conexion.close()

resp = [measure.as_dict() for measure in select_req]

print(resp)
print(type(resp))
