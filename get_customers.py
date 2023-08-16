import psycopg

CONN_STRING = "dbname=dvdrental user=postgres host=localhost"

with psycopg.connect(CONN_STRING) as connection:
    print("conexion exitosa")


    with connection.cursor() as cursor:
    
        def get_customers(id: list):
            for i in id:
             cursor.execute(
                f"""
                    SELECT *
                    FROM customer
                    WHERE customer_id = {i}
                    ORDER BY customer_id
                """) 
             print(cursor.fetchmany(i))

        get_customers([1,20,3,5,10])
    

