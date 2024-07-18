import re


# Fonction pour charger le contenu d'un document texte
def load_document(filepath : str):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

# Fonction pour trouver les mots ou phrases communs entre deux documents en utilisant l'algorithme naïf brute force
def find_common_patterns(doc1, doc2, pattern_length=3):
    # Diviser les documents en listes de mots
    words1 = re.findall(r'\w+', doc1.lower())
    words2 = re.findall(r'\w+', doc2.lower())

    # Utiliser des ensembles pour trouver les motifs communs
    patterns1 = set()
    patterns2 = set()

    # Extraire les motifs de longueur spécifiée
    for i in range(len(words1) - pattern_length + 1):
        patterns1.add(' '.join(words1[i:i + pattern_length]))
    
    for i in range(len(words2) - pattern_length + 1):
        patterns2.add(' '.join(words2[i:i + pattern_length]))
    
    # Trouver les motifs communs
    common_patterns = patterns1.intersection(patterns2)
    
    return common_patterns

# Fonction pour calculer le pourcentage de mots communs
def word_similarity(doc1, doc2):
    words1 = re.findall(r'\w+', doc1.lower())
    words2 = re.findall(r'\w+', doc2.lower())
    
    set_words1 = set(words1)
    set_words2 = set(words2)
    
    common_words = set_words1.intersection(set_words2)
    
    total_words = len(set_words1.union(set_words2))
    
    if total_words == 0:
        return 0.0
    
    return (len(common_words) / total_words) * 100

# Fonction pour calculer le pourcentage de phrases communes
def sentence_similarity(doc1, doc2):
    sentences1 = re.split(r'[.!?]', doc1.lower())
    sentences2 = re.split(r'[.!?]', doc2.lower())
    
    set_sentences1 = set([s.strip() for s in sentences1 if s.strip()])
    set_sentences2 = set([s.strip() for s in sentences2 if s.strip()])
    
    common_sentences = set_sentences1.intersection(set_sentences2)
    
    total_sentences = len(set_sentences1.union(set_sentences2))
    
    if total_sentences == 0:
        return 0.0
    
    return (len(common_sentences) / total_sentences) * 100

    # Fonction pour uploader le premier document
def handle_uploaded_file_01(file):
    with open(settings.BASE_DIR / "uploads/document1.txt", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    
    return load_document(settings.BASE_DIR / "uploads/document1.txt")

# Fonction pour uploader le deuxieme document
def handle_uploaded_file_02(file):
    with open(settings.BASE_DIR / "uploads/document2.txt", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    
    return load_document(settings.BASE_DIR / "uploads/document2.txt")