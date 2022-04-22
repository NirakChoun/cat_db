import mysql.connector

'''
State your group member name and id here:
Song Rithykun 2022120
Socheata Thy 2021341
Choun Chan Nirak 2022201
'''


# TODO:
# host can be 'localhost' or '127.0.0.1'
# if you are using mamp, password is root
# and port is 8889
# use cat_db as database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cat_db",
    port="8889"
print (mydb)


cursor = mydb.cursor()


def register_cat(cat_info):
    sql = "INSERT INTO cats (name, gender, breed, dob, description) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, cat_info)

    mydb.commit()
    print("Register Completed!\n")



def get_cats():
    sql = "SELECT * FROM cats"
    cursor.execute(sql)
    myresult = cursor.fetchall()

    return(myresult)



def get_cat(id):
    sql = "SELECT * FROM cats"
    cursor.execute(sql)
    myresult = cursor.fetchone()

    return(myresult)


def update_cat(cat_info):

    id, name, gender, breed, dob, description = cat_info
    
    sql = f"UPDATE cats SET name = '{name}', gender = '{gender}', breed = '{breed}', dob = '{dob}', description = '{description}' WHERE id = '{id}'"

    cursor.execute(sql)

    mydb.commit()


def remove_cat(id):
    
    sql = "DELETE FROM cats WHERE id = {id}"

    cursor.execute(sql)

    mydb.commit()



