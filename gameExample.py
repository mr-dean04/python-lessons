countries = ['ghana', 'benin', 'togo', 'angola', 'nigeria', 'senegal', 'gabon']
print("Select random number to pick (0 - 6):")


selectedValue = int(input())

#use pop

'''
selectedCountry = countries.pop(selectedValue)
print(selectedCountry)
print(countries)
'''

#use del
selectedCountry = countries[selectedValue]  #countries[2]
del countries[selectedValue]
print(selectedCountry)
print(countries)



