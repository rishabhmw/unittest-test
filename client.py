import requests
import mysql.connector


class Client:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def trades_for_month(self, month):
        response = requests.get(f'http://trades.cs.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

    def get_val_from_db(self):
        mydb = mysql.connector.connect(
                  host="localhost",
                  user="username",
                  password="password"
                )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM customers")
        return mycursor.fetchall()

    def get_email(self):
        return f'{self.first.lower()}.{self.last.lower()}@credit-suisse.com'