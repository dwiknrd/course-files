import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
from sklearn.preprocessing import LabelEncoder  
  
from kmodes.kmodes import KModes  
from kmodes.kprototypes import KPrototypes  
  
import pickle  
from pathlib import Path  
  
# import dataset  
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/customer_segments.txt", sep="\t")  
  
# menampilkan data  
print(df.head())

sns.set(style='white')
plt.clf()

###Standarisasi Kolom Numerik
##Supaya mendapatkan hasil yang maksimal dalam penerapan algoritma ini, 
# kamu perlu menjadikan data-data numerik yang kamu miliki berada pada satu skala. 
# Hal ini dapat di lakukan dengan melakukan standardisasi data yang kamu miliki. 
# Tujuannya adalah agar variabel yang memiliki skala besar tidak mendominasi 
# bagaimana cluster akan di bentuk dan juga tiap variabel akan di anggap sama pentingnya oleh algoritma yang akan di gunakan.

