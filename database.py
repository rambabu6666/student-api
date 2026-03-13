from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

dbUrl="postgresql://postgres:root@localhost:5432/rbk"
engine=create_engine(dbUrl)
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base =declarative_base()

