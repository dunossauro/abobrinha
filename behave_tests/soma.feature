#language: pt
Funcionalidade: Soma
"""
Realiza casos de testes referentes a soma
"""

Cenário: Soma de números inteiros
  Dado que somo "2" e "2"
  Então o resultado deve ser "4"

Cenário: Soma de números flutuantes
  Dado que somo "2.0" e "2.0"
  Então o resultado deve ser "4.0"

Cenário: Soma entre números e string
  Dado que somo "2.0" e "A"
  Então o resultado deve ser "Insira um número"
