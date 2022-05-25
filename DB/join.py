from MysqlPython import DB_connect

class join(DB_connect):
    con = DB_connect
    join_1 = con().connect("SELECT address.phone,city.city_id FROM city INNER JOIN address ON city.city_id=address.city_id; ")


    join_2 = con().connect("SELECT city.city,country.country FROM city INNER JOIN country ON country.country_id=city.country_id;")


