import sys
xyz='aeiouAEIOU'
x='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
g=input()
if g in xyz:
  print("Vowel")
elif g in x:
  print("Consonant")
else:
  print("invalid")
