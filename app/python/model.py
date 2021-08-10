from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE

# テーブル定義(DBのモデル)
class TestUserTable(Base):
    __tablename__ = 'test_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(128), nullable=False)

# モデル定義(apiのモデル) 
class TestUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


def main():
    # テーブル構築
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
