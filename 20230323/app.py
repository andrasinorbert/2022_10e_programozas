#SELECT * FROM `adatok`;
#INSERT INTO `adatok`(`név`, `kor`, `magasság`) VALUES ('Julcsi', '13', '170');

import pymysql
# pip install pymysql

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