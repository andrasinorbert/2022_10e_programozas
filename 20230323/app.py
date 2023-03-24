#SELECT * FROM `adatok`;
#INSERT INTO `adatok`(`név`, `kor`, `magasság`) VALUES ('Julcsi', '13', '170');

# Telepítettük a XAMPP alkalmazást (cross-platform)
# elinditottuk az apache-ot és mysql-t
#     ha valakinek hibát ir, hogy foglalt a port:
#         config gomb, ini fájl szerkesztése
#         a port számot mindenhol kicserüljük valami újra
# megnyitottuk böngészőben a localhost/phpmyadmin felületet
# bal oldalon készítettünk adatbázist (pl: 10e néven)
# létrehoztunk egy táblát 4 oszloppal (pl: adatok néven)
# megj.: az adatbázis név, táblanév ne tartalmazzon ékezetet, szóközt
# az oszlopok:
#     oszlopnév - tipus - egyéb
#     id - int - A_I oszlop pipa
#     név - varchar - maxhossz
#     kor - int
#     magasság - int
# a táblára kattintva a felső menüsorban kiválasztottuk a "jogok" fület
# új felhasználó létrehozása (szóközt ékezetet ne tartalmazzanak a mezők)
#     név: 10e_user
#     password: 10e_user (2 helyen kell megadni)
#     Hely: legördülő menü -> helyi
#     a többi dolgot békénhagytuk


import pymysql
# terminál: pip install pymysql

defaults={
    "DB_USER": "10e_user",
    "DB_PASSWD":"10e_user",
    "DB_HOST":"127.0.0.1",
    "DB_TABLE":"adatok",
    "DB_NAME":"10e"
}
def dbConn(_host, _dbname, _username, _passwd):
    return pymysql.Connection(
                    host=_host,
                    database=_dbname,
                    user=_username,
                    password=_passwd
                    )

def insertDB(nev, kor, magassag):
    conn=dbConn(
            defaults["DB_HOST"],
            defaults["DB_NAME"],
            defaults["DB_USER"],
            defaults["DB_PASSWD"]
            )
    cursor=conn.cursor()
    sql=f"INSERT INTO `adatok`(`név`, `kor`, `magasság`) VALUES ('{nev}', '{kor}', '{magassag}');"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def adatbekeres():
    nev = input("név=")
    kor= input("kor=")
    magassag=input("magasság=")
    insertDB(nev, kor, magassag)

adatbekeres()