import mysql.connector as mc

mydb = mc.connect(host="localhost", user="root", passwd="Qwaszx@123", database="names",
                  auth_plugin='mysql_native_password')

m = mydb.cursor()

b="show databases"
# m.execute(b+";")
# rez = m.fetchall()
# for i in rez:
#     print(i)


# m.execute("CREATE TABLE carrots (name VARCHAR(30), age int not null,species varchar(80))")

# printstuff("show tables")

sqlFormula = "INSERT INTO scores (name,age,species) VALUES (%s,%s,%s);"
pet=('carrots,upadhyay',1,'rabbit')

m.execute(sqlFormula,pet)

mydb.commit()