import pandas as pd
import pyodbc

def upload_excel_to_sql_server(excel_file_path, server, database, username, password, table_name):
    try:
        print("Uploading DataMachine..")
        # Create a connection string
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Establish a connection to the SQL Server
        connection = pyodbc.connect(connection_string)

        # Read the Excel file into a pandas DataFrame
        excel_data = pd.read_excel(excel_file_path, skiprows=0)


        # Create a cursor for executing SQL queries
        cursor = connection.cursor()

        # Define the SQL query to insert data into the SQL Server table
        insert_query = f'INSERT INTO {table_name} ({", ".join([f"[{col}]" for col in excel_data.columns])})'

        # Create a cursor for executing SQL queries
        cursor = connection.cursor()

        # Iterate over rows in the Excel data and insert them into the SQL Server table
        for index, row in excel_data.iterrows():
            values = ""
            for i in range(0,9):
                if i in (6,7) and pd.isna(row[i]):
                    values = f"{values},''"
                else:
                    if i in (1,2,3) and row[i] != "":
                        values = f"{values},N'{row[i]}'"
                    else:
                        values = f"{values},'{row[i]}'"
            values = values.lstrip(',')
            query = f"{insert_query} VALUES ({values})"
            cursor.execute(query)
            values = ""
            #cursor.execute(insert_query)
            
        cursor.execute('EXEC sp_Import_DataMachine')
        # Commit the changes and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    # Define your connection and file details
    server = 'HSVFPTDB07'
    database = 'LSReport'
    username = 'dd'
    password = 'Hoahuongduong2908'
    excel_file_path = 'DataMachine.xlsx'
    table_name = 'DataMaChineTemp'

    # Call the upload function
    upload_excel_to_sql_server(excel_file_path, server, database, username, password, table_name)
    print("Upload DataMachine Success !")

if __name__ == "__main__":
    main()
