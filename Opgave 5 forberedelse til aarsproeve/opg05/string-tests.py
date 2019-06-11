s = "The quick brown fox jumps over the lazy dog"

if "ox" in s: #Tjekker om tegnene ox er i s, hvis der er det, så printes at den har fundet et ox i s.
    print("Found 'ox'")

if "horse" in s: #Tjekker om tegnene / ordet horse er i s, hvis der er det, så printes at den har fundet horse i s. Eftersom der ikke er horse i s, så printes den ikke
    print("Found 'horse'")

print(s[0]) #Printer det første tegn i s
print(s[-1]) #Printer det sidste tegn i s, da vi kører baglæns
print(s[1:7]) #Printer tegnene fra andet tegn i s til syvende tegn i s
print(s[-3:]) #Printer fra tredje sidste tegn i s til slut af s
