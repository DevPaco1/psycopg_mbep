import psycopg

CONN_STRING = "dbname=dvdrental user=postgres host=localhost"

with psycopg.connect(CONN_STRING) as connection:
    print("conexion exitosa")

    
    with connection.cursor() as cursor:
        cursor.execute(
            """
                SELECT *
                FROM customer
                ORDER BY customer_id
            """
        )
        def get_all_customers():
            print(cursor.fetchall())

        get_all_customers()