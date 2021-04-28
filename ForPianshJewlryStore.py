import mysql.connector as mc

mydb = mc.connect(host="localhost", user="root", passwd="Qwaszx@123",database="piansh",auth_plugin='mysql_native_password')

m = mydb.cursor()

# CANNOT MAKE A TABLE IN PROGRAM BECAUSE DATABASE MIGHT BE FULL
print("Please create the table in mysql and place ingredients first 5 space character, then steps :)")

# FINDING DATA TABLE TO STORE IN
name = input("Enter the name of the table that you have created:")

# GETTING COLUMS TO HELP STORE DATA
m.execute(f"show columns from {name};")

# RETRIVING DATA AS A LIST
colums = m.fetchall()

print(colums)

# FILTERING LIST FOR JUST COLUM NAME
for i in range(len(colums)):
    vara = list(colums[i])

    colums[i] = vara[0]

# CREATING LIST TO STORE VALUES
values = []

# ADDING VALUES
for i in range(len(colums)):
    values.append(input(f"Please enter the value for {colums[i]} : "))

# CREATING STRING THAT WILL EXECUTE THE COMMAND (112-128)
executable_string = f"INSERT INTO {name}("

for i in range(len(colums)):
    if i == len(colums) - 1:
        executable_string += f"{colums[i]}"
    else:
        executable_string += f"{colums[i]},"

executable_string += ") VALUES ("

for i in range(len(values)):
    if i == len(values) - 1:
        executable_string += f"'{values[i]}'"
    else:
        executable_string += f"'{values[i]}',"

executable_string += ");"

# EXECUTING COMMAND AND COMMITING TO SAVE THE DATA ON THE TABLE, ASSURING
# THE USER THE PROCCESS WAS SUCCSESSFUL
m.execute(executable_string)
m.execute("COMMIT;")
print("YOUR RECIPIE HAS BEEN ADDED TO THE SERVER, CONGRATULATIONS!!!")

# CALLING THE FUNCTION TO GO OVER AGAIN
