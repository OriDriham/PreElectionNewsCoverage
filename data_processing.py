from nltk.tokenize import RegexpTokenizer
from nltk.stem import porter

stemmer = porter.PorterStemmer()


def get_articles_list(folders, news_lst):
    """
    Generate a list of article file paths based on the given folders and news
    sources.

    :param folders: List of folder names containing the articles.
    :param news_lst: List of news source prefixes.
    :return: list: A list of file paths for all articles.
    """
    articles_lst = []
    for folder in folders:
        range_articles = 11
        articles_lst += [
            f'{folder}\\{name}{i}.txt'
            for name in news_lst
            for i in range(1, range_articles)
        ]
    return articles_lst


def get_election_list(folder, news_lst):
    """
    Generate a list of article file paths for a specific election folder.

    :param folder: The name of the folder containing election articles.
    :param news_lst: List of news source prefixes.
    :return: list: A list of file paths for articles in the specified election
    folder.
    """
    election_lst = []
    range_articles = 11
    election_lst += [
        f'{folder}\\{name}{i}.txt'
        for name in news_lst
        for i in range(1, range_articles)
    ]
    return election_lst


def get_all_elections_list(folders, news_lst):
    """
    Generate lists of article file paths for all election folders.

    :param folders: List of folder names containing the election articles.
    :param news_lst: List of news source prefixes.
    :return: tuple: Five lists of file paths, one for each election year.
    """
    elections_lst = []
    for folder in folders:
        elections_lst.append(get_election_list(folder, news_lst))
    return (elections_lst[0], elections_lst[1], elections_lst[2],
            elections_lst[3], elections_lst[4])


def tokenize_text_from_articles(articles):
    """
    Tokenize and preprocess text from a list of article files.

    :param articles: List of file paths to article text files.
    :return: str: Preprocessed and tokenized text from all articles combined.
    """
    tok = RegexpTokenizer(r"\b\w+(?:[`'']\w+)?(?!'s)\b")
    space_exclusions = ["yisrael beytenu", "united torah judaism",
                        "national unity",  "tikva hadasha",
                        "religious zionist party", "yesh atid", "new hope",
                        "blue and white", "derekh eretz", "joint list",
                        "yisrael beiteinu", "united torah judaism"]
    apostrophe_exclusions = ["ya'alon", "sa'ar"]
    text = ""
    for article in articles:
        with open(article, "r", encoding='utf-8') as f:
            a = f.read().lower()

            for exc in space_exclusions:
                a = a.replace(exc, "_".join(exc.split(" ")))
            for exc in apostrophe_exclusions:
                a = a.replace(exc, "".join(exc.split("'")))

            tokens = tok.tokenize(a)
            for token in tokens:
                if token.isnumeric() or "." in token:
                    if int(token) < 1000 or int(token) > 2100:
                        tokens.remove(token)
            text += " " + " ".join(tokens)
    text = text.replace("'s", "")
    text = text.replace("'s", "")
    return text
