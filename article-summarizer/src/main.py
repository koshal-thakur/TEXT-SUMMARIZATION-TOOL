# filepath: article-summarizer/article-summarizer/src/main.py

from transformers import pipeline

def summarize_article(text, max_length=130, min_length=30):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

def main():
    print("Welcome to the Article Summarizer!")
    article = input("Please enter the article text you want to summarize:\n")
    
    summary = summarize_article(article)
    
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()