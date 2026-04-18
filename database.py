from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Kita menggunakan SQLite karena ringan dan tidak perlu install server database terpisah
SQLALCHEMY_DATABASE_URL = "sqlite:///./vetconnect.db"

# connect_args={"check_same_thread": False} dibutuhkan khusus untuk SQLite di FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency untuk membuka dan menutup koneksi database setiap kali ada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()