import re

text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T


cat 
bat 
mat 
bat



CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net



https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov



'''

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)