import networkx as nx
import numpy as np
import scipy.sparse.linalg

def spectral_clustering(G):
    """
    Thực hiện thuật toán Phân cụm Phổ (Spectral Clustering) trên đồ thị 
    bằng phương pháp quét cắt (sweep-cut).
    
    Input:
        G (nx.Graph): Đồ thị networkx cần phân cụm.
    Output:
        tuple: (Danh_sách_node_Cụm_1, Danh_sách_node_Cụm_2, tỷ_lệ_cắt_tốt_nhất)
    """
    # Bước 1: Tạo ma trận Laplace 
    L = nx.laplacian_matrix(G).astype(float)
    
    # Bước 2: Tìm Trị riêng (Eigenvalues) và Vector riêng (Eigenvectors)
    eigenvalues, eigenvectors = scipy.sparse.linalg.eigs(L, k=3, which='SM')
    
    # Lấy vector riêng thứ 2 và ép kiểu về số thực
    v2 = np.real(eigenvectors[:, 1]) 
    
    # Bước 3: Sắp xếp các node dựa vào điểm số từ vector riêng
    # Tạo một danh sách các tuple: (id_của_node, điểm_vector_riêng)
    node_scores = [(node, v2[i]) for i, node in enumerate(G.nodes())]
    
    # Sắp xếp danh sách theo điểm số (phần tử thứ 2 trong tuple, từ bé đến lớn)
    sorted_nodes = [node for node, score in sorted(node_scores, key=lambda x: x[1])]
    
    # Bước 4: Quét cắt
    best_cut_ratio = float('inf')
    best_cluster_1 = []
    best_cluster_2 = []
    
    total_nodes = len(sorted_nodes)
    
    for i in range(1, total_nodes):
        S1 = sorted_nodes[:i]        # Phía bên trái đường cắt
        S2 = sorted_nodes[i:]        # Phía bên phải đường cắt
        
        # Tính số lượng cạnh bị đứt giữa S1 và S2
        cut_size = nx.cut_size(G, S1, S2)
        
        # Tính tỷ lệ cắt (Cut Ratio): cut_size / (|S1| * |S2|)
        cut_ratio = cut_size / (len(S1) * len(S2))
        
        # Lưu lại cách cắt tốt nhất
        if cut_ratio < best_cut_ratio:
            best_cut_ratio = cut_ratio
            best_cluster_1 = S1
            best_cluster_2 = S2
            
    return best_cluster_1, best_cluster_2, best_cut_ratio