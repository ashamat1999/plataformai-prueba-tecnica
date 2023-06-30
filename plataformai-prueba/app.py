from chalice import Chalice
from chalicelib.models.models import UnitMeasure
from chalicelib.helpers.AuroraConector import AuroraConector
from sqlalchemy import select, delete, update
from chalicelib.routes.measures_routes import unitMeasuresBlue
from chalicelib.routes.products_routes import productsBlue

app = Chalice(app_name='plataformai-prueba')
app.register_blueprint(unitMeasuresBlue, url_prefix='/measures')
app.register_blueprint(productsBlue)



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
