# 盐
SECRET_KEY = "asdfghjkl"

# 数据库配置
HOST_NAME="127.0.0.1"
PORT="3306"
USERNAME="root"
PASSWORD="LZLlzl12345"
DATABASE="python_projects"
DB_URI  = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST_NAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI

