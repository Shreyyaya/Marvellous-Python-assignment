import pandas as pd

df_fake = pd.read_csv("Fake.csv")   
df_true = pd.read_csv("True.csv")   

df_fake['label'] = 0   #labeling 0 to fake
df_true['label'] = 1   #labeling 1 to true


df_combined = pd.concat([df_fake, df_true], ignore_index=True)  #concating the datasets 
#ignore index will reset the index numbers

print(df_combined.head())
print("Fake count:", (df_combined['label'] == 0).sum())  #counting entries of fake articles
print("True count:", (df_combined['label'] == 1).sum())  #counting entries of true articles

df_combined.to_csv("Combined_News.csv", index=False)
#index= false will avoid the extra row number column