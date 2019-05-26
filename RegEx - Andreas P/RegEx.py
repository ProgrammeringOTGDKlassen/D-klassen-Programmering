import re

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec at euismod ex, vel placerat tortor. Fusce et egestas ante. Fusce condimentum fringilla nisl, eget volutpat 13 nunc dignissim eget. Etiam porta justo eu iaculis pretium. Pellentesque sed condimentum nulla. Fusce sit 127 amet scelerisque urna. Lorem ipsum dolor sit 17 amet, consectetur adipiscing elit.'

'''
text = "Ten 10, Twenty 20, Thirty 30"
test = re.findall('T....y', text)
for element in test:
    print(element)

# re.match()
'''

# # Strengen til at søge i.
# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec at euismod ex, vel placerat tortor. Fusce et egestas ante. Fusce condimentum fringilla nisl, eget volutpat 13 nunc dignissim eget. Etiam porta justo eu iaculis pretium. Pellentesque sed condimentum nulla. Fusce sit 127 amet scelerisque urna. Lorem ipsum dolor sit 17 amet, consectetur adipiscing elit.'

# # søgningen og det regulære udtryk
# result = re.findall("[A-ZÆØÅ]{1}[a-zæøå]*", text)

# # Print resultatet.
# for element in result:
#     print(element)


# Opgave 21
# alle ord, der starter med stort bogstav
# stort_bogstav = re.findall('[A-ZÆØÅ]{1}[a-zæøå]*', text)
# for element in stort_bogstav:
#     print(element)

# alle tal
# tal = re.findall('\d+', text)
# for element in tal:
#     print(element)

# find alle ord der har et o som andet bogstav
# o_bogstav = re.findall('[a-zæøåA-ZÆØÅ]{1}o[a-zæøåA-ZÆØÅ]*', text)
# for element in o_bogstav:
#     print(element)

# Print det første ord i teksten
# f_ord = re.findall("^[A-ZÆØÅ][a-zæøå]*", text)
# for element in f_ord:
#     print(element)

# Print det sidste ord i teksten (husk en tekst plejer at slutte med et punktum).
# s_ord = re.findall('[a-zæøåA-ZÆØÅ]+\.$', text)
# for element in s_ord:
#     print(element)

# Find alle ord der efterfølges af et komma eller et punktum
# kp_ord = re.findall("[a-zæøåA-ZÆØÅ]+[.,]{1}", text)
# for element in kp_ord:
#     print(element)


# opgave personer
class Person():
    def __init__(self, fuldeNavn, adresse, postnummer, by, mobil, email):
        self.fuldeNavn = fuldeNavn
        self.adresse = adresse
        self.postnummer = postnummer
        self.by = by
        self.mobil = mobil
        self.email = email
    def __str__(self):
        return "Fulde navn: {} \nAdresse: {} \nPostnummer: {} \nBy: {} \nMobil: {} \nE-mail: {}".format(self.fuldeNavn, self.adresse, self.postnummer, self.by, self.mobil, self.email)


Jens = Person('Jens Jensen', 'Gl. Konge Vej', '6969', 'Odense', '69696969', 'din_mor@gmail.com')
print(Jens)