#!/usr/bin/env python

#!/usr/bin/env python

# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def l100kmtompg(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def mpgtol100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100


if __name__ == '__main__':

	print(l100kmtompg(3.9))
	print(l100kmtompg(7.5))
	print(l100kmtompg(10.))
	print(mpgtol100km(60.3))
	print(mpgtol100km(31.4))
	print(mpgtol100km(23.5))
