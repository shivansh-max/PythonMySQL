"""This program is for all the chefs that don't know how to remember
   a recipe, This program is able to store an entire recipe and it
   can  print the recipe in the amount of batches the chef would
   like to make."""



# MAKING SURE THE FILE IS WORKING
# print("HELLO WORLD.")



# IMPORTS
import mysql.connector as mc
import sys



# CONNECTING TO THE SERVER THAT HAS AND STORES THE RECIPES.
mydb = mc.connect(host="localhost", user="root", passwd="Qwaszx@123", database="recipe",
                  auth_plugin='mysql_native_password')



# MAKING SURE WE ARE ABLE TO RUN CODE IN THE SERVER
m = mydb.cursor()



# MAIN FUNCTION THAT HANDLES THE PROGRAM.
def main():
    # GETTING THE INPUT FOR WHAT THE USER WANTS TO DO
    option = input("Type accordingly : \n    Q - Quit \n    O - Open recipe \n    A - Add recipe \n")

    # OPENING A RECIPE
    if option == "O":

        # GETTING ITEM NAME TO ACCESS DATA ON THAT ITEM
        item = input("Enter the name of the item : ")
        quantity = int(input("Enter amount of batches you would like : "))
        m.execute(f"select * from {item}")

        # RETRIVING THE DATA
        ingredients = m.fetchall()

        # LISTS THAT WILL SEPARATE AND STORE THE DATA
        ingredent_list = []
        step_list = []

        # CREATING A TEMPORARY LIST TO STORE DATA
        temp = list(ingredients[0])

        # CREATING A VARIABLE THAT STORES THE INDEX OF AN ITEM WITHIN THE LIST
        indi = 0

        # FINDING THE SORTER THAT SEPARATES INGREDIENTS FROM STEPS
        for j in range(len(temp)):
            if temp[j] == "     ":
                indi = j

        # USING SEPARATOR TO SEPARATE INGREDIENTS
        for i in range(len(temp)):
            if i < indi:
                ingredent_list.append(temp[i])
            elif i > indi:
                step_list.append(temp[i])

        # USING SEPARATOR TO SEPARATE STEPS
        for i in range(len(ingredent_list)):
            tempstring = list(ingredent_list[i])
            tempstring[0] = int(tempstring[0]) * quantity

            string = ""
            for j in range(len(tempstring)):
                if j == 0:
                    string += str(tempstring[j])
                else:
                    string += tempstring[j]

            ingredent_list[i] = string

        # GIVING OUTPUT FOR THE USER
        print(f"INGREDIENTS : {ingredent_list}")
        print(f"STEPS : {step_list}")

        # CALLING THE FUNCTION TO GO OVER AGAIN
        main()

    # ADDING DATA
    if option == "A":
        # CANNOT MAKE A TABLE IN PROGRAM BECAUSE DATABASE MIGHT BE FULL
        print("Please create the table in mysql and place ingredients first 5 space character, then steps :)")

        # FINDING DATA TABLE TO STORE IN
        name = input("Enter the name of the table that you have created:")

        # GETTING COLUMS TO HELP STORE DATA
        m.execute(f"show columns from {name};")

        # RETRIVING DATA AS A LIST
        colums = m.fetchall()

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
        main()

    # EXITING THE PROGRAM
    else:
        sys.exit()

# STARTING THE LOOP
main()
