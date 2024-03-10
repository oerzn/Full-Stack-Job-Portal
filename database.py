from sqlalchemy import create_engine, text

import pymysql
import os




# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     print(result.all())

pass_string= os.environ['DB_CONNCECTION_PASSWORD']

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="jobportalharsh-jobportal.a.aivencloud.com",
  password= "pass_string"
  # password= "AVNS_MVvh66EMlBD080PUK2k",
  read_timeout=timeout,
  port=12992,
  user="avnadmin",
  write_timeout=timeout,
)
cursor = connection.cursor()
# try:
#   cursor = connection.cursor()
#   cursor.execute("SELECT * FROM jobs")
#   all_result = cursor.fetchall()
# #   print(all_result)
# #   print(type(all_result))
#   first_1 = all_result[3]
#   print((first_1))

# finally:
#   connection.close()

def load_jobs_with_db():
  cursor.execute("SELECT * FROM jobs")
  jobs_list = cursor.fetchall()
  return jobs_list