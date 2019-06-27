import sys
vow1='aeiouAEIOU'
x='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
c=input()
if c in vow1:
  print("vowel")
 elif c in x:
  print("Consonant")
else:
  print("invalid")
