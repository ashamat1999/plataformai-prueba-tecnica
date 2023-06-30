from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

"""
Class created to manage Aurora DDBB conections.
"""

class AuroraConector():

    def __init__(self) -> None:
        """
        Connector init function, it defines each values to create connection with
        Aurora DDBB.
        """
        ENDPOINT = "database-plataformai-instance-1.ch0e22cu1ymh.us-east-1.rds.amazonaws.com"
        PORT = 5432
        USER = 'postgres'

        self.url = URL.create(
            drivername="postgresql",
            username=USER,
            host=ENDPOINT,
            password='password',
            database='plataformai_test',
            port=PORT
        )
    
    def create_engine(self):
        engine = create_engine(self.url, echo=True)

        connection = engine.connect()
        
        return connection

    def create_session(self, engine):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        return session

