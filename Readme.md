# Hệ thống quản lý cửa hàng bán điện thoại
## Các chức năng chính
### 1. Quản lí danh mục
- Xem danh sách điện thoại của shop bán
- Xem danh sách điện thoại với giá gốc nhập về 
- Xem danh sách các hãng điện thoại
- Thêm hãng điện thoại
- Xóa hãng điện thoại
- Lọc danh sách theo hãng
- Thêm điện thoại
- Xóa điện thoại
### 2. Quản lí đơn hàng
- Xem danh sách các đơn hàng trong tháng
- Xem chi tiết đơn hàng
- Cập nhật chi tiết đơn hàng
- Xóa đơn hàng
### 3. Thống kê báo cáo
- Hiển thị danh sách các mặt hàng sắp hết (số lượng < 10)
- Cho biết các mặt hàng bán trong tháng trước
- Cho biết doanh thu, lợi nhuận theo một tháng cụ thể


## Các chức năng bổ trợ
### Xử lí ngoại lệ, input
- Kiểm tra điều kiện nhập (sai kí tự số, kí tự đặc biệt), nhập lại
- Kiểm tra các trường hợp nhập sai định dạng tên(có số, kí tự đặc biệt), số điện thoại(không thuộc kiểu số) và tất cả các thuộc tính khác sai định dạng
- Điều kiện liên kết:
    + Khi điều chỉnh đơn hàng, kiểm tra đầy đủ các điều kiện về tên điện thoại có trong danh sách không, điều kiện về số lượng sản phẩm có đủ không
    + Duy trì sự đồng bộ về thông tin sản phẩm bán và thông tin gốc
- Lưu trữ dạng file csv. Có thể thêm sửa, xóa bằng excel (tuy nhiên dùng cách này không kiểm tra được điều kiện nhập)

## Các chạy chương trình
- Tải các package cần thiết:
```$pip install -r requirements.txt``
- Linux/Mac Os:
```$ python3 main.py```
- Windows:
```$ python main.py```

