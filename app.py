# Importanto a função do arquivo calculadora/__init__.py
import os
import sys

sys.path.insert(0, os.getcwd())

from Projetos.calculadora.__init__ import calcule

# Executando a aplicação
calcule()