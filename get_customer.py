import psycopg

CONN_STRING = "dbname=dvdrental user=postgres host=localhost"

with psycopg.connect(CONN_STRING) as connection:
    print("conexion exitosa")


    with connection.cursor() as cursor:
    
        def get_customer(id):
             cursor.execute(
                f"""
                    SELECT *
                    FROM customer
                    WHERE customer_id = {id}
                    ORDER BY customer_id
                """) 
             print(cursor.fetchone())

        get_customer(4)
    