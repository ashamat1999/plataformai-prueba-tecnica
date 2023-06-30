from chalice import Blueprint
from chalicelib.models.models import Products
from chalicelib.helpers.AuroraConector import AuroraConector
from sqlalchemy import select, delete, update

productsBlue = Blueprint(__name__)

@productsBlue.route('/products', methods=['GET'])
def get_products():
    """
    Function to define GET products endpoint.

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

    select_req = sesion.query(Products).all()
    conexion.close()

    resp = [product.as_dict() for product in select_req]
    return resp


@productsBlue.route('/products/{product}', methods=['GET'])
def get_product(product):
    """
    Function to define GET especific product endpoint.

    params
    product: product_name to search for
    body
    -

    returns
     - resp: JSON formatted answered query.
    """
    connector = AuroraConector()
    conexion = connector.create_engine()

    select_query = select(Products).where(Products.product_name == product)
    product = conexion.execute(select_query)
    product_res = product.first()._asdict()

    conexion.close()

    return product_res


@productsBlue.route('/products', methods=['POST'])
def post_product():
    """
    Function to define POST product endpoint.

    params
    - 
    body, JSON:
    {
        "product_name":String,
        "price":Numeric,
        "unit_measure_id": FOREIGN KEY(int)
    }

    returns
     - rsp: rsp dict object. 
    """

    product_json = productsBlue.current_request.json_body
    product = Products(**product_json)

    connector = AuroraConector()
    conexion = connector.create_engine()
    session = connector.create_session(conexion)

    session.add(product)
    session.commit()

    conexion.close()

    rsp = {
        'message':'Producto creado con éxito.',
        'status_code': 10
    }

    return rsp


@productsBlue.route('/products/{product}', methods=['DELETE'])
def delete_product(product):
    """
    Function to define DELETE especific product endpoint.

    params
    product: product to delete.

    body:
    - 

    returns
     - rsp: rsp dict object. 
    """
    connector = AuroraConector()
    conexion = connector.create_engine()

    delete_query = delete(Products).where(Products.product_name == product)
    conexion.execute(delete_query)
    conexion.commit()
    
    conexion.close()

    rsp = {
        'message':f'Producto eliminado.',
        'status_code': 11
    }

    return rsp


@productsBlue.route('/products/{product}', methods=['PATCH'])
def patch_product(product):
    """
    Function to define PATCH product endpoint.

    params
    product: product to update.
    
    body, JSON:
    {
        "price": OPTIONAL Numeric,
        "unit_measure_id": OPTIONAL int
    }

    returns
     - rsp: rsp dict object. 
    """
    connector = AuroraConector()
    conexion = connector.create_engine()

    try:
        product_as_json = productsBlue.current_request.json_body

        update_query = update(Products).where(Products.product_name == product).values(product_as_json)
        conexion.execute(update_query)
        conexion.commit()
    except KeyError:
        rsp = {
            'message':f'Error de llaves de json.',
            'status_code': 12
        }

        return rsp, 403
    except BaseException:
        rsp = {
            'message':f'Error interno.',
            'status_code': 13
        }

        return rsp,500
    
    conexion.close()

    rsp = {
        'message':f'Producto actualizado.',
        'status_code': 14
    }

    return rsp