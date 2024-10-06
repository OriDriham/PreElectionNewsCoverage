import matplotlib.pyplot as plt
import numpy as np
from constants import save_path


def plot_candidate_scores(party_scores, year, seat_counts):
    """
    Create and save a bar plot of candidate party scores.

    :param party_scores: Dictionary of party scores.
    :param year: The election year being plotted.
    :param seat_counts: Dictionary mapping parties to their seat counts.
    """
    parties = list(party_scores.keys())
    scores = [float(score) for score in party_scores.values()]
    party_labels = [f"{party} ({seat_counts.get(party, 0)})"
                    for party in parties]

    plt.figure(figsize=(10, 6))
    plt.bar(party_labels, scores, align='center')
    plt.xlabel('Parties')
    plt.ylabel('TF-IDF Score')
    plt.title(f'TF-IDF Scores for Candidate Parties in {year}')
    plt.xticks(rotation=45, ha='right')
    plt.ylim((0, 70))
    plt.tight_layout()
    plt.savefig(save_path + f'party_scores_{year}.png')
    plt.close()


def plot_year_comparison(year_data, features):
    """
    Create and save comparison plots for each feature across different years.

    :param year_data: Dictionary containing data for each year.
    :param features: Set of features to be plotted.
    """
    for feature in features:
        values = [year_data[year].get(feature, np.nan)
                  for year in sorted(year_data.keys())]
        plt.figure(figsize=(10, 6))
        plt.bar(year_data.keys(), values, align='center')
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.title(f'Comparison of {feature} Over Years')
        plt.ylim((0, 50))
        plt.tight_layout()
        plt.savefig(save_path +
                    f'{feature.lower().replace(" ", "_")}_comparison.png')
        plt.close()


def plot_averages(year_data):
    """
    Create and save a plot showing averages and variances of election
    parameters across years.

    :param year_data: Dictionary containing data for each year.
    """
    parameters = list(year_data['year_2019a'].keys())
    averages = []
    variances = []

    for param in parameters:
        param_values = [year_data[year][param] for year in year_data]
        avg = np.mean(param_values)
        var = np.var(param_values)
        averages.append(avg)
        variances.append(var)

    plt.figure(figsize=(12, 6))
    bar_width = 0.35
    index = np.arange(len(parameters))

    plt.bar(index, averages, bar_width, label='Average', color='blue')
    plt.bar(index + bar_width, variances, bar_width, label='Variance',
            color='orange')

    plt.xlabel('Parameters')
    plt.ylabel('Value')
    plt.title('Average and Variance of Election Parameters')
    plt.xticks(index + bar_width / 2, parameters, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path + 'average_variance_election_parameters.png')
