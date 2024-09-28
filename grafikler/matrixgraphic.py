import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.array([
    [1990, 1884, 1720, 1837, 1201, 1636, 1484, 1894],
    [1990, 1902, 1586, 1860, 1139, 1639, 1292, 1864],
    [1994, 1882, 1678, 1829, 1268, 1587, 1427, 1908],
    [1890, 1859, 1421, 1890, 736, 1790, 1245, 1280]
])

distributions = ["Uniform", "Ustel", "Beta", "Normal", "Weibull", "Lognormal", "Geometric", "Poisson"]
activation_functions = ["ReLU", "Sigmoid", "Tanh", "Linear"]

plt.figure(figsize=(10, 6))
sns.heatmap(data, annot=True, fmt='d', cmap='viridis', xticklabels=distributions, yticklabels=activation_functions)
plt.title("Aktivasyon Fonksiyonları vs. Dağılım Türleri")
plt.xlabel("Dağılım Türleri")
plt.ylabel("Aktivasyon Fonksiyonları")
plt.show()
