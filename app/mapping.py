# mapping.py
# Mapeamento dinâmico entre frases em PT-BR e proposições (p, q, r...)
DEFAULT_MAP = {
    "joão foi ao mercado": "p",
    "comprou leite": "q",
    "comprou pão": "r",
    "está chovendo": "s"
}

def phrase_to_symbol_map():
    return dict(DEFAULT_MAP)

def symbol_to_phrase_map():
    return {v: k for k, v in DEFAULT_MAP.items()}

def add_mapping(phrase, symbol):
    DEFAULT_MAP[phrase.lower().strip()] = symbol.strip()