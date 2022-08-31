from collections import Counter

c = [
'Júlia',
'Samuel',
'Isabella Calazans',
'Júlia',
'Samuel',
'Isabella Calazans',
'Isabella Calazans',
'Júlia',
'Hériclys',


]
c = [pessoa.strip().lower() for pessoa in c]

for k, v in Counter(c).items():
    print(f'Aluno {str(k).title()}\nFaltas: {v}\n')
