import re
expr = 'CC[GA][CT]GG'
sek = 'GGCCGAGAGCCGACCGCGGCCGGGTTCC'
matches = re.findall(expr, sek)
print(matches)