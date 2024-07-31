import os
from dotenv import load_dotenv
import time
from Target import uploadTarget, deleteTarget
from HR_Function import clearvt, checkout, createstaff
from Item import statusUpdate, item_choice_fn
from offer import fn_offer_process

#Cấu hình file dotenv
load_dotenv()

server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

def display_main_menu():
    print("\n Chọn chức năng thực hiện:")
    print("1. Import Target HTCH            2. Delete Target HTCH")
    print("3. Update Item Value             4. Update Status Item")
    print("5. Import DS Clear VT            6. Checkout DS Clear VT")
    print("7. Create StaffID                8. CTKM")
    print("0. Thoát")

def display_item_menu():
    print("1. Description                   2. VN Description")
    print("3. Shelf-life                    4. VAT Posting ")
    print("5. Vendor No                     6. Vendor Item No")


def display_offer_menu():
    print("1ffer Header")

def get_choice(text):
    choice = input(text)
    return choice

def is_month(input):
    try:
        number = int(input)
        if 1 <= number <= 12:
            return True
        else:
            return False
    except ValueError:
        return False

def main():
    try:
        while True:
            display_main_menu()
            choice = get_choice("Nhập lựa chọn của bạn: ")
            if choice == '1':
                print("Đảm bảo dữ liệu đã được cập nhật trong File Target_Input. Đang đọc dữ liệu file input..")
                time.sleep(2)
                uploadTarget(server, database, username, password)
                time.sleep(2)
            elif choice == '2':
                month_str = get_choice("Nhập tháng cần xóa:")
                if is_month(month_str):
                    time.sleep(2)
                    deleteTarget(server, database, username, password,month_str)
                    time.sleep(2)
                else:
                    print("Tháng không hợp lệ.")
            elif choice == '3':
                print("Chọn Trường thông tin cần cập nhật:")
                time.sleep(2)
                display_item_menu()
                item_fn = get_choice("Nhập lựa chọn của bạn: ")
                time.sleep(1)
                item_choice_fn(choice)
                time.sleep(2)
            elif choice == '4':
                print("Đảm bảo dữ liệu đã được cập nhật trong File Status_Input. Đang đọc dữ liệu file input..")
                time.sleep(2)
                statusUpdate(server, database, username, password)
            elif choice == '5':
                print("Đảm bảo dữ liệu đã được cập nhật trong File ClearVT_Input. Đang đọc dữ liệu file input..")
                time.sleep(2)
                clearvt(server, database, username, password)
                time.sleep(2)
            elif choice == '6':
                checkout(server, database, username, password)
                time.sleep(2)
            elif choice == '7':
                print("Đảm bảo dữ liệu đã được cập nhật trong File Staff_Input. Đang đọc dữ liệu file input..")
                time.sleep(2)
                createstaff(server, database, username, password)
                time.sleep(2)
            elif choice == '8':
                print("Chọn Trường thông tin cần cập nhật: ")
                time.sleep(2)
                display_offer_menu()
                offer_fn = get_choice("Nhập lựa chọn của bạn: ")
                time.sleep(1)
                if offer_fn in ('1','2'):
                    fn_offer_process(offer_fn)
                else:
                    print("Lựa chọn không hợp lệ.")
                    break
            elif choice == '0':
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
                break
    except Exception as e:
        print(f"An error in main function occurred: {str(e)}")


if __name__ == "__main__":
    main()

