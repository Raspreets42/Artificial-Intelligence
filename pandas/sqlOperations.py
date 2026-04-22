import pandas as pd
import os
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, Float, Date

from dotenv import load_dotenv
load_dotenv()

server = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("SQL_DB")
username = os.getenv("SQL_USER")
password = os.getenv("SQL_PASSWORD")
mongo_uri = os.getenv("MONGO_URI")
# Database connection configuration
encoded_password = urllib.parse.quote_plus(password)

# SQLAlchemy connection string for MSSQL
# mssql_connection_string = (
#     f"mssql+pyodbc://{username}:{encoded_password}@{server},{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
# )

# # SQLAlchemy connection string for MSSQL
# mssql_connection_string = (
#     f"postgresql://{username}:{encoded_password}@{server}:{port}/{database}"
# )
#
# # SQLAlchemy connection string for MSSQL
# mssql_connection_string = (
#     f"mysql+pymysql://{username}:{encoded_password}@{server}:{port}/{database}"
# )

# engine = create_engine(
#             mssql_connection_string,
#             pool_size=50,
#             max_overflow=100,
#             pool_timeout=60,
#             pool_recycle=3600,
#             pool_pre_ping=True
#         )

# df = pd.read_sql("select AlertType, CropTitle, HealthAdvisoryValues_EN, HealthAdvisoryValues_HI from AMCropHealthThreshold where AlertType='Pest&Disease' and Month=FORMAT(GETDATE(), 'MMM') and FarmerType = 1", engine)
# df = df.drop(['HealthAdvisoryValues_HI'], axis=1)

# -------------------------------------------------------------------------------------------------------------------------

