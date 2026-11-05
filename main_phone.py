import os
import urllib.request
import re
import customtkinter as ctk
from tkinter import messagebox

class AppCameraDienThoai(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CAMERA AI - ĐIỆN THOẠI")
        self.geometry("400x650")

        # Đuôi IP máy tính của bạn (Ứng dụng tự ghép dải mạng local)
        self.IP_MAY_TINH = "192.168.1.158"  # Thay bằng IP máy tính của bạn
        self.PORT = "8000"

        self.custom_modules = []
        self.setup_ui()

    def setup_ui(self):
        self.lbl_camera = ctk.CTkLabel(self, text="Đang mở Camera...", height=320)
        self.lbl_camera.pack(fill="x", padx=10, pady=10)

        # Nút bấm cập nhật 1-Chạm
        btn_update = ctk.CTkButton(
            self,
            text="⚡ CẬP NHẬT TÍNH NĂNG MỚI",
            command=self.tu_dong_cap_nhat,
            fg_color="#2FA572",
            hover_color="#1E6B49",
            height=45,
            font=ctk.CTkFont(size=15, weight="bold")
        )
        btn_update.pack(pady=15, fill="x", padx=20)

        # Khung chứa các công tắc tự sinh
        self.scroll_switches = ctk.CTkScrollableFrame(
            self, height=200, label_text="TÍNH NĂNG ĐÃ NẠP"
        )
        self.scroll_switches.pack(fill="x", padx=10, pady=10)

    def tu_dong_cap_nhat(self):
        """Tự động quét thư mục máy tính, tải tất cả tệp .py mới và sinh công tắc"""
        url = f"http://{self.IP_MAY_TINH}:{self.PORT}/"
        try:
            # 1. Đọc danh sách tệp từ thư mục máy tính
            with urllib.request.urlopen(url, timeout=3) as response:
                html = response.read().decode('utf-8')

            # 2. Tìm tất cả tệp có đuôi .py trong thư mục
            files = re.findall(r'href="([^"]+\.py)"', html)

            if not files:
                messagebox.showinfo("Thông báo", "Chưa có tệp .py nào trong thư mục máy tính!")
                return

            dem_moi = 0
            for file_name in files:
                # Bỏ qua tệp đã nạp rồi
                if any(mod["name"] == file_name for mod in self.custom_modules):
                    continue

                # 3. Tải tệp .py về điện thoại
                file_url = url + file_name
                urllib.request.urlretrieve(file_url, file_name)

                # 4. Tự động tạo công tắc riêng mang tên tệp
                switch_var = ctk.BooleanVar(value=True)
                new_switch = ctk.CTkSwitch(
                    self.scroll_switches,
                    text=file_name,
                    variable=switch_var
                )
                new_switch.pack(pady=5, anchor="w", padx=10)

                self.custom_modules.append({"name": file_name, "var": switch_var})
                dem_moi += 1

            if dem_moi > 0:
                messagebox.showinfo("Thành công", f"Đã cập nhật tự động {dem_moi} tính năng mới!")
            else:
                messagebox.showinfo("Thông báo", "Tất cả tính năng đã được cập nhật trước đó.")

        except Exception as e:
            messagebox.showerror("Lỗi kết nối", "Không thể kết nối tới máy tính!\nHãy chắc chắn 2 máy chung Wifi.")

if __name__ == "__main__":
    app = AppCameraDienThoai()
    app.mainloop()