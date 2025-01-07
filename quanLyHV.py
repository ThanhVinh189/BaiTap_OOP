class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = []

    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)

    def hienThiKhoaHoc(self):
        for khoaHoc in self.khoaHoc:
            print(khoaHoc.thongTinKhoaHoc())

class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        return f"Mã khóa học: {self.maKhoaHoc}, Tên khóa học: {self.tenKhoaHoc}, Hình thức: {self.hinhThuc}, Học phí: {self.hocPhi}"

# Tạo đối tượng học viên
hocVien1 = HocVien("HV01", "Nguyễn Văn A", "01/01/2000")
hocVien2 = HocVien("HV02", "Trần Thị B", "02/02/2001")

# Tạo đối tượng khóa học
khoaHoc1 = KhoaHoc("KH01", "Lập trình Python", "Online", 3000000)
khoaHoc2 = KhoaHoc("KH02", "Lập trình Java", "Offline", 3500000)

# Đăng ký khóa học cho học viên
hocVien1.dangKyKhoaHoc(khoaHoc1)
hocVien1.dangKyKhoaHoc(khoaHoc2)
hocVien2.dangKyKhoaHoc(khoaHoc1)

# Hiển thị các khóa học đã đăng ký của học viên
print("Khóa học của học viên 1:")
hocVien1.hienThiKhoaHoc()

print("\nKhóa học của học viên 2:")
hocVien2.hienThiKhoaHoc()
