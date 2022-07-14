
import sys
import os
prevdir = os.path.dirname(os.getcwd())
sys.path.append(prevdir)

from moduleA import A

a = A(True)

print(a.imported)