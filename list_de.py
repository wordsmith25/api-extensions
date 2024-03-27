import mysql.connector
import csv

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="laravel-test-wordsmith"
)

cursor = db.cursor()

#with open('/Users/sme/Downloads/almanyaliste.csv', mode='r', newline='', encoding='utf-8') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#    print(csv_reader.fieldnames)  # Sütun başlıklarını yazdır
#    for row in csv_reader:
#        print(row)  # İlk birkaç satırı yazdırarak kontrol et
#        break

with open('C:/Users/Zeki_Yonetim/Desktop/fetch-asin/almanyaliste.csv', mode='r', newline='', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for row in csv_reader:
        ISBN13 = row['ISBN13']
        ISBN10 = row['ISBN10']
        Inventory = row['Inventory']
        query = ("INSERT INTO AsinListDE (ISBN13, ISBN10, Inventory) VALUES (%s, %s, %s)")
        cursor.execute(query, (ISBN13, ISBN10, Inventory))

db.commit()
cursor.close()
db.close()
