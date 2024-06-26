import json, sys, argparse, psycopg2, os
from datetime import datetime
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
                cur.execute("select id Id, Value valor, Date data, Description Descricao from public.register order by Date asc")
                rows = cur.fetchall()

                for i in rows:
                    print(f"> Id:{i[0]} Value: R${i[1]} | Date: {i[2]} | Descr: {i[3]}")
                
                #conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

def insert(value, desc):
    try:
        with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
            now = datetime.now()
            now_f = now.strftime("%d/%m/%Y")
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO public.register(Value, Description, Date)
                    VALUES (%s, %s, %s);
                    """,
                    (value, desc, now_f))
                conn.commit()
                
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    list()
    #value = int(input("> Digite o Valor Gasto: \n"))
    #descr = input("> Digite a Descrição: \n")
    #insert(value, descr)

if __name__ == "__main__":
    main()
