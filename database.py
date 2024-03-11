from sqlalchemy import create_engine, text

import pymysql
import os




# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     print(result.all())


timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="jobportalharsh-jobportal.a.aivencloud.com",
  password= "AVNS_MVvh66EMlBD080PUK2k",
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

def load_job_with_db(id):
  val = int(id)
  cursor.execute("SELECT * FROM jobs WHERE id = id"),
  
  list1 = cursor.fetchall()
  if len(list1) == 0:
    return None
  if val >4:
    return None
  else:
    return list1[val-1]
  


def add_application_to_db(job_id, data):
    
    query = text("INSERT INTO applications(job_id, full_name, email, linkedin_url, skill_set, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :skill_set, education, :work_experience, :resume_url )")


    cursor.execute(query,
                   job_id=job_id,
                   full_name=data['Full Name'],
                   email=data['Email'],
                   linkedin_url=data['LinkedIn'],
                   skill_Set=data['Skill Set'],
                   education=data['Education'],
                   work_experience=data['Experience'],
                   resume_url=data['Resume'])
