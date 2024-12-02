# visualization
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# 假设X1和X2是你从TF-IDF中获得的两个数据集
# 这里我们假设已经读取了TF-IDF生成的CSV文件，包含代词数据
X1 = pd.read_csv(r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tfidf\longer_tfidf_ENG\longer_token_ENG_pronoun_scores.csv")
X2 = pd.read_csv(r"D:\LIS 501 Intro to text mining\Japanese spoken corpora\NICT_JLE_4.1\NICT_JLE_4.1\tfidf\longer_tfidf_ENG\longer_token_ENG_pronoun_scores.csv")

# 添加标签：0表示英语说话者，1表示日语说话者
X1['label'] = 0  # 标签：英语说话者
X2['label'] = 1  # 标签：日语说话者

# 去除0
X1 = X1.loc[~(X1 == 0).all(axis=1)]
X2 = X2.loc[~(X2 == 0).all(axis=1)]

# 合并数据集
X = pd.concat([X1, X2], axis=0)

# 提取特征（去除标签列）
X_features = X.drop('label', axis=1)

# 聚类：使用K-means进行聚类
kmeans = KMeans(n_clusters=5, random_state=42)  # 聚成3类 Personal Processive Demostrative
kmeans.fit(X_features)
cluster_labels = kmeans.labels_

# 降维：使用PCA和t-SNE
pca = PCA(n_components=3)  # 首先使用PCA降维到50维
pca_result = pca.fit_transform(X_features)

# 使用t-SNE进一步降维到2维
#tsne = TSNE(n_components=2, random_state=42)
#tsne_result = tsne.fit_transform(pca_result)

# 可视化
plt.figure(figsize=(10, 8))
plt.scatter(pca_result[:, 0], pca_result[:, 1], c=cluster_labels, cmap='viridis', s=100, marker='o')

# 如果有代词的标签（比如代词列表），可以加上注释
pronouns = ['he', 'her', 'his', 'she', 'our', 'it', 'my', 'their', 'that', 'you', 'we', 'they', 'your']  # 代词示例
for i, txt in enumerate(pronouns):
    plt.annotate(txt, (pca_result[i, 0], pca_result[i, 1]), fontsize=12)

plt.title('Pronoun Clustering and Dimensionality Reduction')
plt.xlabel('PCA Dimension 1')
plt.ylabel('PCA Dimension 2')
plt.colorbar(label='Cluster')
plt.show()