# # TẠO CLASS TASK
# class Task:
#     def __init__(self, description):
#         self.description = description
#         self.is_done = False

#     def mark_as_done(self):
#         self.is_done = True

#     def __str__(self):
#         if self.is_done == True:
#             return "[x] {}".format(self.description)
#         else:
#             return "[ ] {}".format(self.description)


# # CÁC HÀM ĐỌC/GHI FILE
# def load_task_from_file(filename):
#     '''HÀM ĐỌC FILE'''
#     print(f"Đang tải danh sách công việc từ file: {filename}")
#     tasks_list = []

#     try:
#         with open(filename, "r", encoding="utf-8") as f:
#             for line in f:
#                 clean_line = line.strip()
#                 parts = clean_line.split(',')

#                 if len(parts) == 2:
#                     description = parts[0]
#                     status = parts[1]

#                     task_object = Task(description)
#                     if status == "done":
#                         task_object.mark_as_done()

#                     tasks_list.append(task_object)
#     except FileNotFoundError:
#         print("Không tìm thấy file danh sách cũ. Bắt đầu với danh sách công việc rỗng.")
#         return []

#     print("Đã tải danh sách công việc thành công!")
#     return tasks_list


# def save_task_to_file(tasks_list, filename):
#     '''HÀM LƯU FILE'''
#     print(f"\n Đang lưu danh sách công việc vào file: {filename}")
#     with open(filename, "w", encoding="utf-8") as f:
#         for task in tasks_list:
#             status = "done" if task.is_done else "pending"
#             line_to_write = f"{task.description},{status}\n"
#             f.write(line_to_write)

#     print(f"Đã lưu thành công!")


# TO_DO_LIST_FILENAME = "todolist.txt"
# tasks_list = load_task_from_file(TO_DO_LIST_FILENAME)

# while True:
#     print("--- TO-DO LIST ---\n")
#     print("1. Hiển thị danh sách công việc\n")
#     print("2. Thêm công việc mới\n")
#     print("3. Đánh dấu công việc đã hoàn thành\n")
#     print("4. Thoát\n")
#     selection = input("Nhập lựa chọn của bạn:").strip()

#     if selection == "1":
#         print("\n--- DANH SÁCH CÔNG VIỆC ---")
#         if not tasks_list:
#             print("Danh sách của bạn đang trống.")
#         else:
#             for task in tasks_list:
#                 print(task)

#     elif selection == "2":
#         new_task_desc = input("Hãy nhập nội dung công việc mới: ")
#         new_task_object = Task(new_task_desc)
#         tasks_list.append(new_task_object)
#         print(f"Đã thêm công việc: '{new_task_desc}'")

#     elif selection == "3":
#         print("\n--- ĐÁNH DẤU HOÀN THÀNH ---")
#         if not tasks_list:
#             print("Không có công việc nào để đánh dấu.")
#         else:
#             for i, task in enumerate(tasks_list):
#                 print(f"{i + 1}. {task}")

#             try:
#                 task_number_str = input(
#                     "Nhập số thứ tự của công việc bạn muốn đánh dấu hoàn thành: ")
#                 task_index = int(task_number_str) - 1
#                 if 0 <= task_index < len(tasks_list):
#                     tasks_list[task_index].mark_as_done()
#                     print(
#                         f"Đã đánh dấu hoàn thành: '{tasks_list[task_index].description}'")
#                 else:
#                     print("Lỗi: Số thứ tự không hợp lệ.")
#             except ValueError:
#                 print("Lỗi: Vui lòng nhập một con số.")

#     elif selection == "4":
#         save_task_to_file(tasks_list, TO_DO_LIST_FILENAME)
#         print("CẢM ƠN BẠN ĐÃ SỬ DỤNG CHƯƠNG TRÌNH!")
#         break

#     else:
#         print("Lựa chọn không hợp lệ, hãy nhập 1 trong các con số 1,2,3,4")

