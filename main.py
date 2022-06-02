from time import time
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


#! Importamos los archivos de clases
from useraccount import UserAccount
from tweet import Tweet
from retweet import Retweet
from directmessage import DirectMessage

#! Respuestas al ejercicio 2.d

#? a) Si, en timeline solamente deberán aparecer los mensajes que no son DirectMessages.
#? Sin embargo, no hay que cambiar la variable tweets, ya que esa seguirá aceptando todos los tweets del propio user, sea un mensaje directo o no

#? b) No, ya que en python, si funciona con la clase madre, también funciona con la clase hija. Es un principio de diseño de la POO.



#! Análisis EDA
#! Ejercicio 1
train = pd.read_csv("train.csv", index_col=0)
test = pd.read_csv("test.csv")
ss = pd.read_csv("sample_submission.csv")

train = train.dropna()

print(train.head())

counted_items = train.groupby("sentiment")["sentiment"].count()
print(counted_items)

#! Para sacar el gráfico:
sns.barplot(x=counted_items.index, y=counted_items.values)
plt.savefig("barplot")


#! Ejercicio 2
text_list = list(train.text)
selected_text_list = list(train.selected_text)

text_words = []
selected_text_words = []

for text in text_list:
    splitted_text = text.strip().split(sep=" ")
    text_words.append(len(splitted_text))

for text in selected_text_list:
    splitted_text = text.strip().split(sep=" ")
    selected_text_words.append(len(splitted_text))

words_difference = []
for a, b in zip(text_words, selected_text_words):
    words_difference.append(a - b)

train["words_difference"] = words_difference



def jaccard(str1, str2):
    a = set(str1.lower().split())
    b = set(str2.lower().split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

jaccard_values = []
for a, b in zip(text_list, selected_text_list):
    jaccard_values.append(jaccard(a, b))

train["jaccard"] = jaccard_values

print(train.head())

sns.kdeplot(x=jaccard_values, shade=True)
plt.savefig("jaccard_distribution")