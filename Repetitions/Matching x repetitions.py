Regex_Pattern = r'^[a-zA-Z02468]{40}[\s13579]{5}$'    # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
