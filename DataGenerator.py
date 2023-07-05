import mariadb
from faker import Faker
import random
from global_land_mask import globe
connection = mariadb.connect(
               host="localhost",
                port=3306,
                user="root",
                password="Satn200@",
                database = "random_database",
                
            )
print("[+] Made the connection to the database")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS person (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        age INT,
        gender VARCHAR(20),
        latitude FLOAT,
        longitude FLOAT,
        os VARCHAR(50),
        ip_address VARCHAR(50)
    )
""")


fake = Faker()
def generate_geolocation():
    
    while True:

        latitude = float(fake.latitude())
        longitude = float(fake.longitude())
        if(globe.is_land(latitude, longitude)):            
            return latitude, longitude


for i in range(50):
    name = fake.name()
    email = fake.email()
    age = fake.random_int(min=18, max=65)
    gender = fake.random_element(elements=('Male', 'Female'))
    user_os = fake.random_element(elements=('Windows', 'macOS', 'Linux', 'Android', 'iOS'))
    latitude = fake.latitude()
    longitude = fake.longitude()
    ip_address = fake.ipv4()

    
    cursor.execute("""
        INSERT INTO person (name, email, age,gender,latitude,longitude, os,ip_address)
        VALUES (%s, %s, %s,%s, %s,%s,%s,%s)
    """, (name, email,age,gender, latitude,longitude, user_os,ip_address))

print("successfully added data")
connection.commit()
connection.close()


      