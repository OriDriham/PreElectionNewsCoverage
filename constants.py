from nltk.corpus import stopwords

articles_folders = ["elections2019a", "elections2019b", "elections2020",
                    "elections2021", "elections2022"]
jerusalem_string = "jerusalem_article"
times_string = "times_article"
news_list = [jerusalem_string, times_string]

health_words = [
    'health', 'medicine', 'hospital', 'doctor', 'nurse', 'medical',
    'disease', 'treatment', 'vaccine', 'mental', 'wellness', 'clinic',
    'surgery', 'diagnosis', 'nutrition', 'healthcare', 'illness',
    'epidemic', 'pandemic', 'therapy', 'fitness', 'exercise', 'hygiene',
    'pharmacy', 'patient', 'immunity', 'infection', 'symptom', 'prevention']

crime_words = [
    'crime', 'criminal', 'theft', 'murder', 'assault', 'robbery',
    'fraud', 'violence', 'homicide', 'burglary', 'arrest', 'police',
    'law', 'justice', 'illegal', 'offense', 'penalty', 'punishment',
    'court', 'trial', 'conviction', 'prison', 'jail', 'felony',
    'misdemeanor', 'vandalism', 'smuggling', 'drug', 'gang', 'cybercrime']

education_words = [
    'education', 'school', 'university', 'college', 'student', 'teacher',
    'academic', 'curriculum', 'lecture', 'exam', 'degree', 'diploma',
    'learning', 'scholarship', 'tuition', 'classroom', 'literacy',
    'enrollment', 'graduate', 'study', 'syllabus', 'assignment',
    'research', 'institution', 'faculty', 'course', 'seminar', 'training',
    'evaluation', 'knowledge']

defense_words = [
    'defense', 'military', 'army', 'navy', 'air force', 'security',
    'war', 'weapon', 'conflict', 'battle', 'soldier', 'troop',
    'strategy', 'tactic', 'border', 'protection', 'national security',
    'alliance', 'missile', 'nuclear', 'defense minister', 'army chief',
    'intelligence', 'surveillance', 'combat', 'operation', 'patrol',
    'deployment', 'fortification', 'peacekeeping']

foreign_relations_words = [
    'diplomacy', 'foreign', 'international', 'relations', 'ambassador',
    'embassy', 'treaty', 'agreement', 'ally', 'negotiation', 'trade',
    'export', 'import', 'sanction', 'policy', 'summit', 'cooperation',
    'conflict', 'global', 'united nations', 'european union', 'nato',
    'partnership', 'dialogue', 'foreign minister', 'geopolitics',
    'bilateral', 'multilateral', 'consulate', 'visa']

religion_words = [
    'religion', 'faith', 'church', 'mosque', 'synagogue', 'temple',
    'god', 'spiritual', 'belief', 'worship', 'prayer', 'bible', 'quran',
    'torah', 'clergy', 'pastor', 'imam', 'rabbi', 'ritual', 'ceremony',
    'doctrine', 'theology', 'pilgrimage', 'saint', 'divine', 'monk',
    'nun', 'religious', 'sect', 'denomination']

US_election_words = [
    'biden', 'trump', 'republican', 'democrat', 'harris', 'pence', 'USA']

candidate_names_2022 = {
    "Likud": ["netanyahu", "bibi", "likud"],
    "Yesh Atid": ["lapid", "yesh atid"],
    "RZP–Otzma": ["rzp", "otzma", "religious zionist party", "smotrich"],
    "National Unity": ["gantz", "national unity"],
    "Shas": ["shas", "deri"]
}

candidate_names_2021 = {
    "Likud": ["netanyahu", "bibi", "likud"],
    "Yesh Atid": ["lapid", "yesh atid"],
    "Shas": ["shas", "deri"],
    "Blue and White": ["blue and white", "gantz"],
    "Yamina": ["bennett", "yamina"]
}

candidate_names_2020 = {
    "Likud": ["netanyahu", "bibi", "likud"],
    "Blue and White": ["blue and white", "gantz"],
    "Joint List": ["joint list", "odeh"],
    "Shas": ["shas", "deri"],
    "United Torah Judaism": ["utj", "gimel", "united torah judaism", "litzman"]
}

candidate_names_2019b = {
    "Blue and White": ["blue and white", "gantz"],
    "Likud": ["netanyahu", "bibi", "likud"],
    "Joint List": ["joint list", "odeh"],
    "Shas": ["shas", "deri"],
    "Yisrael Beytenu": ["yisrael beytenu", "liberman"]
}

candidate_names_2019a = {
    "Likud": ["netanyahu", "bibi", "likud"],
    "Blue and White": ["blue and white", "gantz"],
    "Shas": ["shas", "deri"],
    "United Torah Judaism": ["utj", "gimel", "united torah judaism",
                             "litzman"],
    "Labor": ["labor", "gabbay"]
}

seat_count_2022 = {
    "Likud": 32,
    "Yesh Atid": 24,
    "RZP–Otzma": 14,
    "National Unity": 12,
    "Shas": 11
}

seat_count_2021 = {
    "Likud": 30,
    "Yesh Atid": 17,
    "Shas": 9,
    "Blue and White": 8,
    "Yamina": 7
}

seat_count_2020 = {
    "Likud": 36,
    "Blue and White": 33,
    "Joint List": 15,
    "Shas": 9,
    "United Torah Judaism": 7
}

seat_count_2019b = {
    "Blue and White": 33,
    "Likud": 32,
    "Joint List": 13,
    "Shas": 9,
    "Yisrael Beytenu": 8
}

seat_count_2019a = {
    "Likud": 35,
    "Blue and White": 35,
    "Shas": 8,
    "United Torah Judaism": 8,
    "Labor": 6
}

stop_words = set(stopwords.words('english'))

save_path = 'results/'
