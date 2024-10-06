import os
from summa import summarizer
from constants import save_path


def summarize_articles(year):
    """
    Generate summaries for all articles in a specific election year.

    :param year: The election year to summarize.
    :return: dict: A dictionary mapping filenames to their summaries.
    """
    summaries = {}
    year_folder = f"elections{year}"
    folder_path = os.path.join(year_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                summary = summarizer.summarize(content, ratio=0.1)
                summaries[filename] = summary

    return summaries


def summarize_by_year(election_year):
    """
    Generate and save summaries for all articles in a specific election year.

    :param election_year: The election year to summarize.
    """
    summaries = summarize_articles(election_year)
    with open(save_path + f'{election_year}_summaries.txt', 'w',
              encoding='utf8') as f:
        for filename, summary in summaries.items():
            f.write(f"\nSummary for {filename}:\n")
            f.write(summary)
            f.write("\n\n")


def summarize_years(years):
    """
    Generate and save summaries for all articles across multiple election
    years.

    :param years: List of election years to summarize.
    """
    for year in years:
        summarize_by_year(year)
