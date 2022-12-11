import psycopg2
with psycopg2.connect(database="HW5", user="postgres", password="Ntktajif") as conn: 

# Функция, создающая структуру БД (таблицы)         
    def create_db(conn):
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Clients(
            id_client INTEGER UNIQUE PRIMARY KEY, 
            name VARCHAR(100), 
            surname VARCHAR(100), 
            email VARCHAR(100));""")
    
        cur.execute("""CREATE TABLE IF NOT EXISTS Phone_numbers (
            id_number SERIAL PRIMARY KEY, 
            id_client INTEGER REFERENCES Clients(id_client), 
            phone_number VARCHAR(20));""")
        conn.commit()     

    # Функция, позволяющая добавить нового клиента
    def add_client(conn, id_client, name, surname, email, phone_number=None):
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Clients(id_client, name, surname, email) VALUES(%s, %s, %s, %s);
            """, (id_client, name, surname, email))
        conn.commit()
    
        cur.execute("""
            SELECT * FROM Clients;
            """)
        print(cur.fetchall())
        
    # Функция, позволяющая добавить телефон для существующего клиента
    def add_phone(conn, id_client, phone_number):
        cur = conn.cursor()
        cur.execute("""
            UPDATE Phone_numbers SET phone_number=%s WHERE id_client=%s;
            """, (phone_number, id_client))
        conn.commit() 
    
        cur.execute("""
            SELECT * FROM Phone_numbers;
            """)
        print(cur.fetchall())
        
# Функция, позволяющая изменить данные о клиенте
    def change_client(conn, id_client, id_number, name=None, surname=None, email=None, phone_number=None):
        cur = conn.cursor()
        cur.execute ("""
            UPDATE Clients SET name = %s WHERE id_client = %s;
            """, (name, id_client))
        conn.commit()
    
        cur.execute ("""
            UPDATE Clients SET surname = %s WHERE id_client = %s;
            """, (surname, id_client))
        conn.commit()
    
        cur.execute ("""
            UPDATE Clients SET email = %s WHERE id_client = %s;
            """, (email, id_client))
        conn.commit()
    
        cur.execute("""
            SELECT * FROM Clients;
            """)
        print(cur.fetchall())   

        cur.execute ("""
            UPDATE Phone_numbers SET id_client = %s WHERE id_number = %s;
            """, (id_client, id_number))
        conn.commit()
    
        cur.execute ("""
            UPDATE Phone_numbers SET phone_number = %s WHERE id_number = %s;
            """, (phone_number, id_number))
        conn.commit()
    
        cur.execute("""
            SELECT * FROM Phone_numbers;
            """)
        print(cur.fetchall())  
        
        
# Функция, позволяющая удалить телефон для существующего клиента
    def delete_phone(conn, id_client, id_number, phone_number):
        cur = conn.cursor()
        cur.execute ("""DELETE Phone_numbers WHERE id_number = %s;
            """, (id_number))
        conn.commit()

# Функция, позволяющая удалить существующего клиента
    def delete_client(conn, id_client):
        cur = conn.cursor()
        cur.execute ("""
            DELETE FROM Clients WHERE id_client = %s;
            """, (id_client))
        conn.commit()
        
# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
    def find_client(conn, name=None, surname=None, email=None, phone_number=None):
        cur = conn.cursor()
        cur.execute ("""SELECT name, surname, email, phone_number FROM Clients WHERE name LIKE %s,
        """, (name))
        print(cur.fetchall()) 
    
        cur.execute ("""SELECT name, surname, email, phone_number FROM Clients WHERE surname LIKE %s,
        """, (surname))
        print(cur.fetchall()) 
    
        cur.execute ("""SELECT name, surname, email, phone_number FROM Clients WHERE email LIKE %s,
        """, (email))
        print(cur.fetchall()) 
    
        cur.execute ("""SELECT id_client FROM Phone_numbers WHERE phone_number LIKE %s;
        """, (phone_number))
        print(cur.fetchall()) 

with psycopg2.connect(database="HW5", user="postgres", password="Ntktajif") as conn:
    

    tables = create_db(conn)
    
    new_client1 = add_client(conn, 1, 'Ivan', 'Ivanov', 'i.ivanov@mail.ru')
    new_client2 = add_client(conn, 2, 'Petr', 'Petrov', 'p.petrovv@mail.ru')
    new_client3 = add_client(conn, 2, 'Ann', 'Black', 'annblack@gmail.com')
    
    new_phone1 = add_phone(conn, 1, '3422')
    new_phone2 = add_phone(conn, 2, '1234')
    new_phone3 = add_phone(conn, 3, '4312')

    change1 = change_client(conn, 1, 1, 'Ivan', 'Vasin', 'i.vasin@mail.ru')

    delete_ph1 = delete_phone(conn, 2, 2,'1234')
    
    delete_cl1 = delete_client(conn, 2)
    
    find_info = find_client(conn, 'Ann')
    
conn.close()
