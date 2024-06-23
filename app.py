import json, sys, argparse, psycopg2, os
import datetime
from dotenv import load_dotenv

load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

def list():
    try:
        with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
            with conn.cursor() as cur:
                cur.execute("select Value valor, Date data, Description Descricao from public.register order by Date asc")
                rows = cur.fetchall()

                for i in rows:
                    print(f"> Value: {i[0]} | Date: {i[1]} | Desc: {i[2]}")
                
                #conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

def insert(value, desc):
    try:
        with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
            with conn.cursor() as cur:
                cur.execute("select Value valor, Date data, Description Descricao from public.register order by Date asc")
                rows = cur.fetchall()

                for i in rows:
                    print(f"> Value: {i[0]} | Date: {i[1]} | Desc: {i[2]}")
                
                conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    list()

if __name__ == "__main__":
    main()
