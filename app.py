import psycopg2, os, click, docker
from datetime import datetime
from dotenv import load_dotenv

# - Author: Pablo Andrade
# - Created: 28/06/2024
# - Version: 0.1.1

"""
    TODO: fix redundancy
"""

load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
CONTAINER = os.getenv("CONTAINER")

client = docker.from_env()
postgre = client.containers.get(CONTAINER)
if (postgre.status) != "running":
    postgre.start
    if (postgre.status) == "running":
        pass

@click.group()
def cli():
    """> Program to keep control of weekly financial expenses."""
    pass

@cli.command(help="> List items from the register")
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

@cli.command(help="> Insert a new item into the register")
@click.argument('value', type=float)
@click.argument('desc')
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

@cli.command(help="> Delete an item from the register by Id")
@click.argument('id', type=float)
def delete(id):
    try:
        with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM public.register where Id = %s;
                    """,
                    (id,))
                conn.commit()

    except Exception as e:
        print(f"> An error occurred: {e}")

@cli.command(help="> Clear all items from the register")
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

@cli.command(help="> Update the weekly budget value")
@click.argument('value', type=float)
def week(value):
    try:
        with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE public.week SET const = %s WHERE id = 1;
                    """,
                    (value,))
                print("> Week value updated.")
                conn.commit()

    except Exception as e:
        print(f"> An error occurred: {e}")

@cli.command(help="> Check the current spend and remaining budget")
def check():
    try:
        with psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=int(PORT)) as conn:
            with conn.cursor() as cur:
                cur.execute("select sum(Value) from public.register")
                sum = cur.fetchone()
                if sum[0] is not None:
                    sum_value = sum[0]

                cur.execute("select const from public.week")
                week = cur.fetchone()
                if week[0] is not None:
                    week_value = week[0]
                
                if sum_value is not None and week_value is not None:
                    left = week_value - sum_value
                    print(f"> Spend: R${sum_value} Week: R${week_value} ->> Left: R${left}")
                else:
                    print("> Data not available.")

    except Exception as e:
        print(f"> An error occurred: {e}")

if __name__ == "__main__":
    cli(prog_name='app')
