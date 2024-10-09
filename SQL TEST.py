import psycopg2

conn = psycopg2.connect(database = "DanielsCooleDatabase", 
                        user = "postgres", 
                        host= '135.236.57.232',
                        password = "c+]O2<*_ 6uJ8f[.S~50",
                        port = 5432)


# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datacamp_courses table

cur.execute("""CREATE TABLE users (
            username SERIAL PRIMARY KEY,
            wachtwoord VARCHAR (50) UNIQUE NOT NULL,
            highscore integer);
            """)

# Make the changes to the database persistent
conn.commit()
# Close cursor and communication with the database
cur.close()
conn.close()




""" set DBHOST="135.236.57.232"
set DBNAME="DanielsCooleDatabase"
set DBUSER="postgres"
set SSLMODE=require """