from chalice import Chalice
from chalicelib.models.models import UnitMeasure
from chalicelib.helpers.AuroraConector import AuroraConector


app = Chalice(app_name='plataformai-prueba')

@app.route('/unit_measures', methods=['GET'])
def get_unit_measures():
    connector = AuroraConector()
    conexion = connector.create_engine()
    sesion = connector.create_session(conexion)

    select = sesion.query(UnitMeasure).all()
    return select


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
