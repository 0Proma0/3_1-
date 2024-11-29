txt = """Would to heaven that the reader, emboldened and momentarily ferocious as he reads,
finds his wild and savage path through the desolate marshes of these dark and poisonous pages, 
without disorientation; for, unless he brings in his reading a rigorous logic and a tension of mind 
equal at least to his distrust, the mortal emanations of this book will soak his soul, as water sugar. 
It is not good for everybody to read the pages that follow; some alone will savor this bitter fruit without danger. 
Therefore, timid soul, before penetrating farther into such unexplored heaths, directs your heels back and not forward. 
Listen well to what I say to you: run your heels back and not forward, like the eyes of a son who, 
deviates respectfully from the august contemplation of the maternal side; 
or, rather, as an endless angle of chilly cranes of great meditation, which, during the winter, 
flies powerfully through the silence, with all sails stretched, towards a fixed point of the horizon, 
whence suddenly leaves a strange and strong wind, precursor of the storm. 
""".replace('\n', ' ')

import re
expr1 = r'\bm\w*'
expr2 = r'\b\w+\s+and'
expr3 = r'\b[^f]\w{6}'
expr4 = r'\b\w{1,4}ing\b'
matches1 = re.findall(expr1, txt)
print(matches1)
matches2 = re.findall(expr2, txt)
print(matches2)
matches3 = re.findall(expr3, txt)
print(matches3)
matches4 = re.findall(expr4, txt)
print(matches4)