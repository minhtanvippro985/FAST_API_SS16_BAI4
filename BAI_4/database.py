from sqlalchemy.orm import sessionmaker , declarative_base 
from sqlalchemy import create_engine



DATABASE_URL = "mysql+pymysql://root:12345@127.0.0.1/enroll_db"


engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(
    autoflush= False,
    autocommit = False,
    bind= engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()