# TẠO CLASS TASK
class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        # Dùng f-string cho ngắn gọn và hiện đại hơn
        status_icon = "[x]" if self.is_done else "[ ]"
        return f"{status_icon} {self.description}"

# CÁC HÀM ĐỌC/GHI FILE


def load_task_from_file(filename):
    '''HÀM ĐỌC FILE'''
    print(f"Đang tải danh sách công việc từ file: {filename}")
    tasks_list = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                clean_line = line.strip()
                if not clean_line:
                    continue

                # Thêm .strip() cho từng phần để an toàn hơn
                parts = [part.strip() for part in clean_line.split(',')]

                if len(parts) == 2:
                    description, status = parts
                    task_object = Task(description)
                    if status == "done":
                        task_object.mark_as_done()
                    tasks_list.append(task_object)
    except FileNotFoundError:
        print("Không tìm thấy file danh sách cũ. Bắt đầu với danh sách công việc rỗng.")
        return []
    print("Đã tải danh sách công việc thành công!")
    return tasks_list


def save_task_to_file(tasks_list, filename):
    '''HÀM LƯU FILE'''
    print(f"\nĐang lưu danh sách công việc vào file: {filename}")
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks_list:
            status = "done" if task.is_done else "pending"
            line_to_write = f"{task.description},{status}\n"
            f.write(line_to_write)
    print(f"Đã lưu thành công!")


# --- PHẦN CHÍNH CỦA CHƯƠNG TRÌNH ---
TO_DO_LIST_FILENAME = "todolist.txt"
tasks_list = load_task_from_file(TO_DO_LIST_FILENAME)

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Hiển thị danh sách công việc")
    print("2. Thêm công việc mới")
    print("3. Đánh dấu công việc đã hoàn thành")
    print("4. Thoát")
    selection = input("Nhập lựa chọn của bạn: ").strip()

    # =================================================================
    # === CÁC DÒNG DEBUG NÂNG CAO ===
    print("\n--- DEBUG INFO ---")
    print(f"Giá trị biến 'selection': '{selection}'")
    print(f"Đại diện chính thức (repr): {repr(selection)}")
    print(f"Kiểu dữ liệu: {type(selection)}")
    print(f"So sánh với '1' có đúng không? -> {selection == '1'}")
    print("--------------------\n")
    # =================================================================

    if selection == "1":
        print("\n--- DANH SÁCH CÔNG VIỆC ---")
        if not tasks_list:
            print("Danh sách của bạn đang trống.")
        else:
            for task in tasks_list:
                print(task)

    elif selection == "2":
        new_task_desc = input("Hãy nhập nội dung công việc mới: ").strip()
        if new_task_desc:
            new_task_object = Task(new_task_desc)
            tasks_list.append(new_task_object)
            print(f"Đã thêm công việc: '{new_task_desc}'")
        else:
            print("Nội dung công việc không được để trống.")

    elif selection == "3":
        print("\n--- ĐÁNH DẤU HOÀN THÀNH ---")
        if not tasks_list:
            print("Không có công việc nào để đánh dấu.")
        else:
            for i, task in enumerate(tasks_list):
                print(f"{i + 1}. {task}")
            try:
                task_number_str = input(
                    "Nhập số thứ tự của công việc bạn muốn đánh dấu hoàn thành: ").strip()
                task_index = int(task_number_str) - 1
                if 0 <= task_index < len(tasks_list):
                    tasks_list[task_index].mark_as_done()
                    print(
                        f"Đã đánh dấu hoàn thành: '{tasks_list[task_index].description}'")
                else:
                    print("Lỗi: Số thứ tự không hợp lệ.")
            except ValueError:
                print("Lỗi: Vui lòng nhập một con số.")

    elif selection == "4":
        save_task_to_file(tasks_list, TO_DO_LIST_FILENAME)
        print("CẢM ƠN BẠN ĐÃ SỬ DỤNG CHƯƠNG TRÌNH!")
        break

    else:
        print("Lựa chọn không hợp lệ, hãy nhập một số từ 1 đến 4.")
