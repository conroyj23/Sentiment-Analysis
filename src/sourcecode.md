# CPS 491 - Capstone II

## 
```python
#from afinn import Afinn
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

df = pd.read_excel("NRC-Emotion-Lexicon-CPS-2.xlsx")

samp = "Are you in the office? Kindly let me know because i need you to do something very important for me."

def text_process(message):
    nopunc = [char for char in message if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    
def getScore(mess):
    res = [0,0,0,0,0,0,0,0,0,0,0]
    for y in mess:
        #print(y)
        for x in range(df['English'].size-1):
            #print(x)
            if y == df['English'][x]:
                res[0] = res[0] + df['Positive'][x]
                res[1] = res[1] + df['Negative'][x]
                res[2] = res[2] + df['Anger'][x]
                res[3] = res[3] + df['Anticipation'][x]
                res[4] = res[4] + df['Disgust'][x]
                res[5] = res[5] + df['Fear'][x]
                res[6] = res[6] + df['Joy'][x]
                res[7] = res[7] + df['Sadness'][x]
                res[8] = res[8] + df['Surprise'][x]
                res[9] = res[9] + df['Trust'][x]
                res[10] = res[10] + df['Phishing'][x]
    return res
    
def outputNicely(scores):
    emotionArray = ["Positive", "Negative", "Anger", "Anticipation", "Disgust", "Fear", "Joy", "Sadness", "Surprise", "Trust", "Phishing"]
    z=0
    for y in emotionArray:
        print(y + ": " + str(scores[z]) + " occurence(s)")
        z+=1
        
samp_tp = text_process(samp)
samp_scores = getScore(samp_tp)
outputNicely(samp_scores)
        

```
