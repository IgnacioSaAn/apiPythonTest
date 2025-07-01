from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://test_7o5s_user:GhvUIdDlPrcFDO8T4aYFu24lur5dxWtb@dpg-d1hupd3uibrs73805i5g-a.oregon-postgres.render.com/test_7o5s"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
