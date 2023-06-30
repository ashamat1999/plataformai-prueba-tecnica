from chalice import Blueprint
from chalice import Chalice
from chalicelib.models.models import UnitMeasure
from chalicelib.helpers.AuroraConector import AuroraConector
from sqlalchemy import select, delete, update

"""
File to manage each measure routes.
Due to blueprint defined in app.py endpoints are:

/measures/*
"""
unitMeasuresBlue = Blueprint(__name__)

@unitMeasuresBlue.route('/unit_measures', methods=['GET'])
def get_unit_measures():
    """
    Function to define GET measures endpoint.

    params
    -
    body
    -

    returns
     - resp: select JSON formatted answered query.
    """
    connector = AuroraConector()
    conexion = connector.create_engine()
    sesion = connector.create_session(conexion)

    select_req = sesion.query(UnitMeasure).all()
    conexion.close()

    resp = [measure.as_dict() for measure in select_req]
    return resp


@unitMeasuresBlue.route('/unit_measures/{measure_id}', methods=['GET'])
def get_unit_measures_id(measure_id):
    """
    Function to define GET especific measure endpoint.

    params
    measure_id: measure_id to search for
    body
    -

    returns
     - resp: JSON formatted answered query.
    """
    connector = AuroraConector()
    conexion = connector.create_engine()

    select_query = select(UnitMeasure).where(UnitMeasure.unit_measure_id == measure_id)
    measure = conexion.execute(select_query)
    measure_res = measure.first()._asdict()

    conexion.close()

    return measure_res


@unitMeasuresBlue.route('/unit_measures', methods=['POST'])
def post_unit_measures():
    """
    Function to define POST measure endpoint.

    params
    - 
    body, JSON:
    {
        "unit_measure_id": int,
        "measure_name": String
    }

    returns
     - rsp: rsp dict object. 
    """
    unit_as_json = unitMeasuresBlue.current_request.json_body
    unit = UnitMeasure(**unit_as_json)

    connector = AuroraConector()
    conexion = connector.create_engine()
    session = connector.create_session(conexion)

    session.add(unit)
    session.commit()

    conexion.close()

    rsp = {
        'message':'Médida creada con éxito.',
        'status_code': 0
    }

    return rsp


@unitMeasuresBlue.route('/unit_measures/{measure_id}', methods=['DELETE'])
def delete_unit_measures(measure_id):
    """
    Function to define DELETE especific measure endpoint.

    params
    measure_id: measure_id to delete.

    body:
    - 

    returns
     - rsp: rsp dict object. 
    """
    connector = AuroraConector()
    conexion = connector.create_engine()

    delete_query = delete(UnitMeasure).where(UnitMeasure.unit_measure_id == measure_id).returning(UnitMeasure.measure_name)
    conexion.execute(delete_query)
    conexion.commit()
    
    conexion.close()

    rsp = {
        'message':f'Medida eliminada.',
        'status_code': 1
    }

    return rsp


@unitMeasuresBlue.route('/unit_measures/{measure_id}', methods=['PATCH'])
def patch_unit_measures(measure_id):
    """
    Function to define PATCH especific measure endpoint.

    params
    measure_id: measure_id to update.
    
    body, JSON:
    {
        "measure_name": String
    }

    returns
     - rsp: rsp dict object. 
    """
    connector = AuroraConector()
    conexion = connector.create_engine()

    try:
        unit_as_json = unitMeasuresBlue.current_request.json_body

        update_query = update(UnitMeasure).where(UnitMeasure.unit_measure_id == measure_id).values(unit_as_json)
        conexion.execute(update_query)
        conexion.commit()
    except KeyError:
        rsp = {
            'message':f'Error de llaves de json.',
            'status_code': 2
        }

        return rsp, 403
    except BaseException:
        rsp = {
            'message':f'Error interno.',
            'status_code': 3
        }

        return rsp,500
    
    conexion.close()

    rsp = {
        'message':f'Medida actualizada.',
        'status_code': 4
    }

    return rsp