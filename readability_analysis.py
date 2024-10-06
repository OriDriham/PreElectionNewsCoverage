import os
import numpy as np
import textstat
import matplotlib.pyplot as plt
from constants import save_path


def analyze_readability(text):
    """
    Analyze the readability of the given text using multiple metrics.

    :param text: The text to analyze.
    :return: dict: A dictionary containing various readability scores.
    """
    return {
        "Flesch Reading Ease": textstat.flesch_reading_ease(text),
        "Flesch-Kincaid Grade": textstat.flesch_kincaid_grade(text),
        "SMOG Index": textstat.smog_index(text)
    }


def analyze_year_folder(year):
    """
    Analyze the readability of all articles in a specific election year folder.

    :param year: The election year to analyze.
    :return: dict: A dictionary containing average readability scores for the
    year.
    """
    readability_scores = []
    for filename in os.listdir(f'elections{year}'):
        if filename.endswith(".txt"):
            with open(os.path.join(f'elections{year}', filename), 'r',
                      encoding='utf-8') as file:
                text = file.read()
                scores = analyze_readability(text)
                readability_scores.append(scores)

    if readability_scores:
        avg_scores = {metric: np.mean([score[metric]
                                       for score in readability_scores])
                      for metric in readability_scores[0]}
    else:
        avg_scores = {metric: 0 for metric in [
            "Flesch Reading Ease", "Flesch-Kincaid Grade", "SMOG Index"]}

    return avg_scores


def analyze_readability_across_years(years):
    """
    Analyze readability across multiple election years.

    :param years: List of election years to analyze.
    :return: dict: A dictionary mapping years to their average readability
    scores.
    """
    return {year: analyze_year_folder(year) for year in years}


def plot_readability_results(readability_results):
    """
    Create and save plots of readability results across multiple years.

    :param readability_results: Dictionary containing readability results for
    each year.
    """
    metrics = list(readability_results[next(iter(readability_results))].keys())
    x = list(readability_results.keys())

    for metric in metrics:
        y = [readability_results[year][metric] for year in x]
        plt.figure(figsize=(10, 6))
        plt.bar(x, y)
        plt.xlabel('Years')
        plt.ylabel(metric)
        plt.title(f'Average {metric} Across Election Years')
        plt.tight_layout()
        plt.savefig(save_path +
                    f'{metric.lower().replace(" ", "_")}_comparison.png')
