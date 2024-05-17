import numpy as np
import matplotlib.pyplot as plt

# Define the possible returns and their probabilities
returns = np.array([1.1, 1.2, 0.7, 0.0])
probabilities = np.array([0.6, 0.1, 0.25, 0.05])

# Plotting the returns against their probabilities
plt.figure(figsize=(8, 4))
plt.bar(returns, probabilities, width=0.05, color='green', edgecolor='black')
# plt.title('Probability Distribution of Returns')
plt.xlabel('Returns')
plt.ylabel('Probability')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(returns)
plt.savefig('fig1.png')
# plt.show()