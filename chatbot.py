import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import streamlit as st

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

with open(r'C:\Users\batta\Desktop\chatbot\text.txt',"r",encoding="utf8") as file:
    data = file.read().replace("\n"," ")
    #print(data)

sentences = sent_tokenize(data)
#print(sentences)

def preprocess(sentence):
    word = word_tokenize(sentence)
    stopword = set(stopwords.words("english"))
    word = [ i for i in word if i not in stopword and i not in string.punctuation]
    limitizer = WordNetLemmatizer()
    word = [ limitizer.lemmatize(i) for i in word ]
    return word

lst = [preprocess(i) for i in sentences]

def get_most_relevant_sentence (query):
    query_list = preprocess(query)
    max_similarity = 0
    relevant_sentence = ""
    for i in lst :
        intersection = set(query_list).intersection(set(i))
        union = set(query_list).union(set(i))
        similarity = len(intersection)/len(union)
        if similarity > max_similarity:
            max_similarity = similarity
            relevant_sentence = sentences[lst.index(i)]

    if not relevant_sentence:
        return "sorry, I didn't find an answer"
    
    return(relevant_sentence)


def chatbot (question):
    response = get_most_relevant_sentence(question)
    return response

def main():
    st.title("chatbot")
    query= st.text_input("Ask a question")
    if st.button ("submit"):
        if not query.strip():
            st.warning("enter a valid question")
        else:
            response = chatbot(query)
            st.success(response)

if __name__ =="__main__":
    main()
    

