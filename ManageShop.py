from MobilePhone import *
from Post import *
from ProductSell import *

import pandas as pd
from os import system
import datetime

class ManageShop:
    df_product_sells = []
    df_posts = []
    df_product_info_origin = []
    company_names = []
    
    def __init__(self, path_data='Data/'):
        ManageShop.df_product_sells = pd.read_csv(path_data + 'product_sell.csv')
        ManageShop.df_posts = pd.read_csv(path_data + "posts.csv")
        ManageShop.df_product_info_origin = pd.read_csv(path_data + "product_info.csv")
        ManageShop.company_names = open(path_data + 'company_mobilephones.txt', 'r').read().split(",")
        
    @staticmethod
    def display_main_menu():
        print("1. QUẢN LÍ DANH MỤC")
        print("2. QUẢN LÍ ĐƠN HÀNG")
        print("3. THỐNG KÊ BÁO CÁO")
        print("4. EXIT AND SAVE")
    
    @staticmethod
    def display_option1():
        print("1. Xem danh sách điện thoại của shop bán")
        print("2. Xem danh sách điện thoại với giá gốc nhập về ")    
        print("3. Xem danh sách các hãng điện thoại")
        print("4. Thêm hãng điện thoại")
        print("5. Xóa hãng điện thoại")
        print("6. Lọc danh sách theo hãng")
        print("7. Thêm điện thoại")
        print("8. Xóa điện thoại")
        print("9. Chính sửa thông tin của điện thoại")
        print("0. exit")
        
    @staticmethod
    def display_option2():    
        print("1. Xem danh sách các đơn hàng trong tháng")
        print("2. Xem chi tiết đơn hàng")
        print("3. Cập nhật chi tiết đơn hàng")
        print("4. Xóa đơn hàng")
        print("0. exit")
        
    @staticmethod
    def display_option3():    
        print("1. Hiển thị danh sách các mặt hàng sắp hết (số lượng < 10)")
        print("2. Cho biết các mặt hàng bán trong tháng trước")
        print("3. Cho biết doanh thu, lợi nhuận theo một tháng cụ thể ")
        print("0. exit")

    @staticmethod
    def add_company_names():
        print("Nhập tên hãng mới: ", end="")
        company_name = input()
        if company_name in ManageShop.company_names:
            print("Hãng này đã có trong danh sách")
        else:
            ManageShop.company_names.append(company_name)
            print("Đã thêm thành công!")
            
    @staticmethod
    def del_company_names():
        print("Nhập tên hãng cần xóa: ", end="")
        company_name = input()
        if company_name in ManageShop.company_names:
            ManageShop.company_names.remove(company_name)
            print("Đã xóa thành công!")
        else:
            print("Hãng này không có trong danh sách")        
    
    @staticmethod
    def filter_with_company_name():
        print("Nhập tên hãng cần xem: ", end="")
        company_name = input()     
        if company_name in ManageShop.company_names:
            print(ManageShop.df_product_sells[ManageShop.df_product_sells.company_name == company_name])
        else:
            print("Hãng này không có trong danh sách")
            
    
    @staticmethod
    def add_phone():
        product_sell = ProductSell() 
        # name
        print("nhập tên điện thoại: ", end='')
        name = input()
        product_sell.name = name
        if name not in ManageShop.df_product_info_origin.name.unique():
            print("Điện thoại này không có trong thông tin shop có, vui lòng thêm các thông tin khác.")
            print("Nhập tên hãng: ", end='')
            company_name = input()
            product_sell.company_name = company_name
            
            print("Nhập giá gốc: ")
            origin_price = float(input())
        else:
            pass    
        
        print("Nhập giá cần bán: ", end='')
        price = float(input())
        product_sell.price = price
        
        # amount
        print("Nhập số lượng: ", end='')
        amount = int(input())
        product_sell.amount = amount
        
        if product_sell.is_valid_info():
            pass
        else:
            print("Thông tin bạn nhập không đúng định dạng!")
    
    
    @staticmethod
    def remove_phone():
        pass
    
    @staticmethod
    def edit_phone():
        pass
            
    @staticmethod
    def loop1():
        system("clear")
        while True:
            ManageShop.display_option1()
            print("Choose: ", end="")
            choose = int(input())
            try:
                if choose == 1: # Xem danh sach dien thoai shop ban
                    print(ManageShop.df_product_sells)
                elif choose == 2: # Xem danh sach dien thoai gia goc
                    print(ManageShop.df_product_info_origin)
                elif choose == 3: # Xem danh sach cac hang dien thoai
                    print(ManageShop.company_names)
                elif choose == 4: # Them hang dien thoai
                    ManageShop.add_company_names()
                elif choose == 5: # Xoa hang dien thoai
                    ManageShop.del_company_names()
                elif choose == 6: # Loc danh sach theo hang dien thoai
                    ManageShop.filter_with_company_name()
                elif choose == 7: # Them dien thoai
                    ManageShop.add_phone()
                elif choose == 8: # Xoa dien thoai
                    ManageShop.remove_phone()
                elif choose == 9: # Chinh sua thong tin dien thoai
                    ManageShop.edit_phone()
                elif choose == 0:
                    break
                else:
                    print("only 9 options, please input again!")
                    input()
            except:
                print("Please enter number!")
                input()
            print("Press anykey to continue")
            input()
            system("clear")  
            
    
    
    @staticmethod
    def view_post_in_month():
        ManageShop.df_posts['date'] = pd.to_datetime(ManageShop.df_posts['date'], format="%d/%m/%Y")
        ManageShop.df_posts["month"] = ManageShop.df_posts["date"].apply(lambda x: x.month)
        column_view = ["id","name_product", "amount", "status", "date"]
        for month in range(1,13,1):
            print(f"\n---Month {month}---")
            df_view = ManageShop.df_posts[ManageShop.df_posts.month == month][column_view]
            print(df_view)
        
        ManageShop.drop(["month"], axis=1, inplace=True)
          
    @staticmethod
    def view_detail_post():
        print("Nhập id của post cần xem: ", end='')
        try:
            id = int(input())
            print(ManageShop.df_posts[ManageShop.df_posts.id == id].T)
        except:
            print("error input")
    
    @staticmethod
    def edit_post():
        pass
    
    @staticmethod
    def remove_post():
        pass
    
    
    @staticmethod
    def loop2():
        system("clear")
        while True:
            ManageShop.display_option2()
            try:
                print("Choose: ", end="")
                choose = int(input())
            
                if choose == 1: # Xem danh sach cac don hang trong thang
                    ManageShop.view_post_in_month()
                elif choose == 2: # Xem chi tiet don hang
                    ManageShop.view_detail_post()
                elif choose == 3: # Cap nhat chi tiet don hang
                    ManageShop.edit_post()
                elif choose == 4: # Xoa don hang
                    ManageShop.remove_post()
                elif choose == 0:
                    break
                else:
                    print("only 5 options, please input again!")
                    input()
            except:
                print("Please enter number!")
                input()
            print("Press anykey to continue")
            input()
            system("clear")  
    
    
    
    @staticmethod
    def display_rare_product():
        print(ManageShop.df_product_sells[ManageShop.df_product_sells.amount < 10])
    
    @staticmethod
    def display_product_sell_prevmonth():
        dt_cur = datetime.datetime.today()
        cur_month = dt_cur.month
        prev_month = cur_month - 1
        year = dt_cur.year
        
        if prev_month == 0:
            prev_month = 12
            year -= 1
        
        ManageShop.df_posts['date'] = pd.to_datetime(ManageShop.df_posts['date'], format="%d/%m/%Y")
        ManageShop.df_posts["month"] = ManageShop.df_posts["date"].apply(lambda x: x.month)
        ManageShop.df_posts["year"] = ManageShop.df_posts["date"].apply(lambda x: x.year)
        
        print(f"{prev_month}/{year}")
        products = ManageShop.df_posts[(ManageShop.df_posts.month == prev_month) & (ManageShop.df_posts.year == year)].name_product.unique()
        
        print(products)
        
                    
            
    @staticmethod
    def check_bussiness():
        pass
    
    @staticmethod
    def loop3():
        system("clear")
        while True:
            ManageShop.display_option3()
            try:
                print("Choose: ", end="")
                choose = int(input())
            
                if choose == 1: # Hien thi cac mat hang sap het
                    ManageShop.display_rare_product()
                elif choose == 2: # Cho biet cac mat hang ban trong thang truoc
                    ManageShop.display_product_sell_prevmonth()
                elif choose == 3: # Cho biet doanh thu, loi nhuan trong 1 thang cu the
                    ManageShop.check_bussiness()
                elif choose == 0:
                    break
                else:
                    print("only 4 options, please input again!")
                    input()
            except:
                print("Please enter number!")
                input()
            print("Press anykey to continue")
            input()
            system("clear")  
    
    @staticmethod
    def loop4():
        print("Data has been updated!")
    
    @staticmethod
    def main_loop():
        while True:
            ManageShop.display_main_menu()
            
            try:
                print("Choose: ", end="")
                choose = int(input())
            
                if choose == 1: 
                    ManageShop.loop1()
                elif choose == 2:
                    ManageShop.loop2()
                elif choose == 3:
                    ManageShop.loop3()
                elif choose == 4:
                    ManageShop.loop4()
                    break
                else:
                    print("only 4 options, please input again! Press anykey to continue")
                    input()
            except:
                print("Please enter number! Press anykey to continue")
                input()
            system("clear")
            
            
            
                  