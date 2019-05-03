# Ghi chép về Flask_restful

### Resourceful Routing
cho phép truy cập nhiều phương thức HTTP chỉ bằng cách định nghĩa các phương thức trong mã nguồn
### Argument Parsing
Nó là 1 cách để xác thực form  
```
parser = reqparse.RequestParser()
parser.add_argument('task')
```  
`.add_argument()` được truyền vào các thuộc tính: tên của object, `type` kiểu dữ liệu, `help` mô tả, `require` True yêu cầu dữ liệu phải được truyền vào  
nếu có nhiều giá trị được truyền vào `parser` ta phải đưa vào thuộc tính `action='append'` sẽ đưa ra 1 list  
để đổi tên của object ta truyền vào thuộc tính `dest='new name'`  
thuộc tính `location` xác định chúng ta sẽ lấy dữ liệu từ đâu
```
# Look only in the POST body
parser.add_argument('name', type=int, location='form')
# Look only in the querystring
parser.add_argument('PageSize', type=int, location='args')

# From the request headers
parser.add_argument('User-Agent', location='headers')

# From http cookies
parser.add_argument('session_id', location='cookies')

# From file uploads
parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')
```  
> Lưu ý: chỉ sử dụng `type=list` khi `location='json'`  


### Data Formatting
Flask resful cung cấp `fields` module và `marshal_with()` decorator tương tự như Django ORM và WTForm, `fields` module mô tả cấu trúc dữ liệu trả về, `marshal_with()` sẽ áp dụng đúng định dạng được mô tả
