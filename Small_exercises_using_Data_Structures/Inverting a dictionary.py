# An algorithm that creates the right-hand side dictionary from the one on the left-hand side.

def invert(original: dict) -> dict:
    inverted = dict()
    for (word, translations) in original.items():
        for translation in translations:
            if translation in inverted:
                inverted[translation].append(word)
            else:
                inverted[translation] = [word]
    return inverted


pt_to_en = {
    'carro': ['car'],
    'andar': ['floor', 'walk'],     # as in 'second floor'
    'chão': ['floor'],              # as in 'wooden floor'
    'saudade': []                   # translation omitted
}

en_to_pt = {
    'car' : ['carro'],
    'walk': ['andar'],
    'floor': ['andar', 'chão']
}

invert_tests = [
    #case,              a_to_b,             inverted
    ('no words',        dict(),             dict()),
    ('pt_to_en',        pt_to_en,           en_to_pt)
]