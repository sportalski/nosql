import psycopg2

def insert_data():
    file_path = "J:/MongoDB/Server/3.0/bin/trades.json"
    connection = psycopg2.connect(database="postgres", user="postgres", password="a")

    cursor = connection.cursor()
    print("Reading started")
    with open(file_path, "rb") as file:
        i = 1
        for r in file:
            cursor.execute("INSERT INTO trades (data) VALUES ('%s')" % (r))
            i = i + 1
            if  i % 10000 == 0:
                connection.commit()
                print("Inserted " + str(i) + " trades.")
        print("Inserting finished.")
    connection.commit()
    cursor.close()
    connection.close()

insert_data()
