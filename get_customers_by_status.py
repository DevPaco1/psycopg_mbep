import psycopg

CONN_STRING = "dbname=dvdrental user=postgres host=localhost"

with psycopg.connect(CONN_STRING) as connection:
    print("conexion exitosa")


    with connection.cursor() as cursor:
    
        def get_customers_by_status(bool):
             cursor.execute(
                f"""
                    SELECT *
                    FROM customer
                    WHERE activebool = {bool}
                    ORDER BY customer_id
                """) 
             print(cursor.fetchall())

        get_customers_by_status(False)
    
