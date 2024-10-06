import os
from textblob import TextBlob
import matplotlib.pyplot as plt
from constants import save_path


def perform_sentiment_analysis(text):
    """
    Perform sentiment analysis on the given text.

    :param text: The text to analyze.
    :return: float: The sentiment polarity score.
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity


def analyze_sentiment_for_folder(year):
    """
    Perform sentiment analysis on all articles in a specific election year
    folder.

    :param year: The election year to analyze.
    :return: dict: A dictionary mapping filenames to their sentiment scores.
    """
    sentiment_scores = {}
    for filename in os.listdir(f'elections{year}'):
        file_path = os.path.join(f'elections{year}', filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        polarity_score = perform_sentiment_analysis(content)
        sentiment_scores[filename] = polarity_score
    return sentiment_scores


def plot_sentiment_scores(sentiment_scores, year):
    """
    Create and save a bar plot of sentiment scores for a specific election
    year.

    :param sentiment_scores: Dictionary mapping filenames to sentiment scores.
    :param year: The election year being plotted.
    """
    files = list(sentiment_scores.keys())
    scores = list(sentiment_scores.values())

    plt.figure(figsize=(10, 6))
    plt.bar(files, scores, color='blue')
    plt.xlabel('Files')
    plt.ylabel('Polarity Score')
    plt.title(f'Sentiment Polarity Scores for {year} Elections')
    plt.xticks(rotation=45, ha='right')
    plt.ylim((-0.2, 0.2))
    plt.tight_layout()
    plt.savefig(save_path + f'sentiment_polarity_{year}.png')


def create_sentiment_plots(years):
    """
    Create and save sentiment plots for multiple election years.

    :param years: List of election years to analyze and plot.
    """
    for year in years:
        sentiment = analyze_sentiment_for_folder(year)
        plot_sentiment_scores(sentiment, year)
