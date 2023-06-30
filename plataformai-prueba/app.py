from chalice import Chalice
from chalicelib.routes.measures_routes import unitMeasuresBlue
from chalicelib.routes.products_routes import productsBlue
from chalicelib.routes.sales_routes import salesBlue

"""
Main chalice python file.
It contains each Blueprint register.
"""

app = Chalice(app_name='plataformai-prueba')
app.register_blueprint(unitMeasuresBlue, url_prefix='/measures')
app.register_blueprint(productsBlue)
app.register_blueprint(salesBlue)
