# Составить генератор (yield), который переведет символы строки из верхнего
# регистра в нижний.

string = input('Напишите любое предложение или набор слов: ')
gen = (s.lower() for s in string)
result = ''.join(gen)
print(result)