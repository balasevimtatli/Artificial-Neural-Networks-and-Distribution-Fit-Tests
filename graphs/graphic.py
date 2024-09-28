import numpy as np
import matplotlib.pyplot as plt

distributions = ['Uniform', 'Ustel', 'Beta', 'Normal', 'Weibull', 'Lognormal', 'Geometric', 'Poisson']
relu_values = [2000-10, 2000-116, 2000-280, 2000-163, 2000-799, 2000-364, 2000-516, 2000-106]
sigmoid_values = [2000-10, 2000-98, 2000-414, 2000-140, 2000-861, 2000-361, 2000-708, 2000-136]
tanh_values = [2000-6, 2000-118, 2000-322, 2000-171, 2000-732, 2000-413, 2000-573, 2000-92]
linear_values = [2000-110, 2000-141, 2000-579, 2000-110, 2000-1264, 2000-210, 2000-755, 2000-720]

x = np.arange(len(distributions))

bar_width = 0.2
plt.bar(x - bar_width * 1.5, relu_values, width=bar_width, label='ReLU')
plt.bar(x - bar_width / 2, sigmoid_values, width=bar_width, label='Sigmoid')
plt.bar(x + bar_width / 2, tanh_values, width=bar_width, label='Tanh')
plt.bar(x + bar_width * 1.5, linear_values, width=bar_width, label='Linear')

plt.xlabel('Dağılımlar')
plt.ylabel('Değerler')
plt.title('Aktivasyon Fonksiyonlarına Göre Dağılımlar')
plt.xticks(x, distributions)
plt.legend()
plt.grid(axis='y')

plt.tight_layout()
plt.show()
