# Project: Generating Random Quiz Files

import random, os
from pathlib import Path

Respostas = {'do Acre':'Rio Branco','de Alagoas':'Maceió','do Amapá':'Macapá','do Amazonas':'Manaus',
             'da Bahia':'Salvador','do Ceará':'Fortaleza','do Espírito Santo':'Vitória','de Goiás':'Goiânia',
             'do Maranhão':'São Luís','do Mato Grosso':'Cuiabá','do Mato Grosso do Sul':'Campo Grande',
             'de Minas Gerais':'Belo Horizonte','do Pará':'Belém','da Paraíba':'João Pessoa','do Paraná':'Curitiba',
             'de Pernambuco':'Recife','do Piauí':'Teresina','do Rio de Janeiro':'Rio de Janeiro',
             'do Rio Grande do Norte':'Natal','do Rio Grande do Sul':'Porto Alegre','de Rondônia':'Porto Velho',
             'da Roraima':'Boa Vista','de Santa Catarina':'Florianópolis','de São Paulo':'São Paulo',
             'de Sergipe':'Aracaju','de Tocantins':'Palmas','do Distrito Federal':'Brasília'}

for quizNum in range (35):
    Estados = list(Respostas.keys())
    random.shuffle(Estados)
    quiz = open(f"Quiz_{str(quizNum+1)}.txt", 'w')
    quizAns = open(f"Quiz Answer_{str(quizNum+1)}.txt", 'w')
    quiz.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz.write((' ' * 20) + f'Quiz Capitais dos Estados (Formulário {quizNum + 1})')
    quiz.write('\n\n')
    for questionNum in range(len(Estados)):
        quiz.write(f"{str(questionNum+1)}. Qual a capital {Estados[questionNum]}?\n")
        escolhas = random.sample(list(Respostas.values()), 4)
        if not Respostas[Estados[questionNum]] in escolhas:
            del escolhas[escolhas.index(random.choice(escolhas))]
            escolhas.append(Respostas[Estados[questionNum]])
        random.shuffle(escolhas)
        for i in range(len(escolhas)):
            quiz.write(f"   {'ABCD'[i]}. {escolhas[i]}\n")
        quizAns.write(f"{str(questionNum+1)}.{'ABCD'[escolhas.index(Respostas[Estados[questionNum]])]}\n")
        quiz.write('\n')
    quiz.close()
    quizAns.close()

        
    
