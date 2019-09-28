class _Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def by_index(start, end, line):
    return line[:start] + _Color.OKGREEN + line[start:end] + _Color.ENDC + line[end:]

def by_word(word, line):
    def _by_word(w, l):
        index = l.find(w)
        if index == -1:
            return [l]
        else:
            highlighted = _by_word(w, l[index + len(w):])
            return [l[:index], _Color.OKGREEN, w, _Color.ENDC, *highlighted]
    return ''.join(_by_word(word, line))

def by_token(indices, doc, color=_Color.OKGREEN):
    highlighted = []
    for i, token in enumerate(doc):
        if i in indices:
            highlighted.append(color + token.text + _Color.ENDC)
        else:
            highlighted.append(token.text)
    return ' '.join(highlighted)

def by_token_two_color(indices1, indices2, doc, color1=_Color.OKGREEN, color2=_Color.OKBLUE):
    highlighted = []
    for i, token in enumerate(doc):
        if i in indices1:
            highlighted.append(color1 + token.text + _Color.ENDC)
        elif i in indices2:
            highlighted.append(color2 + token.text + _Color.ENDC)
        else:
            highlighted.append(token.text)
    return ' '.join(highlighted)