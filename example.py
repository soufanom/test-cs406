import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("hello")
exit(1)


mpg = pd.read_csv("datasets/mpg.csv")

plt.figure(figsize=(12, 6))

print(mpg['class'])
unique_valus, encoded_labels = np.unique(mpg['class'], return_inverse=True)
print(encoded_labels)

