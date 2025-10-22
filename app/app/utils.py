# utils.py
import re

def looks_like_cpc(s):
    if not s:
        return False
    # se contém operadores lógicos ou símbolos de proposição comuns
    return bool(re.search(r"[∧∨¬\^\~v&\|()]", s)) or bool(re.match(r"^[A-Za-z]\s*(?:[∧∨v\^&\|\)\(]|$)", s))