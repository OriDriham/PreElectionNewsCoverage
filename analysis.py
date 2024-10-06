from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from constants import (stop_words, save_path, health_words, crime_words,
                       education_words, defense_words, foreign_relations_words,
                       religion_words, US_election_words)
from visualization import plot_candidate_scores


def get_tfidf_score_and_indices(dense_matrix):
    """
    Extract TF-IDF scores and their corresponding indices from a dense matrix.

    :param dense_matrix: Dense matrix of TF-IDF scores.
    :return: tuple: (tfidf_scores, sorted_indices) where tfidf_scores is a
    numpy array of scores and sorted_indices is a numpy array of indices sorted
    by descending score.
    """
    tfidf_scores = dense_matrix[0].tolist()[0]
    tfidf_scores = np.array(tfidf_scores)
    sorted_indices = np.argsort(tfidf_scores)[::-1]
    return tfidf_scores, sorted_indices


def plot_reality_check(dense_matrix, feature_names, top_n_words,
                       plot_file_name):
    """
    Create and save a bar plot of the top N words by TF-IDF score.

    :param dense_matrix: Dense matrix of TF-IDF scores.
    :param feature_names: List of feature (word) names corresponding to the
    TF-IDF scores.
    :param top_n_words: Number of top words to include in the plot.
    :param plot_file_name: Name of the file to save the plot.
    """
    tfidf_scores, sorted_indices = get_tfidf_score_and_indices(dense_matrix)
    sorted_indices = sorted_indices[:top_n_words]
    words = []
    scores = []
    for idx in sorted_indices:
        words.append(feature_names[idx])
        scores.append(tfidf_scores[idx])
    words = np.array(words)
    scores = np.array(scores)
    plt.figure(figsize=(12, 6))
    plt.bar(range(top_n_words), scores, align='center')
    plt.xticks(range(top_n_words), words, rotation=45, ha='right')
    plt.xlabel('Words')
    plt.ylabel('TF-IDF Score')
    plt.title(f'Top {top_n_words} words by TF-IDF score')
    plt.tight_layout()
    plt.savefig(save_path + plot_file_name)
    plt.close()


def count_topic_words(tokens, tf_idf_dict, topic_words):
    """
    Count the occurrence of topic-specific words in the tokens, weighted by
    their TF-IDF scores.

    :param tokens: List of tokens from the preprocessed text.
    :param tf_idf_dict: Dictionary mapping tokens to their TF-IDF scores.
    :param topic_words: List of words related to a specific topic.
    :return: float: The weighted count of topic words.
    """
    count = sum((tf_idf_dict[token] * 100)
                for token in tokens if token in topic_words)
    return count


def analyze_text_by_topics(tokens, tf_idf_dict):
    """
    Analyze the text for multiple predefined topics.

    :param tokens: List of tokens from the preprocessed text.
    :param tf_idf_dict: Dictionary mapping tokens to their TF-IDF scores.
    :return: dict: A dictionary with topics as keys and their corresponding
    weighted counts as values.
    """
    results = {
        'Health': count_topic_words(tokens, tf_idf_dict, health_words),
        'Crime': count_topic_words(tokens, tf_idf_dict, crime_words),
        'Education': count_topic_words(tokens, tf_idf_dict, education_words),
        'Defense': count_topic_words(tokens, tf_idf_dict, defense_words),
        'Foreign Relations': count_topic_words(tokens, tf_idf_dict,
                                               foreign_relations_words),
        'Religion': count_topic_words(tokens, tf_idf_dict, religion_words),
        'US Election': count_topic_words(tokens, tf_idf_dict,
                                         US_election_words)
    }
    return results


def count_candidate_words(tokens, tf_idf_dict, candidate_words):
    """
    Count the occurrence of candidate-specific words in the tokens, weighted by
    their TF-IDF scores.

    :param tokens: List of tokens from the preprocessed text.
    :param tf_idf_dict: Dictionary mapping tokens to their TF-IDF scores.
    :param candidate_words: Dictionary mapping candidates to their associated
    words.
    :return: dict: A dictionary with candidates as keys and their corresponding
    weighted word counts as values.
    """
    candidate_tfidf_sums = {}
    for candidate, words in candidate_words.items():
        total_tfidf = sum((tf_idf_dict.get(token, 0) * 100)
                          for token in tokens if token in words)
        candidate_tfidf_sums[candidate] = total_tfidf
    return candidate_tfidf_sums


def analyze_election_year(text, year, candidate_parties, seat_counts):
    """
    Perform comprehensive analysis on the text data for a specific election
    year.

    :param text: Preprocessed and tokenized text for the election year.
    :param year: The election year being analyzed.
    :param candidate_parties: Dictionary mapping parties to their associated
    words.
    :param seat_counts: Dictionary mapping parties to their seat counts.
    :return: dict: Analysis results including topic analysis and party scores.
    """
    vectorizer = TfidfVectorizer(token_pattern=r"\b\w+(?:[`'']\w+)?(?!'s)\b",
                                 stop_words=list(stop_words), encoding='utf-8')
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    new_features = [feature.replace("_", " ") if "_" in feature else feature
                    for feature in feature_names]
    dense_tfidf_matrix = tfidf_matrix.todense()

    plot_reality_check(dense_tfidf_matrix, new_features, 30,
                       f'top_features{year}')
    tf_idf_dict = {new_features[i]: dense_tfidf_matrix[0, i]
                   for i in range(len(new_features))}

    res = analyze_text_by_topics(new_features, tf_idf_dict)
    party_scores = count_candidate_words(new_features, tf_idf_dict,
                                         candidate_parties)
    plot_candidate_scores(party_scores, year, seat_counts)

    wordcloud = WordCloud(
        width=800, height=400,
        background_color='white').generate_from_frequencies(tf_idf_dict)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(save_path + f'word_cloud_{year}.png')
    plt.close()
    return res
