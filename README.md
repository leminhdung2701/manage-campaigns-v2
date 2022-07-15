# TEST
## Tên đề tài : Manage campaigns

### Mục lục
[1. Tổng quan](#1)

[2. Yêu cầu về môi trường project](#2)

[3. Tóm tắt](#3)

[4. Cách sử dụng project](#4)

============================================

### 1. Tổng quan  
* Design a program (a group of services) that provides following functionalities:

    * Manage campaigns (creating, updating, starting, stopping, duplicating, disabling)

    * A campaign is described as a json with fields.

* Ngôn ngữ chính `Python` và framework `FastAPI` 
* Sử dụng Mongo Database Atlas

* Thiết kế hệ thống

   * ![ảnh danh mục](/server/static/Manage-campaigns-Demo.drawio.png)

<a name="2"></a>

### 2. Yêu cầu về môi trường để sử dụng project
* `Python 3.8`
* `FastAPI 0.70.1`
* `Unicorn 0.15.0`
* `Gunicorn`
* `Celery`
* `Redis`
* `Flower`

<a name="3"></a>

### 3. Tóm tắt

* Tạo một campaign với nội dung truyền vào
 ```
   POST /campaign/create/ 
   ```
* Cập nhật một campaign với nội dung truyền vào
 ```
   PUT /campaign/{id_campaign}/update
   ```
* Bắt đầu khởi động một campaign
 ```
    PUT /campaign/{id_campaign}/start
   ```
* Dừng một campaign đã khởi động 
 ```
    PUT /campaign/{id_campaign}/stop
   ```
* Vô hiệu hoá một campaign đã khởi động nhưng không xoá bỏ campaign
 ```
    PUT /campaign/{id_campaign}/disable
   ```
* Nhân đôi một campaign có sẵn
 ```
    PUT /campaign/{id_campaign}/duplicate
   ```
   
### 4. Cách sử dụng project
* Clone git
    ```
   gh repo clone leminhdung2701/manage-campaigns-v2
   ```
* Build Docker
    ```
   docker-compose up --build
   ```

* Chạy demo  
    ```
   python3 demo.py   
   ```

* Chạy unit tests 
    ```
   python3 -m pytest -q -v tests/test_api.py  
   ```

* Test API
    ```
   http://0.0.0.0:8000/docs
   ```

* Flower
    ```
   http://0.0.0.0:5556/
   ```
  
  
  
  
