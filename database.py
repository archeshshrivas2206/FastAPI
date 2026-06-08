from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url= "postgresql://postgres:Archesh%402206@localhost:5432/FirstDB"
engine= create_engine(db_url)

sessionlocal = sessionmaker(autocommit=False, autoflush= False, bind= engine)

