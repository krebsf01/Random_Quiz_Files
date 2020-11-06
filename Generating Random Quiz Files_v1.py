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
    Capitais = list(Respostas.values())
    Estados = list(Respostas.keys())
    random.shuffle(Estados)
    quiz = open('Quiz_'+ str(quizNum+1)+'.txt', 'w')
    quizAns = open('Quiz Answer_'+ str(quizNum+1)+'.txt', 'w')
    for questionNum in range(len(Estados)):
        quiz.write(str(questionNum+1) +'. Qual a capital '+ Estados[questionNum] + '?' + '\n')
        escolhas = random.sample(Capitais, 4)
        if not Respostas[Estados[questionNum]] in escolhas:
            del escolhas[escolhas.index(random.choice(escolhas))]
            escolhas.append(Respostas[Estados[questionNum]])
        random.shuffle(escolhas)
        for i in range(len(escolhas)):
            Alt = ['A', 'B', 'C', 'D']
            quiz.write(Alt[i]+'. '+ escolhas[i] +'\n')
            if escolhas[i] == Respostas[Estados[questionNum]]:
                quizAns.write(str(questionNum+1)+ '.' + Alt[i] +'\n')
        quiz.write('\n')
    quiz.close()
    quizAns.close()

        
    
