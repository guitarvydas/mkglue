import sys
import re

for line in sys.stdin:
    newl = re.sub (r' \| [A-Za-z]+', '', line).strip ()
    newl = re.sub (r'([A-Za-z]+)\*', r'@\1', newl)
    newl = re.sub (r'([A-Za-z]+)\+', r'@\1', newl)
    newl = re.sub (r'("[A-Za-z\\]+")', r'k', newl)
    newl2 = re.sub (r'\n', '', newl) + "]"
    newl2 = re.sub (r' = ', ' [', newl2)
    deconstruct = re.search (r'([A-Za-z]+) \[(.*)\]', newl2)
    if deconstruct:
        name = deconstruct.group (1)
        params = deconstruct.group (2).replace('(','').replace(')','')
        body = ""
        for part in params.split(' '):
            identity = '${' + part + '}'
            identity = identity.replace ('@','')
            body = body + identity
        print (name + '[' + params + '] = [[' + body + ']]')
    else:
        print (newl)
