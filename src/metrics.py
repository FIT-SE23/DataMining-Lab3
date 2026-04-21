import numpy as np
from sklearn.metrics import normalized_mutual_info_score, adjusted_rand_score
from scipy.optimize import linear_sum_assignment

def symmetric_difference_distance(cluster_clean_1, cluster_clean_2, cluster_noisy_1, cluster_noisy_2):
    """
    Tính toán độ lệch d_size giữa các cụm của đồ thị gốc và đồ thị nhiễu 

    Input:
        cluster_clean_1, cluster_clean_2 (list): Kết quả phân cụm của đồ thị gốc.
        cluster_noisy_1, cluster_noisy_2 (list): Kết quả phân cụm của đồ thị nhiễu.
    Output:
        int: Số lượng node bị xếp sai cụm.
    """

    # Chuyển đổi danh sách (list) thành tập hợp (set)
    T = set(cluster_clean_1)
    T_bar = set(cluster_clean_2)
    P = set(cluster_noisy_1)
    P_bar = set(cluster_noisy_2)
    
    diff_alignment_1 = len(T.symmetric_difference(P)) + len(T_bar.symmetric_difference(P_bar))
    diff_alignment_2 = len(T.symmetric_difference(P_bar)) + len(T_bar.symmetric_difference(P))
    
    return min(diff_alignment_1, diff_alignment_2)

def clustering_accuracy(y_true, y_pred):
    """
    Tính độ chính xác (Accuracy - ACC) bằng thuật toán Hungarian matching.
    """
    y_true = np.array(y_true, dtype=np.int64)
    y_pred = np.array(y_pred, dtype=np.int64)
    
    assert y_pred.size == y_true.size
    
    # Kích thước ma trận bằng số lượng cụm lớn nhất
    D = max(y_pred.max(), y_true.max()) + 1
    w = np.zeros((D, D), dtype=np.int64)
    
    # Tạo ma trận nhầm lẫn
    for i in range(y_pred.size):
        w[y_pred[i], y_true[i]] += 1
        
    # Áp dụng Hungarian matching để tìm cách ghép cặp tốt nhất
    ind_row, ind_col = linear_sum_assignment(w.max() - w)
    
    # Tính tổng số mẫu dự đoán đúng sau khi ghép cặp / tổng số mẫu
    return sum([w[i, j] for i, j in zip(ind_row, ind_col)]) * 1.0 / y_pred.size

def calculate_all_metrics(y_true, y_pred):
    """
    Tính toán cả 3 độ đo bắt buộc trong đồ án.
    
    Output:
        dict: Chứa điểm ACC, NMI và ARI.
    """
    acc = clustering_accuracy(y_true, y_pred)
    nmi = normalized_mutual_info_score(y_true, y_pred)
    ari = adjusted_rand_score(y_true, y_pred)
    
    return {
        "ACC": acc,
        "NMI": nmi,
        "ARI": ari
    }