import os

# Hàm đếm số lần xuất hiện của từng ký tự
def dem_so_lan_xuat_hien(s):
    dem = {}
    for char in s:
        dem[char] = s.count(char)
    return dict(sorted(dem.items()))

# Hàm đổi chữ hoa thành chữ thường và ngược lại
def doi_chu_hoa(s):
    ket_qua = ""
    for char in s:
        if char.islower():
            ket_qua += char.upper()
        elif char.isupper():
            ket_qua += char.lower()
        else:
            ket_qua += char
    return ket_qua

# Hàm viết hoa chữ cái đầu tiên trong mỗi từ
def viet_hoa_chu_dau(s):
    cac_tu = s.split()
    tu_viet_hoa = [tu[0].upper() + tu[1:].lower() for tu in cac_tu]
    return ' '.join(tu_viet_hoa)

# Hàm loại bỏ ký tự đặc biệt từ chuỗi
def loai_bo_ky_tu_dac_biet(chuoi):
    ky_tu_dac_biet = "!@#$%^&*()_+[]{}|;:,.<>?/'\"\\"
    chuoi_moi = ''
    for char in chuoi:
        if char not in ky_tu_dac_biet:
            chuoi_moi += char
    return chuoi_moi

# Hàm thay thế ký tự theo độ dài của từ
def thay_the_ky_tu():
    tu_nhap = input("Nhập từ cần thay thế: ")
    ket_qua = ''.join('#' if len(tu_nhap) >= 4 else char for char in tu_nhap)
    print(f"Chuỗi sau khi thay thế: {ket_qua}")

# Hàm loại bỏ ký tự lặp lại liên tiếp
def loai_bo_ky_tu_lap():
    s = input("Nhập chuỗi: ")
    ket_qua = ""
    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1]:
            ket_qua += s[i]
    return ket_qua

# Hàm thêm dấu gạch chéo ở cả hai bên mỗi ký tự không phải là nguyên âm
def them_dau_gach(s):
    nguyen_am = 'aeiouAEIOU'
    ket_qua = ""
    for char in s:
        if char not in nguyen_am:
            ket_qua += '-' + char + '-'
        else:
            ket_qua += char
    return ket_qua

# Hàm trích xuất tên từ địa chỉ email
def trich_xuat_ten(email):
    ten = ""
    for char in email:
        if char == '@':
            break
        ten += char
    return ten

# Hàm đếm số lần xuất hiện của ba ký tự giống nhau tại cùng một chỉ mục
def dem_ba_ky_tu_giong_nhau(s):
    dem = 0
    for i in range(len(s) - 2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            dem += 1
    return dem

# Hàm tính độ giống nhau giữa hai chuỗi
def tinh_do_giong_nhau(chuoi1, chuoi2):
    if chuoi1 == chuoi2:
        return 1.0
    else:
        giao = len(set(chuoi1).intersection(set(chuoi2)))
        hop = len(set(chuoi1).union(set(chuoi2)))
        do_giong_nhau = giao / hop
        return do_giong_nhau

# Hàm hiển thị menu
def menu():
    print("[a] Đếm số lần xuất hiện của từng ký tự")
    print("[b] Đổi chữ hoa thành chữ thường và ngược lại")
    print("[c] Viết hoa chữ cái đầu tiên trong mỗi từ")
    print("[d] Loại bỏ ký tự đặc biệt từ chuỗi")
    print("[e] Thay thế ký tự theo độ dài của từ")
    print("[f] Loại bỏ ký tự lặp lại liên tiếp")
    print("[g] Thêm dấu gạch chéo ở cả hai bên ký tự không phải là nguyên âm")
    print("[h] Trích xuất tên từ địa chỉ email")
    print("[i] Đếm số lần xuất hiện của ba ký tự giống nhau")
    print("[j] Tính độ giống nhau giữa hai chuỗi")
    print("[E] Thoát")

# Vòng lặp để hiển thị menu và xử lý lựa chọn của người dùng
while True:
    os.system('cls')
    menu()
    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == 'a':
        chuoi = input("Nhập chuỗi: ")
        ket_qua = dem_so_lan_xuat_hien(chuoi)
        print(ket_qua)
    elif lua_chon == 'b':
        chuoi = input("Nhập chuỗi: ")
        ket_qua = doi_chu_hoa(chuoi)
        print(ket_qua)
    elif lua_chon == 'c':
        chuoi = input("Nhập chuỗi: ")
        ket_qua = viet_hoa_chu_dau(chuoi)
        print(ket_qua)
    elif lua_chon == 'd':
        chuoi = input("Nhập chuỗi: ")
        ket_qua = loai_bo_ky_tu_dac_biet(chuoi)
        print(f"Chuỗi sau khi loại bỏ ký tự đặc biệt: {ket_qua}")
    elif lua_chon == 'e':
        thay_the_ky_tu()
    elif lua_chon == 'f':
        ket_qua = loai_bo_ky_tu_lap()
        print(ket_qua)
    elif lua_chon == 'g':
        chuoi = input("Nhập chuỗi: ")
        ket_qua = them_dau_gach(chuoi)
        print(ket_qua)
    elif lua_chon == 'h':
        email = input("Nhập địa chỉ email: ")
        ket_qua = trich_xuat_ten(email)
        print(ket_qua)
    elif lua_chon == 'i':
        chuoi = input("Nhập chuỗi: ")
        ket_qua = dem_ba_ky_tu_giong_nhau(chuoi)
        print(ket_qua)
    elif lua_chon == 'j':
        chuoi1 = input("Nhập chuỗi thứ nhất: ")
        chuoi2 = input("Nhập chuỗi thứ hai: ")
        ket_qua = tinh_do_giong_nhau(chuoi1, chuoi2)
        print(ket_qua)
    elif lua_chon == 'E':
        break
    else:
        print("Lựa chọn không hợp lệ")

    input("Nhấn phím bất kỳ để tiếp tục...")
