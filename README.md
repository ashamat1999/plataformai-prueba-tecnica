# plataformai-prueba-tecnica

# Description
Project created to probe tecnical knowgledge in python.

This project uses python aws chalice framework, creating a serverless API to
CRUD Products, UnitMeasures and Sales.

It mainly have 3 router pages, each one defined by a chalice Blueprint:
/measures:
- GET /measures/unit_measures/{measure_id}
- GET /measures/unit_measures
- POST /measures/unit_measures
- DELETE /measures/unit_measures/{measure_id}
- PATCH /measures/unit_measures/{measure_id}
/products:
- GET /products/{product_name}
- GET /products
- POST /products
- DELETE /products/{product_name}
- PATCH /products/{product_name}
/sales:
- POST /sales
- POST /sales/{product_name}
- POST /sales

# Run project
To run this project, user needs to have aws credentials loaded in machine.
Once user has credentials loaded, run:
- chalice deploy

This will start to deploy project in aws defined account.

# About endpoints
To read more about endpoints, read each docstring endpoint.

## Authors
José Ashamat Jaimes Saavedra.