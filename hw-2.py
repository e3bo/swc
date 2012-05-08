import sqlite3

connection = sqlite3.connect("experiments.db")
cursor = connection.cursor()
cursor.execute("""
SELECT Project.ProjectName,COUNT(DISTINCT Involved.Login) 
  from Project join Involved 
  where (Project.ProjectId = Involved.ProjectId) 
  group by Project.ProjectId;
""")
results = cursor.fetchall();
for r in results:
     print r[0], r[1]
cursor.close();
connection.close();
