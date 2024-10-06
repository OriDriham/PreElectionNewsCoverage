from data_processing import (get_all_elections_list,
                             tokenize_text_from_articles)
from analysis import analyze_election_year
from visualization import plot_year_comparison, plot_averages
from summarization import summarize_years
from sentiment_analysis import create_sentiment_plots
from readability_analysis import (analyze_readability_across_years,
                                  plot_readability_results)
from constants import (
    articles_folders, news_list, candidate_names_2019a, candidate_names_2019b,
    candidate_names_2020, candidate_names_2021, candidate_names_2022,
    seat_count_2019a, seat_count_2019b, seat_count_2020, seat_count_2021,
    seat_count_2022
)


def main():
    """
    The main entry point of the program. Orchestrates the overall flow of the
    analysis, including data processing, analysis, visualization,
    summarization, sentiment analysis, and readability analysis for multiple
    election years.
    """
    (elect_2019a_article, elect_2019b_article, elect_2020_article,
     elect_2021_article, elect_2022_article) = (
        get_all_elections_list(articles_folders, news_list))

    elect_2019a_text = tokenize_text_from_articles(elect_2019a_article)
    elect_2019b_text = tokenize_text_from_articles(elect_2019b_article)
    elect_2020_text = tokenize_text_from_articles(elect_2020_article)
    elect_2021_text = tokenize_text_from_articles(elect_2021_article)
    elect_2022_text = tokenize_text_from_articles(elect_2022_article)

    year_data = {
        'year_2019a': analyze_election_year(
            elect_2019a_text, '2019a', candidate_names_2019a,
            seat_count_2019a),
        'year_2019b': analyze_election_year(
            elect_2019b_text, '2019b', candidate_names_2019b,
            seat_count_2019b),
        'year_2020': analyze_election_year(
            elect_2020_text, '2020', candidate_names_2020,
            seat_count_2020),
        'year_2021': analyze_election_year(
            elect_2021_text, '2021', candidate_names_2021,
            seat_count_2021),
        'year_2022': analyze_election_year(
            elect_2022_text, '2022', candidate_names_2022,
            seat_count_2022)}

    features = set()
    for year in year_data:
        features.update(year_data[year].keys())

    plot_year_comparison(year_data, features)
    plot_averages(year_data)

    years = ['2022', '2021', '2020', '2019b', '2019a']
    summarize_years(years)
    create_sentiment_plots(years)
    plot_readability_results(analyze_readability_across_years(years))


if __name__ == '__main__':
    main()
