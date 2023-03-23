
# INSERT INTO `elso`(`Név`, `Kor`, `Magasság`) VALUES ('Béla', '12', '150');

# SELECT Kor FROM `elso`;

import pymysql
# pip install pymysql

defaults= {
    "DB_HOST": "127.0.0.1",
    "DB_NAME": "10b",
    "DB_TABLE": "elso",
    "DB_UNAME": "10b_user",
    "DB_PASSWD": "10b_user"
}

conn=pymysql.connect(host=defaults["DB_HOST"],
                     user=defaults["DB_UNAME"],
                     password=defaults["DB_PASSWD"],
                     database=defaults["DB_NAME"])

cursor = conn.cursor()
sql = "INSERT INTO `elso`(`Név`, `Kor`, `Magasság`) VALUES ('Józsi', '15', '142');"
cursor.execute(sql)
conn.commit()
conn.close()

