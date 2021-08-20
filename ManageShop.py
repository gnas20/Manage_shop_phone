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
        try:
            product = ProductSell()
            print("- name: ", end='')
            product.name = input()
            
            if product.name in ManageShop.df_product_sells.name.values:
                print("Nhập số lượng cần thêm: ", end='')
                amount = int(input())
                ManageShop.df_product_sells.loc[ManageShop.df_product_sells.name == product.name, "amount"] += amount
                print("Đã thêm số lượng thành công")
            elif product.name in ManageShop.df_product_info_origin.name.values:
                product.company_name = ManageShop.df_product_info_origin.loc[
                    ManageShop.df_product_info_origin.name == product.name, "company_name"].values[0]
                origin_price = ManageShop.df_product_info_origin.loc[ManageShop.df_product_info_origin.name == product.name, "price"].values[0]
                print(f"- Giá bán (Giá gốc: {origin_price}): ", end='')
                price = float(input())
                product.price = price
            
                print("- amount: ", end='')
                amount = int(input())
                product.amount = amount
            
                product.id = int(ManageShop.df_product_info_origin.loc[ManageShop.df_product_info_origin.name == product.name, "id"].values[0])
                
                if product.is_valid_info():
                    dict_info = {key[1:]: value for key, value in product.__dict__.items()}
                    ManageShop.df_product_sells = ManageShop.df_product_sells.append(dict_info, ignore_index=True)
                    print("Mặt hàng đã được thêm")
                else:
                    print(product.__dict__)
                    print("Bạn nhập sai định dạng")  
            else:
                print("- company name: ", end='')
                company_name = input()
                if company_name not in ManageShop.company_names:
                    print("Hãng này chưa có trong danh sách, bạn cần thêm hãng này vào.")
                else:
                    product.company_name = company_name
                    print("- Giá gốc: ", end='')
                    origin_price = float(input())
                    
                    print("- Giá bán: ", end='')
                    product.price = float(input())
                    
                    print("- Số lượng: ", end='')
                    product.amount = int(input())
                    product.id = ManageShop.df_product_info_origin.id.max() + 1
                    if product.is_valid_info():
                        dict_info = {key[1:]: value for key, value in product.__dict__.items()}
                        ManageShop.df_product_sells = ManageShop.df_product_sells.append(dict_info, ignore_index=True)
                        
                        dict_info_origin = {"id": product.id, 
                                            "name": product.name,
                                            "company_name": product.company_name, 
                                            "price": origin_price}
                        ManageShop.df_product_info_origin = ManageShop.df_product_info_origin.append(dict_info, ignore_index=True)
                        print("Đã thêm thành công!")
                    else:
                        print(product.__dict__)
                        print("Bạn nhập sai định dạng")    
        except:
            print("error input")
    
    
    @staticmethod
    def remove_phone():
        print("Nhập id sản phẩm cần xóa: ", end='')
        try:
            id = int(input())
            print(f"Info of post: {ManageShop.df_product_sells[ManageShop.df_product_sells.id == id].T}")
            ManageShop.df_product_sells = ManageShop.df_product_sells.drop(
                labels=ManageShop.df_product_sells[ManageShop.df_product_sells.id == id].index, axis=0)
            print("Đã xóa thành công!")
        except:
            print("Error input")  
        
            
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
        print("Nhập id đơn hàng cần chỉnh sửa: ", end='')
        try:
            id = int(input())
            add_success = False
            if id in ManageShop.df_posts.id.values:
                post = Post()
                post.id = id
                print(f"Info of post: {ManageShop.df_posts[ManageShop.df_posts.id == id].T}")
                print("--Nhập các thông tin mới--")
                print("- name_customer: ", end='')
                post.name_customer = input()
                
                print("- address: ", end='')
                post.address = input()
                
                print("- phone_number: ", end='')
                post.phone_number = input()
                
                while True:
                    print("- name_product: ", end='')
                    post.name_product = input()
                    if post.name_product in ManageShop.df_product_sells.name.unique():
                        break
                    else:
                        print("Điện thoại này không có trong danh sách bán")
                        print("Vui lòng nhập lại")
                
                post.price = float(ManageShop.df_product_sells[ManageShop.df_product_sells.name == post.name_product].price)
                
                print("- Status(ORDERED, DELIVERING, PAID): ", end='')
                post.status = input()
                
                print("-Date(Ngày/tháng/năm): ", end='')
                post.date = input()
                
                print("- Amount: ", end='')
                post.amount = int(input())
                
                if post.is_valid_post():
                    # Check amount
                    
                    # reset amount in product_sell
                    amount_old_post = ManageShop.df_posts[ManageShop.df_posts.id == id].amount.values[0]
                    name_product_old_post = ManageShop.df_posts[ManageShop.df_posts.id == id].name_product.values[0]
        
                    ManageShop.df_product_sells.loc[ManageShop.df_product_sells.name == name_product_old_post, "amount"] += amount_old_post
            
                    # get new amount with new post
                    while True:
                        new_amount = ManageShop.df_product_sells[ManageShop.df_product_sells.name == post.name_product].amount.values[0] - post.amount
                        print(1)
                        if new_amount < 0:
                            print("Kho hàng của sản phẩm này không đủ số lượng, vui lòng nhập lại amount khác")
                        else:
                            ManageShop.df_product_sells.loc[ManageShop.df_product_sells.name == post.name_product, "amount"] -= post.amount
                            print(2)
                            break
                        print("- amount: ", end='')
                        post.amount = int(input())
                        
                    dict_info = {key[1:]: value for key, value in post.__dict__.items()}

                    # update post
                    ManageShop.df_posts.loc[ManageShop.df_posts.id == post.id, list(dict_info.keys())] = dict_info.values()
                    
                    print("Cập nhật đơn hàng thành công!")
                else:
                    print("Bạn đã nhập sai định dạng")
                    print(post.__dict__)    
            else:
                print("id không có trong danh sách")
        except:
            print("Error input!")
    
    
    @staticmethod
    def remove_post():
        print("Nhập id đơn hàng cần xóa: ", end='')
        try:
            id = int(input())
            print(f"Info of post: {ManageShop.df_posts[ManageShop.df_posts.id == id].T}")
            ManageShop.df_posts = ManageShop.df_posts.drop(labels=ManageShop.df_posts[ManageShop.df_posts.id == id].index, axis=0)
            ManageShop.df_posts.id = range(0, ManageShop.df_posts.shape[0])
            print("Đã xóa thành công và cập nhật lại id.")
        except:
            print("Error input")    
    
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
        try:
            month, year = 1, 2000
            while True:
                print("- month: ", end='')
                month = int(input())
                if month >= 1 and month <= 12:
                    break
                else:
                    print("error month: 1 <= month <= 12")
                    
            while True:
                print("- year: ", end='')
                year = int(input())
                current_year = datetime.datetime.today().year
                if year >= 2000 or year <= current_year:               
                    break
                else:
                    print("error month: 1 <= month <= 12")
                    
            ManageShop.df_posts['date'] = pd.to_datetime(ManageShop.df_posts['date'], format="%d/%m/%Y")
            ManageShop.df_posts["month"] = ManageShop.df_posts["date"].apply(lambda x: x.month)
            ManageShop.df_posts["year"] = ManageShop.df_posts["date"].apply(lambda x: x.year)
            ManageShop.df_posts["sum_money"] = ManageShop.df_posts.price*ManageShop.df_posts.amount
            # revenue
            revenue = ManageShop.df_posts[(ManageShop.df_posts.year == year) & (ManageShop.df_posts.month == month)]["sum_money"].sum()
            
            # profit
            def get_origin_price_col(x):
                return ManageShop.df_product_info_origin .loc[ManageShop.df_product_info_origin.name == x.name_product, "price"].values[0]

            ManageShop.df_posts['origin_price'] = ManageShop.df_posts.apply(lambda x: get_origin_price_col(x), axis=1)
            
            ManageShop.df_posts["sum_money_origin"] = ManageShop.df_posts.origin_price*ManageShop.df_posts.amount
            profit = ManageShop.df_posts[(ManageShop.df_posts.year == year) & (ManageShop.df_posts.month == month)]["sum_money_origin"].sum()
            
            print(f"- Doanh thu: {revenue}")
            print(f"- Lợi nhuận: {profit}")
            ManageShop.df_posts = ManageShop.df_posts.drop(["month", "year", "sum_money", "origin_price", "sum_money_origin"], axis=1)
             
        except:
            print("error input")
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
        ManageShop.df_product_info_origin.to_csv("Data/product_info.csv", index=False)
        ManageShop.df_product_sells.to_csv("Data/product_sell.csv", index=False)
        ManageShop.df_posts.to_csv("Data/posts.csv", index=False)
        f = open("Data/company_mobilephones.txt", 'w')
        f.write(",".join(ManageShop.company_names))
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
            
            
            
                  