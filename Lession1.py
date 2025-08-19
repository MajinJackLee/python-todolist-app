shopping_cart = {}

shopping_cart["Táo"] = 5
shopping_cart["Mít"] = 3
shopping_cart["Kem"] = 2


def save_cart_to_file(cart, filename):
    """
    Hàm này nhận một dictionary giỏ hàng và lưu nó vào file.
    File sẽ bị ghi đè mỗi lần lưu.
    """
    print(f"\n... Đang lưu giỏ hàng vào file {filename} ...")

    # 1. Mở file ở chế độ 'w' (write) để ghi mới hoàn toàn.
    # 'encoding="utf-8"' rất quan trọng cho tiếng Việt.
    with open(filename, "w", encoding="utf-8") as f:

        # 2. Duyệt qua từng cặp (món hàng, số lượng) trong dictionary.
        for item, quantity in cart.items():

            # 3. Tạo một chuỗi theo đúng định dạng yêu cầu.
            # Ví dụ: item="Táo", quantity=10 -> line_to_write = "Táo,10\n"
            # Thêm "\n" để mỗi món hàng nằm trên một dòng riêng.
            line_to_write = f"{item},{quantity}\n"

            # 4. Ghi chuỗi đó vào file.
            f.write(line_to_write)

    print("Lưu thành công!")


def load_cart_from_file(filename):
    """
    Hàm này đọc dữ liệu từ file và tái tạo lại dictionary giỏ hàng.
    Nếu file không tồn tại, nó trả về một giỏ hàng rỗng.
    """
    print(f"... Đang tải giỏ hàng từ file {filename} ...")
    cart = {}  # 1. Bắt đầu với một giỏ hàng rỗng.

    try:
        # 2. Mở file ở chế độ 'r' (read).
        with open(filename, "r", encoding="utf-8") as f:

            # 3. Duyệt qua từng dòng trong file.
            for line in f:

                # 4. Xử lý từng dòng:
                # Dòng đọc được có thể là "Táo,10\n"
                # a. Xóa khoảng trắng và ký tự xuống dòng thừa: "Táo,10"
                clean_line = line.strip()

                # b. Tách chuỗi thành một list gồm 2 phần tại dấu phẩy: ["Táo", "10"]
                parts = clean_line.split(',')

                # c. Kiểm tra xem dòng có đúng định dạng không (phải có 2 phần)
                if len(parts) == 2:
                    item = parts[0]
                    quantity_str = parts[1]

                    # d. Thêm vào dictionary, nhớ chuyển đổi số lượng từ chuỗi về số nguyên!
                    cart[item] = int(quantity_str)

    except FileNotFoundError:
        # 5. Nếu file không tồn tại (chạy lần đầu), báo cho người dùng và trả về giỏ rỗng.
        print("Không tìm thấy file giỏ hàng cũ. Bắt đầu với giỏ hàng mới.")
        return {}  # Trả về dictionary rỗng

    print("Tải giỏ hàng thành công!")
    return cart  # 6. Trả về dictionary đã được tái tạo.

# --- PHẦN CODE CHÍNH CỦA CHƯƠNG TRÌNH ---


# Đặt tên file vào một biến để dễ quản lý
CART_FILENAME = "cart.txt"

# 1. Bắt đầu bằng việc tải giỏ hàng từ file
shopping_cart = load_cart_from_file(CART_FILENAME)

# 2. Hiển thị cho người dùng giỏ hàng cũ (nếu có)
print("\n--- Giỏ hàng hiện tại của bạn ---")
if not shopping_cart:  # Kiểm tra xem giỏ hàng có rỗng không
    print("Giỏ hàng của bạn đang trống.")
else:
    for item, quantity in shopping_cart.items():
        print(f"- {item}: {quantity}")

# 3. Thực hiện một vài thay đổi (ví dụ)
print("\n--- Cập nhật giỏ hàng ---")
print("Thêm 3 quả Chuối...")
shopping_cart["Chuối"] = 3

print("Cập nhật Táo lên 15 quả...")
shopping_cart["Táo"] = 15

# 4. Lưu lại những thay đổi vào file trước khi kết thúc
save_cart_to_file(shopping_cart, CART_FILENAME)
