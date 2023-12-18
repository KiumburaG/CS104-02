Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # CS104
... # Kiumbura Githinji
... # conditions.py
... 
... # Input temperature from the user
... temp = int(input("Please enter the current temperature: "))
... 
... # Check temperature conditions and provide appropriate advice
... if temp > 90:
...     print("Wear Shorts")
... elif temp > 70:
...     print("Short sleeves are fine")
... elif temp > 50:
...     print("Wear a jacket")
... elif temp > 32:
...     print("Wear a heavy coat")
... else:
...     print("Stay Inside")
