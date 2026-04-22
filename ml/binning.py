import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# ------------------------------------------------------------
# 1. SAMPLE REAL-WORLD JSON DATASET (house prices in USD)
# ------------------------------------------------------------
houses = [
    {"house_id": 1, "price": 125},
    {"house_id": 2, "price": 184},
    {"house_id": 3, "price": 95},
    {"house_id": 4, "price": 310},
    {"house_id": 5, "price": 278},
    {"house_id": 6, "price": 145},
    {"house_id": 7, "price": 430},
    {"house_id": 8, "price": 89},
    {"house_id": 9, "price": 205},
    {"house_id": 10, "price": 167},
    {"house_id": 11, "price": 540},
    {"house_id": 12, "price": 62},
    {"house_id": 13, "price": 312},
    {"house_id": 14, "price": 198},
    {"house_id": 15, "price": 275},
    {"house_id": 16, "price": 188},
    {"house_id": 17, "price": 410},
    {"house_id": 18, "price": 134},
    {"house_id": 19, "price": 229},
    {"house_id": 20, "price": 98}
]

prices = np.array([h['price'] for h in houses])
num_bins = 4

# ------------------------------------------------------------
# 2. APPLY BINNING METHODS
# ------------------------------------------------------------
# Equal Width
width_bins, width_edges = pd.cut(prices, bins=num_bins, include_lowest=True, retbins=True)
print("width_edges :: ", width_edges)

# Equal Frequency
freq_bins, freq_edges = pd.qcut(prices, q=num_bins, retbins=True, duplicates='drop')
print("freq_bins :: ", freq_bins)
print("freq_edges :: ", freq_edges)



# K-means Binning
prices_reshaped = prices.reshape(-1, 1)
kmeans = KMeans(n_clusters=num_bins, random_state=42, n_init=10)
kmeans.fit(prices_reshaped)
centers = kmeans.cluster_centers_.flatten()
sorted_centers = np.sort(centers)
boundaries = (sorted_centers[:-1] + sorted_centers[1:]) / 2
kmeans_edges = np.concatenate(([-np.inf], boundaries, [np.inf]))
# Map labels to sorted bin order
center_order = np.argsort(centers)
label_to_bin = {orig: new for new, orig in enumerate(center_order)}
kmeans_bins = [label_to_bin[l] for l in kmeans.labels_]
#
# # ------------------------------------------------------------
# # 3. PLOT COMPARISON
# # ------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
sns.set_style("whitegrid")

# ---- Original distribution ----
ax = axes[0, 0]
sns.histplot(prices, kde=True, bins=12, color='gray', ax=ax)
ax.axvline(prices.mean(), color='red', linestyle='--', label=f'Mean = ${prices.mean():,.0f}')
ax.set_title('Original Price Distribution', fontsize=12)
ax.set_xlabel('Price ($)')
ax.set_ylabel('Frequency')
ax.legend()

# ---- Equal Width ----
ax = axes[0, 1]
# Show histogram with bin edges from equal-wiy
# dth
ax.hist(prices, bins=width_edges, edgecolor='black', alpha=0.7, color='steelblue')
# Mark bin boundaries
for edge in width_edges:
    ax.axvline(edge, color='red', linestyle='--', linewidth=1)
ax.set_title(f'Equal-Width Binning ({num_bins} bins)', fontsize=12)
ax.set_xlabel('Price ($)')
ax.set_ylabel('Frequency')
# Add count per bin as text
counts, _ = np.histogram(prices, bins=width_edges)
for i, (left, right) in enumerate(zip(width_edges[:-1], width_edges[1:])):
    ax.text((left+right)/2, max(counts)*0.9, f'n={counts[i]}', ha='center', fontsize=9)

# ---- Equal Frequency ----
ax = axes[1, 0]
# To show equal-frequency bin boundaries on the original distribution, we reuse the freq_edges
ax.hist(prices, bins=20, alpha=0.5, color='lightgreen', edgecolor='black', label='Original')
for edge in freq_edges:
    ax.axvline(edge, color='red', linestyle='--', linewidth=1.5)
ax.set_title(f'Equal-Frequency Binning ({len(freq_edges)-1} bins)', fontsize=12)
ax.set_xlabel('Price ($)')
ax.set_ylabel('Frequency')
# Show that each bin has same count
counts_freq, _ = np.histogram(prices, bins=freq_edges)
for i, (left, right) in enumerate(zip(freq_edges[:-1], freq_edges[1:])):
    ax.text((left+right)/2, max(counts_freq)*0.9, f'n={counts_freq[i]}', ha='center', fontsize=9)

# ---- K-Means Binning ----
ax = axes[1, 1]
ax.hist(prices, bins=20, alpha=0.5, color='salmon', edgecolor='black', label='Original')
# Plot cluster centers as vertical lines
for center in sorted_centers:
    ax.axvline(center, color='blue', linestyle='-', linewidth=2, label='Cluster center' if center == sorted_centers[0] else "")
# Plot boundaries (midpoints)
for bound in boundaries:
    ax.axvline(bound, color='red', linestyle='--', linewidth=1.5, label='Bin boundary' if bound == boundaries[0] else "")
ax.set_title(f'K-Means Binning ({num_bins} clusters)', fontsize=12)
ax.set_xlabel('Price ($)')
ax.set_ylabel('Frequency')
# Add counts per bin (using mapped bins)
counts_kmeans = [np.sum(np.array(kmeans_bins) == i) for i in range(num_bins)]
# Get bin intervals from edges
kmeans_intervals = list(zip([-np.inf] + list(boundaries), list(boundaries) + [np.inf]))
for i, (left, right) in enumerate(kmeans_intervals):
    center_x = sorted_centers[i]  # use cluster center as label position
    ax.text(center_x, max(counts_kmeans)*0.9, f'n={counts_kmeans[i]}', ha='center', fontsize=9, color='darkred')
ax.legend()

plt.tight_layout()
plt.show()