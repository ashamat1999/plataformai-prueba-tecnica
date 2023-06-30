from chalice import Blueprint
from chalicelib.models.models import Sales, Products
from chalicelib.helpers.AuroraConector import AuroraConector
from sqlalchemy import select, delete, update
from sqlalchemy.sql import func

salesBlue = Blueprint(__name__)


@salesBlue.route('/sales', methods=['POST'])
def post_sale():
    """
    Function to define POST sales endpoint.

    params
    - 
    body, JSON:
    {
        "product_name": String,
        "quantity": int,
        "sale_date":"YYYY-MM-DD" Date
        
    }

    returns
     - rsp: rsp dict object. 
    """
    sale_json = salesBlue.current_request.json_body
    sale = Sales(**sale_json)

    connector = AuroraConector()
    conexion = connector.create_engine()
    session = connector.create_session(conexion)

    session.add(sale)
    session.commit()

    conexion.close()

    rsp = {
        'message':'Venta creada con éxito.',
        'status_code': 20
    }

    return rsp

@salesBlue.route('/sales/{product}', methods=['GET'])
def get_sales_product(product):
    """
    Function to define GET especific product sales (amount and quantity).

    params
    product: product_name to search for
    body
    -

    returns
     - resp: JSON formatted answered query.
    """
    connector = AuroraConector()
    conexion = connector.create_engine()

    sesion = connector.create_session(conexion)

    select_req = sesion.query(Products.product_name,
                        func.sum(Sales.quantity * Products.price).label('total_ventas'),
                        func.sum(Sales.quantity).label('total_productos')) \
                        .join(Sales, Sales.product_name == Products.product_name) \
                        .filter(Products.product_name == product) \
                        .group_by(Products.product_name)

    select_req = select_req.all()
    conexion.close()


    rsp = [measure._asdict() for measure in select_req]

    return rsp

@salesBlue.route('/sales', methods=['GET'])
def get_sales():
    """
    Function to define GET products sales (amount and quantity).

    params
    - 
    body
    -

    returns
     - resp: JSON formatted answered query.
    """
    connector = AuroraConector()
    conexion = connector.create_engine()

    sesion = connector.create_session(conexion)

    select_req = sesion.query(Products.product_name,
                        func.sum(Sales.quantity * Products.price).label('total_ventas'),
                        func.sum(Sales.quantity).label('total_productos')) \
                        .join(Sales, Sales.product_name == Products.product_name) \
                        .group_by(Products.product_name)

    select_req = select_req.all()
    conexion.close()


    rsp = [measure._asdict() for measure in select_req]

    return rsp
