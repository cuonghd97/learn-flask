# Tìm hiểu về framework flask của python  
 cấu trúc cơ bản của một project flask như sau:  
```
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```  
+ flaskr: package này chứa code  
+ test: chứa các test module
+ venv: môi trường ảo của python

> Trong tutorial chúng ta sẽ dùng cơ sở dữ liệu sqlite  

### Kết nối với database

`flaskr/db.py`  
```
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```  
`g`: là một đối tượng đặc biệt duy nhất cho mỗi request. Nó dùng để lưu trữ dữ liệu có thể truy cập bởi nhiều hàm trong suốt các request. Kết nối được lưu trữ và dùng lại thay cho việc tạo một kết nối mới nếu `get_db` được gọi lần 2 trong cùng một request.

### Tạo bảng
`flaskr/chema.sql`  
```
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```
> Thêm các hàm sau vào `db.py` để thực hiện các câu lệnh sql  

`flaskr/db.py`  
```
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```  
`open_resource()`: mở các file liên quan đến package flaskr, nó rất hữu dụng nếu bán không cần biết vị trí file sql khi triển khai ứng dụng. Hàm `get_db` trả về kết nối database dùng để đọc các câu lệnh sql trong file sql.  
`click.command()`:  định nghĩa một dòng lệnh gọi là init-db, hàm này hiển thị kết quả là thông báo success trên CLI.  

Hàm `close_db` và `init_db_command` cần được khai báo  

> Chạy flask init-db để khởi tạo các bảng  

### Blueprint and Views
#### Blueprint
Blueprint là cách tổ chức nhóm các view liên quan và code. Thay vì khai báo views và code thẳng đến một ứng dụng, ta khai báo với 1 blueprint  
`Flaskr` sẽ có 2 blueprint:  
+ Cho các hàm authentications
`flaskr/auth.py`  
```
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```  
Blueprint này được đặt tên là `auth`, `url_prefix` sẽ được thêm vào tất cả các url liên kết với Blueprint
+ Cho các hàm liên quan đến blog

Code trongh các blueprint được chia thành các module `auth.py` và `blog.py`

