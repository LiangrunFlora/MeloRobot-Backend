HOST_NAME = "rm-cn-36z3o5awf000cd8o.rwlb.rds.aliyuncs.com"
PORT = "3306"
DATABASE = "network"
USERNAME = "root"
PASSWORD = "Jjhbpd_2022"
DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST_NAME}:{PORT}/{DATABASE}?charset=utf8mb4"

SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False
