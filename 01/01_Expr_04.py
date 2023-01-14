w, h = float(input()), float(input())

from math import sqrt, log10

mosteller = sqrt(w * h) / 60
haycock = 0.024265 * ( w ** 0.5378 ) * ( h ** 0.3964 )
boyd = 0.0333 * ( w ** ( 0.6157 - 0.0188 * log10( w ))) * ( h ** 0.3 )

print(mosteller)
print(haycock)
print(boyd)