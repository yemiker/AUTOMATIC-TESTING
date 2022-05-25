from mySQL.MysqlPython import DB_connect

class Select(DB_connect):
    co = DB_connect()
    print(co.connect("SELECT * FROM film"))
    print(co.connect("SELECT * FROM actor"))
    print(co.connect("SELECT COUNT(actor_id) FROM actor"))
    print(co.connect("SELECT COUNT(film_id) FROM film"))



