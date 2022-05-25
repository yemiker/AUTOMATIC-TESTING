from mySQL.MysqlPython import DB_connect
#
#
class Update(DB_connect):
    con = DB_connect
    update_1 = con().Update("UPDATE actor SET first_name = 'MAr' WHERE last_name = 'WEST' ")
    print(con().connect("SELECT*FROM actor WHERE last_name = 'WEST'"))

    update_2 = con().Update("UPDATE city SET city = 'Tel Aviv' WHERE city_id = '1' ")
    print(con().connect("SELECT*FROM city WHERE city_id = '1'"))

    update_3 = con().Update("UPDATE city SET city = 'Asdod' WHERE city_id = '2'  ")
    print(con().connect("SELECT*FROM city WHERE city_id = '2'"))

    update_4 = con().Update("UPDATE actor SET first_name = 'yemiker' WHERE last_name = 'WAHLBERG' ")
    print(con().connect("SELECT*FROM actor WHERE last_name = 'WAHLBERG'"))

    update_5 = con().Update("UPDATE actor SET last_name = 'adonia' WHERE first_name = 'yemiker' ")
    print(con().connect("SELECT*FROM actor WHERE first_name = 'yemiker'"))



