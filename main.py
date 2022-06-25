import customtkinter
import sqlite3
import tkinter


connection = sqlite3.connect('users.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
        USERS(username text, password text)
"""

cursor.execute(command1)

cursor.execute("INSERT INTO USERS VALUES('user1', 'password1')")
cursor.execute("INSERT INTO USERS VALUES('user2', 'password2')")
cursor.execute("INSERT INTO USERS VALUES('user3', 'password3')")
cursor.execute("INSERT INTO USERS VALUES('user4', 'password4')")
cursor.execute("INSERT INTO USERS VALUES('user5', 'password5')")




customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Turtle Code Youtube Log In System")
app.geometry("960x540")

bottomframe = tkinter.Frame(app)
bottomframe.pack(expand = True)

def button_event():
    cursor.execute("SELECT * from USERS")
    results = cursor.fetchall()

    for result in results:
        if user_name.get() == result[0] and password.get() == result[1]:
            label.set_text("Correct")
            break
        else:
            label.set_text("Wrong")

user_name = customtkinter.CTkEntry(master=bottomframe,
                               placeholder_text="Username",
                               text_font=('Helvetica',28),
                               width=800,
                               height=100,
                               border_width=2,
                               corner_radius=10)
user_name.pack()

password = customtkinter.CTkEntry(master=bottomframe,
                               placeholder_text="Password",
                               text_font=('Helvetica', 28),
                               width=800,
                               height=100,
                               border_width=2,
                               corner_radius=10)
password.pack()

button = customtkinter.CTkButton(master=bottomframe,
                                 width=500,
                                 height=100,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Log In",
                                 text_font=('Helvetica', 28),
                                 command=button_event)
button.pack()


label = customtkinter.CTkLabel(master=bottomframe,
                               text="",
                               text_color="black",
                               width=200,
                               height=100,
                               text_font=('Helvetica', 28),
                               fg_color=("white"),
                               corner_radius=8
                               )
label.pack()


app.mainloop()