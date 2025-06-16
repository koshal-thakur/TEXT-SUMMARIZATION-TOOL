def clean_text(text):
    """Cleans the input text by removing unwanted characters and extra spaces."""
    import re
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.strip()  # Remove leading and trailing spaces
    return text

def tokenize_text(text):
    """Tokenizes the input text into sentences and words."""
    import nltk
    nltk.download('punkt')
    from nltk.tokenize import sent_tokenize, word_tokenize
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    return sentences, words

def extract_keywords(text, num_keywords=5):
    """Extracts keywords from the input text using simple frequency analysis."""
    from collections import Counter
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    
    words = [word for word in text.split() if word.lower() not in stop_words]
    word_freq = Counter(words)
    keywords = word_freq.most_common(num_keywords)
    return [keyword for keyword, freq in keywords]