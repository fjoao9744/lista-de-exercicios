'''
import random

aluno = random.choice(['joao', 'maria', 'josé', 'cristina', 'smogon'])

print(f"o aluno escolhido foi: {aluno}")

'''

'''
from random import choice

alunos = ['joao', 'maria', 'josé', 'cristina', 'smogon']

print(f"o aluno escolhido foi: {choice(alunos)}")
'''

from random import choice

def escolher(x):
    return choice(x)

alunos = ['joao', 'maria', 'josé', 'cristina', 'smogon']

print(f"o aluno escolhido foi: {escolher(alunos)}")
    