# User_Interface_ID3

## Cài đặt thư viện
```
%cd /path/project
pip install -r requirements.txt
```

## Cài đặt graphviz để chuyển đổi dạng tree sang dạng hình ảnh: [Link] (https://graphviz.org/download/)


## Cấu trúc thư mục
```
project|
       |____datasets (Xử lý dataset như lấy các thuộc tính của dataset cũng như class của dataset)
       |____utils (Chuyển đổi class TreeNode được sinh ra bởi thuật toán ID3 sang dạng graph tối ưu)
       |____id3.py (Code thuật toán train ID3)
       |____requirements.txt (File cài thư viện cần thiết)
       |____ud_id3.py (File chứa code UI của thuật toán)
```