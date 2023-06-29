from chalicelib.models.models import UnitMeasure
from chalicelib.helpers.AuroraConector import AuroraConector

connector = AuroraConector()
conexion = connector.create_engine()
sesion = connector.create_session(conexion)

select = sesion.query(UnitMeasure).all()

print(select)
