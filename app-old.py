# Import thêm thư viện datetime để làm việc với thời gian
from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    # Lấy thời gian hiện tại từ hệ thống
    now = datetime.datetime.now()
    # Định dạng nó thành một chuỗi dễ đọc (Giờ:Phút:Giây ngày-tháng-năm)
    time_string = now.strftime("%H:%M:%S ngày %d-%m-%Y")

    # Truyền biến time_string vào template.
    # Tên biến bên trái ('current_time') là tên chúng ta sẽ dùng trong file HTML.
    # Tên biến bên phải ('time_string') là biến trong code Python này.
    return render_template('index.html', current_time=time_string)


if __name__ == '__main__':
    app.run(debug=True)
