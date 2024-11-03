import mysql.connector
from datetime import datetime, timedelta

def create_date_dimension_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS dwh_date;")
    cursor.execute("""
    CREATE TABLE dwh_date (
        Date_key INT PRIMARY KEY,
        Dates DATE,
        Day_name VARCHAR(20),
        Month_name VARCHAR(20),
        Year_name INT
    );
    """)
    print("Table dwh_date created successfully.")

def generate_date_records(start_date, end_date):
    delta = timedelta(days=1)
    date_records = []
    while start_date <= end_date:
        record = (
            start_date.year * 10000 + start_date.month * 100 + start_date.day,  # Date_key
            start_date.date(),  # Dates
            start_date.strftime('%A'),  # Day_name
            start_date.strftime('%B'),  # Month_name
            start_date.year  # Year_name
        )
        date_records.append(record)
        start_date += delta
    print("Date records generated successfully.")
    return date_records

def insert_data_into_table(cursor, connection, data, batch_size=1000):
    insert_query = """
    INSERT INTO dwh_date (Date_key, Dates, Day_name, Month_name, Year_name)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE Dates = VALUES(Dates);
    """
    # Insert data in smaller batches
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        cursor.executemany(insert_query, batch)
        connection.commit()  # Commit after each batch to avoid large transactions
    print("Date dimension data inserted successfully.")

def main():
    # Establish connection
    connection = mysql.connector.connect(
        host='localhost',  # Replace with your MySQL server address
        user='root',       # Your MySQL username
        password='',       # Your MySQL password
        database='dwh_ecom',
    )
    cursor = connection.cursor()

    # Create the date dimension table
    create_date_dimension_table(cursor)

    # Generate date records from 1990-01-01 to 2100-12-31
    start_date = datetime(1990, 1, 1)
    end_date = datetime(2100, 12, 31)
    date_records = generate_date_records(start_date, end_date)

    # Insert data into the table
    insert_data_into_table(cursor, connection, date_records)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("MySQL connection closed.")

if __name__ == "__main__":
    main()
