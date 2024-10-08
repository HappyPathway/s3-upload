#!/usr/bin/env python3
import random
import string
print(''.join(random.choices(string.ascii_uppercase + string.digits, k=32)))
