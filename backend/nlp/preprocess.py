import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
import nltk

# Download only required resources
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
tokenizer = TreebankWordTokenizer()   # <-- IMPORTANT

def preprocess_text(text):
    """
    NLP preprocessing using:
    - Lowercasing
    - Tokenization (Treebank tokenizer)
    - Stopword removal
    - Lemmatization
    """

    text = text.lower()

    # SAFE tokenization (does NOT use punkt)
    tokens = tokenizer.tokenize(text)

    cleaned_tokens = []
    for word in tokens:
        if word not in stop_words and word not in string.punctuation:
            cleaned_tokens.append(lemmatizer.lemmatize(word))

    return " ".join(cleaned_tokens)


# Test locally
if __name__ == "__main__":
    print(preprocess_text("I am feeling very stressed and anxious today!"))
