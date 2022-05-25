#יש להגדיר קלאס של התחברות לבסיס נתונים בתוך הקלאס יהיה מתודה של התחברות והמתודה מחזירה את cursor
#יש לשלוף את כל השחקנים מטבלת שחקנים
# יש לשלוף את כל הסרטים
#ולהדפיס כל אחת מתוצאות
#יש למנות את כמות הסרטים וכמות השחקנים ולהציג כל אחד
#עכדני אחת מרשומות וקובוץ 3 גוין


import mysql.connector

class DB_connect():
    def __init__(self):
        self.con = mysql.connector.connect(
        host='localhost',
        user='root',
        password="Ahruah123",
        database="sakila"
    )


    def connect(self, sql):
        connect = self.con.cursor()
        connect.execute(sql)
        return connect.fetchall()

    def Update(self,Type):
        connect = self.con.cursor()
        connect.execute(Type)
        return self.con.commit()








