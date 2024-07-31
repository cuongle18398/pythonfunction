import os
from dotenv import load_dotenv
import pyodbc
import pandas as pd
import time

#Cấu hình file dotenv
load_dotenv()

server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

def valiperiod():
    excel_file_path = 'Input/Offer/VPID_Input.xlsx'
    table_name = 'Inp_ERP_Offer_ValidationPeriod_Temp'
    print("Đang kết nối cơ sở dữ liệu.")
    time.sleep(1)
    try:
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
                if (i in (3,4) and row.iloc[i] == 'NaT'):
                    row.iloc[i] = '1753-01-01 00:00:00.000'
                values = f"{values},'{row.iloc[i]}'"
            values = values.lstrip(',')
            query = f"{insert_query} VALUES ({values})"
            cursor.execute(query)
            values = ""
            print(f'Line {row.iloc[1]} input !')
        time.sleep(1)
        print("Commit database.. Cập nhật vào hệ thống")
        cursor.execute('Inp_ERP_Offer_ValidationPeriod_Process')
        connection.commit()
        cursor.close()
        connection.close()
        time.sleep(1)
        print("Dữ liệu đã được cập nhật thành công.")
    except Exception as e:
        print(f"An error valiperiod function occurred: {str(e)}")


def fn_offer_process(offer_fn):
    choice = offer_fn
    try:
        if choice == '1':
            print("Đảm bảo dữ liệu đã được cập nhật trong File VPID_Input. Đang đọc dữ liệu file input..")
            time.sleep(2)
            valiperiod()
            time.sleep(1)
        # elif choice == '2':
        #     month_str = get_choice("Nhập tháng cần xóa:")
        #     if is_month(month_str):
        #         time.sleep(2)
        #         deleteTarget(server, database, username, password,month_str)
        #         time.sleep(2)
        #     else:
        #         print("Tháng không hợp lệ.")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
    except Exception as e:
        print(f"An error in main function occurred: {str(e)}")