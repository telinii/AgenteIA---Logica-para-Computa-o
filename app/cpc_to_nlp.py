# cpc_to_nlp.py
import re
from mapping import symbol_to_phrase_map

OP_MAP = {"∧": "e", "^": "e", "&": "e", "∨": "ou", "v": "ou", "|": "ou"}
NEG_SYMBOLS = {"¬", "~"}

def tokenize(formula):
    spaced = re.sub(r'([\(\)¬~∧∨\^\|&v])', r' \1 ', formula)
    parts = [p for p in spaced.split() if p.strip()]
    return parts

def prop_to_phrase(token, rev_map):
    # negação simples
    if token.startswith("¬") or token.startswith("~"):
        base = token[1:]
        phrase = rev_map.get(base)
        if phrase:
            return f"não {phrase}"
        return f"não {base}"
    if token in rev_map:
        return rev_map[token]
    return token

def cpc_to_nl(formula):
    if not formula:
        return ""
    rev_map = symbol_to_phrase_map()
    tokens = tokenize(formula)
    parts = []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t in OP_MAP:
            parts.append(OP_MAP[t])
            i += 1
        elif t in NEG_SYMBOLS:
            # negação unária
            if i+1 < len(tokens):
                nxt = tokens[i+1]
                phrase = prop_to_phrase("¬"+nxt, rev_map)
                parts.append(phrase)
                i += 2
            else:
                parts.append("não")
                i += 1
        elif t == "(" or t == ")":
            i += 1
        else:
            parts.append(prop_to_phrase(t, rev_map))
            i += 1
    # montagem: juntar e ajustar espaçamento
    sentence = " ".join(parts)
    sentence = re.sub(r"\s+,", ",", sentence)
    sentence = sentence.capitalize().strip()
    if not sentence.endswith("."):
        sentence += "."
    return sentence