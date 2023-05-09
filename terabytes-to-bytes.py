# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

import pprint;pprint.pprint(zip(('Byte', 'KByte', 'MByte', 'GByte', 'TByte'), (1 << 10*i for i in range(5))))