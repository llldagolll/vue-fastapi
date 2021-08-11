from sqlalchemy import create_engine
from models.tasks import Base


host = "db:3306"
db_name = "vue-fastapi-db"
user = "fastapi"
password = "secret"

DATABASE = 'mariadb://%s:%s@%s/%s?charset=utf8' % (
    user,
    password,
    host,
    db_name,
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

def reset_database():
    Base.metadata.drop_all(bind=ENGINE)
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    reset_database()