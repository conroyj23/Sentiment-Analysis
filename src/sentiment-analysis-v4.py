import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from spellchecker import SpellChecker

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

spell = SpellChecker()

def text_process(message):
    nopunc = [char for char in message if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    
def spell_check(message):
    formatted_sentence = []
    for i in message:
        corrected_word = spell.correction(i) # if "Thsi" is passed to correction it should return "This" 
        formatted_sentence.append(corrected_word.lower())
    return formatted_sentence
    
df['content'] = df['content'].apply(text_process)
df['content'] = df['content'].apply(spell_check)

#bow = bag of words
#count the frequency of each unique word occuring and create vectors based 
#off of those values
bow_transformer = CountVectorizer(analyzer=text_process).fit(df['content'])

messages_bow = bow_transformer.transform(df['content'])

#term frequency, inverse document frequency
tfidf_transformer = TfidfTransformer().fit(messages_bow)
messages_tfidf = tfidf_transformer.transform(messages_bow)

sentiment_model = MultinomialNB().fit(messages_tfidf,df['sentiment'])

predictions = sentiment_model.predict(messages_tfidf)

msg_train,msg_test,sentiment_train,sentiment_test = train_test_split(df['content'],df['sentiment'],test_size=0.3)

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(msg_train, sentiment_train)
predictions = pipeline.predict(msg_test)

print(classification_report(sentiment_test,predictions))