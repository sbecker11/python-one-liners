from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Cramming Python into Makefiles
A related issue is embedding Python into a Makefile. I had a really long script that I was trying to cram into a makefile so I automated the process:


Toggle line numbers
   1 import sys,re
   2 
   3 def main():
   4     fh = open(sys.argv[1],'r')
   5     lines = fh.readlines()
   6     print '\tpython2.2 -c "`printf \\"if 1:\\n\\'
   7     for line in lines:
   8         line = re.sub('[\\\'\"()]','\\\g<0>',line)
   9         # grab leading white space (should be multiples of 4) and makes them into
  10         # tabs
  11         wh_spc_len = len(re.match('\s*',line).group())
  12 
  13         sys.stdout.write('\t')
  14         sys.stdout.write(wh_spc_len/4*'\\t'+line.rstrip().lstrip())
  15         sys.stdout.write('\\n\\\n')
  16     print '\t\\"`"'
  17 
  18 if __name__=='__main__':
  19     main()
This script generates a "one-liner" from make's point of view.

