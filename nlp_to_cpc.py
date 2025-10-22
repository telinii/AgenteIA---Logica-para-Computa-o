# nlp_to_cpc.py
import re
from app.mapping import phrase_to_symbol_map

CONNECTIVES = {"e": "∧", "ou": "∨", "mas": "∧", "nem": "∧"}
NEGATIONS = {"não", "nao", "nunca"}

def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"[.,;:]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

def split_by_connectives(text):
    # retorna lista intercalando frases e conectivos como tokens
    tokens = []
    words = text.split()
    buf = []
    for w in words:
        if w in CONNECTIVES:
            if buf:
                tokens.append(" ".join(buf))
                buf = []
            tokens.append(w)
        elif w in NEGATIONS:
            buf.append("não")
        else:
            buf.append(w)
    if buf:
        tokens.append(" ".join(buf))
    return tokens

def map_phrase_to_symbol(phrase, mapping):
    phrase = phrase.strip()
    # tentativa exata
    if phrase in mapping:
        return mapping[phrase]
    # tentativa por substring (frase contém chave)
    for k, v in mapping.items():
        if k in phrase:
            return v
    # se começa com 'não ' -> tratar negação
    if phrase.startswith("não "):
        base = phrase[4:]
        sym = map_phrase_to_symbol(base, mapping)
        if sym:
            return f"¬{sym}"
    return None

def nl_to_cpc(text):
    text = normalize(text)
    if not text:
        return ""
    mapping = phrase_to_symbol_map()
    tokens = split_by_connectives(text)
    out = []
    for t in tokens:
        if t in CONNECTIVES:
            out.append(CONNECTIVES[t])
        else:
            sym = map_phrase_to_symbol(t, mapping)
            if sym is None:
                # gerar símbolo temporário xN
                sym = f"x{len([c for c in out if c.startswith('x')])+1}"
            out.append(sym)
    # juntar com espaços, manter parênteses simples se houver 'ou' com 'e' -- aqui deixamos linear
    return " ".join(out)