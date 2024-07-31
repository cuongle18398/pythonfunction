import pyodbc
import pandas as pd
import time
import openpyxl

def clearvt(server, database, username, password):
    try:
        excel_file_path = 'Input/ClearVT_Input.xlsx'
        table_name = 'HR_FP_ClearVT'
        #Tạo connection và đọc file excel
        print("Đang kết nối cơ sở dữ liệu.")
        time.sleep(1)
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        connection = pyodbc.connect(connection_string)
        excel_data = pd.read_excel(excel_file_path, skiprows=3)
        insert_query = f'INSERT INTO {table_name} ({", ".join(excel_data.columns)})'
        cursor = connection.cursor()
        time.sleep(1)
        print("Kết nối thành công. Dữ liệu đang được import!")
        time.sleep(1)
        for index, row in excel_data.iterrows():
            values = ""
            for i in range(0,2):
                values = f"{values},'{row.iloc[i]}'"
            values = values.lstrip(',')
            query = f"{insert_query} VALUES ({values})"
            cursor.execute(query)
            values = ""
            print(f'Line {row.iloc[0]} input !')
        connection.commit()
        cursor.close()
        connection.close()
        time.sleep(1)
        print("Dữ liệu đã được cập nhật thành công.")
    except Exception as e:
        print(f"An error uploadTarget function occurred: {str(e)}")


def checkout(server, database, username, password):
    try:
        print("Đang truy xuất cơ sở dữ liệu.")
        time.sleep(2)
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        connection = pyodbc.connect(connection_string)
        query = f'EXEC [sp_HR_FP_ClearVT_Update] @type = 2'
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
        time.sleep(1)
        print("Dữ liệu Checkout được cập nhật thành công.")
    except Exception as e:
        print(f"An error HR function - checkout occurred: {str(e)}")


def createstaff(server, database, username, password):
    try:
        excel_file_path = 'Input/Staff_Input.xlsx'
        table_name = 'HR_Staff_Temp'
        #Tạo connection và đọc file excel
        print("Đang kết nối cơ sở dữ liệu.")
        time.sleep(1)
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        connection = pyodbc.connect(connection_string)
        excel_data = pd.read_excel(excel_file_path, skiprows=3)
        insert_query = f'INSERT INTO {table_name} ({", ".join(excel_data.columns)})'
        cursor = connection.cursor()
        time.sleep(1)
        print("Kết nối thành công. Dữ liệu đang được import!")
        time.sleep(1)
        for index, row in excel_data.iterrows():
            values = ""
            for i in range(0,4):
                if i == 2 or i == 3:
                    values = f"{values},N'{row.iloc[i]}'"
                else:
                    values = f"{values},'{row.iloc[i]}'"
            values = values.lstrip(',')
            query = f"{insert_query} VALUES ({values})"
            cursor.execute(query)
            values = ""
            print(f'Line {row.iloc[1]} input !')
        print("Commit database.. Cập nhật vào hệ thống")
        time.sleep(1)
        cursor.execute('EXEC sp_HR_StaffID_Update')
        connection.commit()
        cursor.close()
        connection.close()
        time.sleep(1)
        print("Dữ liệu đã được cập nhật thành công.")
    except Exception as e:
        print(f"An error createstaff function occurred: {str(e)}")