from decouple import config

DATABASE_URL = config("DATABASE_URL", default="sqlite+pysqlite:///app/db/data.db")
