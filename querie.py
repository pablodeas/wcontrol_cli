import sys
import psycopg2
from dotenv import load_dotenv
from app import USER
from app import PASSWORD
from app import DATABASE
from app import HOST
from app import PORT

def main():
    try:
        with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
            with conn.cursor() as cur:
                cur.execute("""CREATE TABLE IF NOT EXISTS Week(
                        	    Id int primary key,
	                            Const int not null
                            );""")
                rows = cur.fetchall()

                for i in rows:
                    print(f"> {i}")

                conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
