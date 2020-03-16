import pandas as pd
import string
import emoji
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import re
from fot import *


print("all modules uceesflly imported")

#convert emoji to words
def convert_emojis(text):
    text = emoji.demojize(text)
    return text

def to_loweR(text):
    return text.lower()



#remove punctuations
PUNCT_TO_REMOVE = string.punctuation
punch = ""
x = 0
for j in PUNCT_TO_REMOVE:
    x = x+1
    if x != 24:
        punch = punch+j 
punch = punch + "%/*-+~$#&^)(" 
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', punch))

#stop words
STOPWORDS = set(stopwords.words('english'))
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

#stemming (walks,walking ==> walk)
stemmer = PorterStemmer()
def stem_words(text):
    return " ".join([stemmer.stem(word) for word in text.split()])

#lemmatizing (because of steming private ==> privat so we retain it back to private)
lemmatizer = WordNetLemmatizer()
wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}
def lemmatize_words(text):
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])

#remove urls
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

# expand chat words
chat_words_map_dict = {}
chat_words_list = []
for line in chat_words_str.split("\n"):
    if line != "":
        cw = line.split("=")[0]
        cw_expanded = line.split("=")[1]
        chat_words_list.append(cw)
        chat_words_map_dict[cw] = cw_expanded
chat_words_list = set(chat_words_list)

def chat_words_conversion(text):
    new_text = []
    for w in text.split():
        if w.upper() in chat_words_list:
            new_text.append(chat_words_map_dict[w.upper()])
        else:
            new_text.append(w)
    return " ".join(new_text)

def preprocess_all(df):
    df["text"] = df["text"].apply(lambda text: convert_emojis(text))
    print("emoji")
    print(df.head())
    df["text"] = df["text"].apply(lambda text: to_loweR(text))
    print("lower")
    print(df.head())
    df["text"] = df["text"].apply(lambda text: remove_punctuation(text))
    print("punct")
    print(df.head())
    df["text"] = df["text"].apply(lambda text: remove_stopwords(text))
    print("stop")
    print(df.head())
    df["text"] = df["text"].apply(lambda text: remove_urls(text))
    print("urls")
    print(df.head())
    df["text"] = df["text"].apply(lambda text: chat_words_conversion(text))

    print("success")
   
    return df
     

'''
df2 = pd.read_csv("tweetproduct1.csv",engine = "python")
df2 = preprocess_all(df2)
print(df2.head())

'''

    
    
