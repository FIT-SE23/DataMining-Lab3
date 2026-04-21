import networkx as nx
import random
import numpy as np

def get_label_array(G_nodes, cluster_1, cluster_2):
    """
    Chuyển đổi danh sách node của 2 cụm thành mảng nhãn (0 và 1)
    
    Input:
        G_nodes (danh sách): Danh sách tất cả các node trong đồ thị gốc.
        cluster_1, cluster_2 (list): Danh sách các node thuộc cụm 1 và cụm 2.
    Output:
        numpy.array: Mảng chứa nhãn (0 hoặc 1) của từng node.
    """
    labels = np.zeros(len(G_nodes))
    cluster_1_set = set(cluster_1)
    
    for i, node in enumerate(G_nodes):
        if node in cluster_1_set:
            labels[i] = 0
        else:
            labels[i] = 1
    return labels

def load_and_preprocess_graph(filepath):
    """
    Tải đồ thị từ file danh sách cạnh và loại bỏ các node có bậc < 10 
    
    Input:
        filepath (str): Đường dẫn đến file .edges.
    Output:
        nx.Graph: Đồ thị đã được làm sạch.
    """
    G = nx.read_edgelist(filepath)
    
    # Lấy thành phần liên thông lớn nhất
    largest_cc = max(nx.connected_components(G), key=len)
    S = nx.Graph(G.subgraph(largest_cc))
    
    # Loại bỏ các node có bậc < 10 
    while True:
        removed_any = False
        for node in list(S.nodes()):
            if S.degree(node) < 10:
                S.remove_node(node)
                removed_any = True
                break 
        if not removed_any:
            break
            
    # Đánh lại nhãn các node thành số nguyên từ 0 đến N-1
    return nx.convert_node_labels_to_integers(S)


def apply_edge_flipping(G, p, seed=42):
    """
    Áp dụng kỹ thuật Phản hồi ngẫu nhiên (Randomized Response - Edge Flipping) 
    
    Input:
        G (nx.Graph): Đồ thị gốc ban đầu.
        p (float): Xác suất lật cạnh.
        seed (int): random seed để tái hiện lại kết quả.
    Output:
        nx.Graph: Đồ thị đã được thêm nhiễu.
    """
    random.seed(seed)
    noisy_G = nx.Graph()
    noisy_G.add_nodes_from(G.nodes())
    
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            edge_exists = G.has_edge(u, v)
            
            if random.random() < p:
                # Lật: Nếu cạnh đã tồn tại thì xóa đi. Nếu chưa có thì thêm vào.
                if not edge_exists:
                    noisy_G.add_edge(u, v)
            else:
                if edge_exists:
                    noisy_G.add_edge(u, v)
                    
    return noisy_G