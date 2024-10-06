# Pre-Election News Coverage

The Pre-Election News Coverage project is designed to analyze and summarize news coverage related to pre-election events. It includes components for fetching news articles, processing the content, and generating summaries based on sentiment analysis and readability metrics across multiple election years.


# File Descriptions

### main.py
The main entry point for the project, responsible for orchestrating the overall flow of the analysis. It handles data processing, analysis, visualization, summarization, sentiment analysis, and readability analysis for multiple election years.

### data_processing.py
A module that provides functions for retrieving and tokenizing news articles from various sources. It generates lists of article file paths based on specified folders and news sources.

### analysis.py
This module performs comprehensive analysis on the text data for specific election years. It includes functions for calculating TF-IDF scores, analyzing topics, and counting candidate-specific words.

### visualization.py
A module that creates and saves visualizations for the analysis results. It includes functions for plotting candidate scores, year comparisons, and averages of election parameters.

### summarization.py
This module generates summaries for all articles in specific election years. It saves the summaries to text files for further review and analysis.

### sentiment_analysis.py
A module that performs sentiment analysis on the articles. It calculates sentiment polarity scores and generates plots for visual representation of sentiment trends.

### readability_analysis.py
This module analyzes the readability of the articles using various metrics. It generates plots to compare readability scores across different election years.

### constants.py
A module that defines constants used throughout the project, including folder names, candidate names, seat counts, and topic-related words.


# Usage

Run the main script:

```sh
python main.py
```

### Output

The program will generate various output files, including:

- Plots for candidate scores, sentiment scores, and readability metrics.
- Summaries of articles for each election year saved in the `results` directory.


# Design

The project is structured to separate concerns, with distinct modules handling specific tasks such as data processing, analysis, visualization, and summarization. This modular approach enhances maintainability and scalability.


# Implementation details

The project utilizes data structures such as lists and dictionaries to manage articles and their associated metadata. It employs libraries like NLTK for text processing, TextBlob for sentiment analysis, and Matplotlib for visualization.


# Error Handling

Error handling is implemented using try-except blocks to gracefully manage exceptions during file operations and data processing. Meaningful error messages are logged to assist in debugging.


# Object Oriented Design

The design emphasizes encapsulation and modularity, allowing for easy extension and modification of features. Each module is responsible for a specific aspect of the analysis, promoting clarity and organization within the codebase.

