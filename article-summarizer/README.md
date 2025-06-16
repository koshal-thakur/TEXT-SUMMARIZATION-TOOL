# Article Summarizer

This project is a tool for summarizing lengthy articles using natural language processing techniques. It leverages various NLP libraries to preprocess text, summarize content, and evaluate the quality of the summaries.

## Project Structure

```
article-summarizer
├── src
│   ├── main.py               # Entry point of the application
│   ├── summarizer            # Contains the summarization logic
│   │   ├── __init__.py       # Package initialization
│   │   └── summarizer.py     # Summarizer class implementation
│   ├── utils                 # Utility functions for text processing
│   │   └── text_utils.py     # Text processing utilities
│   └── types                 # Type definitions and interfaces
│       └── __init__.py       # Package initialization
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd article-summarizer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the summarization tool, execute the following command:

```
python src/main.py
```

Follow the prompts to input the article you wish to summarize.

## Features

- Summarization of lengthy articles
- Text preprocessing
- Evaluation of summary quality

## Dependencies

This project requires the following Python packages:

- nltk
- spacy
- transformers

Make sure to install these packages using the `requirements.txt` file provided.