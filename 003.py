import sys
xyz='aeiouAEIOU'
x='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
g=input()
if g in xyz:
  print("vowel")
 elif g in x:
  print("Consonant")
else:
  print("invalid")
