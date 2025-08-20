# ==============================================================================
# IMPORT CÁC THƯ VIỆN CẦN THIẾT
# ==============================================================================
# render_template: để render file HTML
# request: để truy cập dữ liệu từ form (GET, POST)
# redirect, url_for: để chuyển hướng người dùng
from flask import Flask, render_template, request, redirect, url_for

# ==============================================================================
# ĐỊNH NGHĨA CLASS VÀ CÁC HÀM HỖ TRỢ (LOGIC CỐT LÕI)
# ==============================================================================


class Task:
    """Đại diện cho một công việc trong danh sách To-Do."""

    def __init__(self, description):
        self.description = description
        self.is_done = False

    def mark_as_done(self):
        """Đánh dấu công việc là đã hoàn thành."""
        self.is_done = True

    def __str__(self):
        """Định nghĩa cách đối tượng Task được hiển thị dưới dạng chuỗi."""
        status_icon = "[x]" if self.is_done else "[ ]"
        return f"{status_icon} {self.description}"


def load_tasks_from_file(filename):
    """Đọc file và tái tạo lại danh sách các đối tượng Task."""
    tasks_list = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                clean_line = line.strip()
                if not clean_line:
                    continue

                parts = [part.strip() for part in clean_line.split(',')]
                if len(parts) == 2:
                    description, status = parts
                    task_object = Task(description)
                    if status == "done":
                        task_object.mark_as_done()
                    tasks_list.append(task_object)
    except FileNotFoundError:
        print(
            f"Cảnh báo: Không tìm thấy file {filename}. Bắt đầu với danh sách rỗng.")
    return tasks_list


def save_tasks_to_file(tasks_list, filename):
    """Lưu danh sách các đối tượng Task vào file."""
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks_list:
            status = "done" if task.is_done else "pending"
            line_to_write = f"{task.description},{status}\n"
            f.write(line_to_write)

# ==============================================================================
# KHỞI TẠO ỨNG DỤNG FLASK VÀ CẤU HÌNH
# ==============================================================================


app = Flask(__name__)
TO_DO_LIST_FILENAME = "todolist.txt"

# ==============================================================================
# ĐỊNH NGHĨA CÁC ROUTE (CÁC TRANG CỦA WEB)
# ==============================================================================


@app.route('/', methods=['GET', 'POST'])
def home():
    """Route chính, xử lý cả việc hiển thị và thêm mới công việc."""
    if request.method == 'POST':
        # Xử lý logic khi người dùng THÊM công việc mới
        task_description = request.form.get('task_desc', '').strip()
        if task_description:
            tasks = load_tasks_from_file(TO_DO_LIST_FILENAME)
            tasks.append(Task(task_description))
            save_tasks_to_file(tasks, TO_DO_LIST_FILENAME)
        return redirect(url_for('home'))
    else:  # request.method == 'GET'
        # Logic khi người dùng chỉ XEM trang
        all_tasks = load_tasks_from_file(TO_DO_LIST_FILENAME)
        return render_template('index.html', tasks=all_tasks)


@app.route('/done/<int:task_index>', methods=['POST'])
def mark_task_as_done(task_index):
    """Route để đánh dấu một công việc là đã hoàn thành."""
    tasks = load_tasks_from_file(TO_DO_LIST_FILENAME)
    if 0 <= task_index < len(tasks):
        tasks[task_index].mark_as_done()
        save_tasks_to_file(tasks, TO_DO_LIST_FILENAME)
    return redirect(url_for('home'))


@app.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    """Route để xóa một công việc."""
    tasks = load_tasks_from_file(TO_DO_LIST_FILENAME)
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks_to_file(tasks, TO_DO_LIST_FILENAME)
    return redirect(url_for('home'))

# ==============================================================================
# CHẠY ỨNG DỤNG
# ==============================================================================


if __name__ == '__main__':
    # debug=True giúp server tự động khởi động lại khi có thay đổi trong code
    app.run(debug=True)
