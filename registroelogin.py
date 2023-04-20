import tkinter as tk
import sqlite3

class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        
        self.label_username = tk.Label(self.master, text="Username")
        self.label_username.pack()
        
        self.entry_username = tk.Entry(self.master)
        self.entry_username.pack()
        
        self.label_password = tk.Label(self.master, text="Password")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack()
        
        self.button_login = tk.Button(self.master, text="Login", command=self.login)
        self.button_login.pack(pady=10)
        
        self.button_register = tk.Button(self.master, text="Register", command=self.register)
        self.button_register.pack()
        
        self.label_message = tk.Label(self.master, text="")
        self.label_message.pack()
        
        self.create_table()
        
    def create_table(self):
        connection = sqlite3.connect("login.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        connection.commit()
        connection.close()
        
    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username == "" or password == "":
            self.label_message.config(text="Please enter a username and password")
            return
        
        connection = sqlite3.connect("login.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        connection.commit()
        connection.close()
        
        self.label_message.config(text="Registration successful")
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        connection = sqlite3.connect("login.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        connection.close()
        
        if user is not None:
            self.label_message.config(text="Login successful")
        else:
            self.label_message.config(text="Invalid username or password")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()
