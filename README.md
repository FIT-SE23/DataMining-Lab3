# Khai thác dữ liệu và ứng dụng  
## Đồ Án 3: Phân cụm và ứng dụng
### **Bài báo được chọn:** [Local Differential Privacy-Preserving Spectral Clustering for General Graphs](https://arxiv.org/pdf/2309.06867)

### Danh sách thành viên
| STT | MSSV | Họ và tên |
|---|---|---|
| 1 | 23127157 | Nguyễn Hoàng Gia Bảo |
| 2 | 23127236 | Lê Hồng Ngọc |
| 3 | 23127247 | Châu Đình Phúc |
| 4 | 23127305 | Nguyễn Hiệp Thắng |

## 1. Cấu trúc thư mục
```text
├── data/                 # Chứa các bộ dữ liệu SNAP
│   ├── 0.edges
│   ├── 1684.edges
│   ├── 414.edges
│   ├── twitter_medium.edges
│   └── twitter_small.edges
├── notebooks/            # Chứa các file jupyter notebook cho việc thực nghiệm
│   ├── 01_main_experiments.ipynb 
│   ├── 02_ablation_study.ipynb 
│   └── 03_new_dataset_test.ipynb 
├── src/                  # Chứa mã nguồn 1 số hàm dùng cho notebook
│   └── metrics.py
│   └── model.py
│   └── utils.py
├── requirements.txt      # Thông tin các thư viện cần tải cho thực nghiệm
└── README.md
```

## 2. Chạy thực nghiệm

Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```

Sau đó tiến hành chạy các file notebook ở thư mục notebooks/. Một số file sẽ được tạo ra trong quá trình chạy
(chẳng hạn như .svg dùng cho ảnh chất lượng cao ở báo cáo).

- **01_main_experiments.ipynb**: Dùng để chạy lại 1 số thực nghiệm trong bài báo
- **02_ablation_study.ipynb**: Các thực nghiệm phân tích ablation study
- **03_new_dataset_test.ipynb**: Chạy thực nghiệm với bộ dữ liệu twitter
