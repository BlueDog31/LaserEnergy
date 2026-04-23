
from pylab import *

y = array([3.73, 3.53, 3.75, 3.63, 3.82])
n = len(y)
y_snitt = sum(y) / n
s = sqrt(sum(y - y_snitt)**2 / (n - 1))
se = s/sqrt(n) #se = standard error
em = 2*se #em = error margin/feilmargin

print("Gjennomsnittet er:", round(y_snitt, 2))
print("Standardavviket er", round(s, 2))
print("Standard error is:", round(se, 2))
