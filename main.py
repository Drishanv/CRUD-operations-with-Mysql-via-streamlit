import mysql.connector
import streamlit as st

# establish a connection to MYSQL server

mydb = mysql.connector.connect(
    host= "sql12.freesqldatabase.com",
    port = 3306,
    user = "sql12795418",
    password = "splpAf4kYI",
    database = "sql12795418"
)

mycursor = mydb.cursor()

print("Connection established")

# Create streamlit app

def main():
    st.title("CRUD Application with MySQL")

# Display options for CRUD operations
    option = st.sidebar.selectbox("Select an operation", ("Create", "Read", "Update", "Delete"))

# Perform selected CRUD operations

    if option == "Create":
        st.subheader("Create a record") 
        name = st.text_input("Enter name")
        email = st.text_input("Enter email")
        if st.button("Create"):
            sql = "insert into users(name, email) values(%s, %s)"
            val = (name, email)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Create records successfully!!!!!")


    elif option == "Read":
        st.subheader("Read records")
        mycursor.execute("Select * from users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)


    elif option == "Update":
        st.subheader("Update a record")
        id = st.number_input("Enter id", min_value = 1)
        name = st.text_input("Enter name")
        email = st.text_input("Enter email")
        if st.button("Update"):
            sql = "Update users set name = %s , email = %s where id =%s"
            val = (name, email, id)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record updated successfully")



    elif option == "Delete":
        st.subheader("Delete a record")
        id = st.number_input("Enter id", min_value = 1)
        if st.button("Delete"):
            sql = "Delete from users where id = %s"
            val = (id, )
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record deleted successfully")


if __name__ == "__main__":
    main()
