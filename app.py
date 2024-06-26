import psycopg2, os, click
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
                    print(f"> Id:{i[0]} | Value: R${i[1]} | Date: {i[2]} | Descr: {i[3]}")
                
                #conn.commit()
    except Exception as e:
        print(f"> An error occurred: {e}")

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
        print(f"> An error occurred: {e}")

def delete(id):
    try:
        with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM public.register where Id = %s;
                    """,
                    (id))
                conn.commit()

    except Exception as e:
        print(f"> An error occurred: {e}")

def clear():
    try:
        case = input("> WARNING - You will clear all values. Are you sure? (Y)-Yes or (N)-No\n> ")
        
        if case == "Y":
            with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        DELETE FROM public.register;
                        """)
                    conn.commit()
                    print("> All clear.")
        else:
            pass

    except Exception as e:
        print(f"> An error occurred: {e}")

def check():
    try:
        with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
            with conn.cursor() as cur:
                cur.execute("select sum(Value) from public.register")
                sum = cur.fetchone()
                if sum[0] is not None or Null:
                    sum_value = sum[0]

                cur.execute("select const from public.week")
                week = cur.fetchone()
                if week[0] is not None or Null:
                    week_value = week[0]
                
                left = week_value - sum_value
                print(f"> Spend: R${sum_value} Week: R${week_value} ->> Left: R${left}")
                

    except Exception as e:
        print(f"> An error occurred: {e}")

def main():
    list()
    
    #value = int(input("> Value: \n> "))
    #descr = input("> Descr: \n> ")
    #insert(value, descr)
    
    #id = input(f"> Which Id: \n> ")
    #delete(id)

    clear()

    #check()

if __name__ == "__main__":
    main()
