import os

# File lưu kết quả
RESULT_FILE = 'selected_numbers.txt'

# Danh sách các số từ 1 đến 15
available_numbers = list(range(1, 16))

# Đọc các tên và số đã được chọn từ file
def load_selected_numbers():
    if os.path.exists(RESULT_FILE):
        with open(RESULT_FILE, 'r') as f:
            data = [line.strip().split() for line in f.readlines()]
            return {name: int(number) for name, number in data}
    return {}

# Lưu số và tên người chọn vào file
def save_selected_number(name, number):
    with open(RESULT_FILE, 'a') as f:
        f.write(f'{name} {number}\n')

# Hàm kiểm tra xem tên đã chọn số trước đó chưa
def has_user_chosen(name, selected_numbers):
    return name in selected_numbers

# Hiển thị danh sách các số còn lại
def display_remaining_numbers(selected_numbers):
    remaining_numbers = [n for n in available_numbers if n not in selected_numbers.values()]
    print("Các số còn lại để chọn: ", remaining_numbers)

# Chương trình chính
def main():
    selected_numbers = load_selected_numbers()

    while True:
        name = input("Nhập tên của bạn (hoặc nhập 'exit' để thoát): ").strip()

        if name.lower() == 'exit':
            print("Kết thúc chương trình.")
            break

        if has_user_chosen(name, selected_numbers):
            print(f"Tên {name} đã chọn số trước đó. Bạn không thể chọn lại.")
            continue

        display_remaining_numbers(selected_numbers)

        try:
            number = int(input("Chọn một số từ 1 đến 15: "))

            if number not in available_numbers:
                print("Số bạn chọn không hợp lệ, vui lòng chọn lại.")
                continue

            if number in selected_numbers.values():
                print("Số này đã có người chọn, vui lòng chọn số khác.")
                continue

            # Lưu số đã chọn và cập nhật danh sách
            save_selected_number(name, number)
            selected_numbers[name] = number
            print(f"{name} đã chọn số {number} thành công!")

        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

if __name__ == '__main__':
    main()
