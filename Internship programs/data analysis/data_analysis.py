import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv("spam.csv", encoding='latin-1')
df = df[['v1','v2']]
df.columns = ['label','message']
print(df.head())

print("\nDataset Information: ")
print(df.info())

print("\nStatistical summary: ")
print(df.describe(include='all'))

df['message_len'] = df['message'].apply(len)
average_length = df['message_len'].mean()

print("\nAvg length of the message: ",average_length)


label_counts = df['label'].value_counts()

plt.bar(label_counts.index, label_counts.values)
plt.xlabel("Message type")
plt.ylabel("Count")
plt.title("Bar graph comparision of spam and ham messages")
plt.show()

df['label_num'] = df['label'].map({'ham':0, 'spam': 1})

plt.scatter(df['message_len'], df['label_num'])
plt.xlabel("message length")
plt.ylabel("Message type (0 = Ham, 1 = Spam)")
plt.title("Scatter point representation")
plt.show()

correlation = df[['message_len', 'label_num']].corr()

plt.figure(figsize=(6,4))
plt.imshow(correlation, cmap='inferno', interpolation='kaiser')
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("correlation heatmap")
plt.tight_layout()
plt.show()



    
