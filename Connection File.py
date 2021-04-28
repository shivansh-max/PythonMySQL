import mysql.connector as mc

mydb = mc.connect(host="localhost", user="root", passwd="Qwaszx@123",database="names",auth_plugin='mysql_native_password')

# print(mydb)

m = mydb.cursor()

# name = input("ENTER THE PERSON YOU WANT INFORMATION ABOUT >>>>>")

anousha = f"SELECT * FROM anousha"
shivansh = f"SELECT * FROM shivansh"
prakash = f"SELECT * FROM prakash"
isha = f"SELECT * FROM isha"

m.execute(anousha)
print("ANOUSHA : ")
rez = m.fetchall()
for i in rez:
    print(i)

print()

m.execute(shivansh)
print("SHIVANSH : ")
rez = m.fetchall()
for i in rez:
    print(i)

print()

m.execute(prakash)
print("PRAKASH : ")
rez = m.fetchall()
for i in rez:
    print(i)

print()

m.execute(isha)
print("ISHA : ")
rez = m.fetchall()
for i in rez:
    print(i)


mydb.close()