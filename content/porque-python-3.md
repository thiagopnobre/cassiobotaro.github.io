Title: Por que python 3?
Date: 2015-03-10 03:00  
Category: Python3  
Tags: python, python3, iniciantes 
Slug: porque-python-3 
Author: Cássio Botaro  
Summary: Motivos para a utilização da versão 3.0 da linguagem Python.
related_posts: hello-word

![logo-python](../images/logopython2.png 
"Logo Python")

##Um pouco de história

O python 3.0 foi uma decisão tomada em 2008, e decidiu-se assim por causa da incompatibilidade de alguns novos recursos com a versão 2.0 .
É uma versão com novas baterias incluídas como asyncio, pip, enum, statistics, venv.
Uma longa correção da nomeclatura de alguns módulos foi feita seguindo mais o padrão pythonico(pep-8).
Outras mudanças foram a transformação do print em uma função, o que trouxe novas possibilidades, a utilização de visão e iteradores ao invés de listas como retorno de alguns métodos, a unificação de long e int, e várias outras mudanças que serão apresentadas.

##Mas porque python 3?

Se a correção de nomeclatura e inclusão de novas bibliotecas à biblioteca padrão do python ainda não te convenceram, abaixo serão listados novos recursos e possibilidades que podem te atrair a esta nova versão. 

##Fatiamento

Agora é possivel extrair, inicio, meio e fim de sequencias utlizando novas possibilidades de atribuições.

```python
head, *rest, tail = range(10)
print(head)
# retorna 0
print(tail)
# retorna 9
print(rest)
# retorna [1, 2, 3, 4, 5, 6, 7, 8]
*rest, tail = range(5)
print(rest)
# retorna [0, 1, 2, 3]
print(tail)
# retorna 4
```

##Iteradores em todo lugar!
Nada de se preocupar em otimizar memória modificando o metodo através da adição de algum prefixo como x  ou iter.
Ou seja, nada mais de Xtudo ou iterlista no python 3.

```python
print(range(10))
# retorna range(0, 10)
# não é mais uma lista
# se comporta como xrange do python 2
for numero in range(10):
    print(numero, endp=" ")
# 0 1 2 3 4 5 6 7 8 9
dic = {"chaveA": 1, "chaveB": 2, "chaveC": 3}
dic.keys()
# retorna dict_keys(['chaveB', 'chaveC', 'chaveA'])
# visão com os valores das chaves do dicionário
for (chave, valor) in dic.items():
    print(chave, valor)
# chaveB 2
# chaveC 3
# chaveA 1
```


##Tipificação forte em comparadores.

Dado que python é uma linguagem dinâmica porém  com tipificação forte, nada mais sensato que comparadores também reclamem quando tipos distintos são comparados.

```python
# No Python 2
'abc' > 1
# True
None < 0
# True

# No Python 3
'abc' > 1
# TypeError: unorderable types: str() > int()
None < 0
# TypeError: unorderable types: NoneType() < int()
```

##Strings divididas em bytes e unicodes

Agora é possivél utilizar de acentos, caracteres de outros alfabetos como chinês e outros caracteres especias.

```python
# python 2
nome ='cássio'
nome 
# 'c\xc3\xa1ssio
bytes('cássio')
# 'c\xc3\xa1ssio
# bytes e strings são a mesma coisa

# python 3
nome ='cássio'
nome 
# 'cássio'
bytes('cássio', encoding='utf-8')
# b'c\xc3\xa1ssio'
# bytes e strings são coisas distintas
```

E uma outra coisa permitida:

```python 
def Σ(lim_inf, lim_sup, funcao):
    '''Um somatório é um operador matemático que nos permite
    representar facilmente somas de um grande número de termos,
    até infinitos.
    É representado com a letra grega sigma ( \Sigma ).
    Uma variável i chamada índice do somatório recebe como valor inicial o
    limite inferior(lim_inf).A
    Esta variável percorre os valores inteiros até alcançar o limite
    superior(lim_sup).
    A cada iteração uma função(funcao) é executada sobre o índice do
    somatório.
    A função de entrada (funcao) deve receber um valor de entrada e retornar
    um valor de saída.

    Σ(1,5,lambda x:x) = 1 + 2 + 3 + 4 + 5 = 15

    >>> Σ(1,5,lambda x:x)
    15
    '''
    return sum([funcao(i) for i in range(lim_inf, lim_sup + 1)])
```

##Leitura de dados de forma segura

Toda leitura de dados feita do teclado é feita em forma de string  e cabe ao programa sua manipulação.
```python
# No python 2 
a = input('Comando a ser executado: ')
# experimente a expressão 80*'-' como entrada
# embora no python 2 existe uma versão mais segura que é o raw_input
# no python 3
input("Digite um número: ")
# '4'
# o input sempre retorna string e caso precise deve ser explicitamente convertida
```

##python -m modulo
Uma série de módulos da biblioteca padão se utilizam do artificio de colocar uma condicional para verificar quando são executados ou importados e podem ser utilizados como ferramentas.

```bash
# criação de um ambiente virtual
python -m venv /path/to/<my_venv>
# ubuntu apresenta problemas, nele utilize
python -m venv --without-pip /path/to/<my_venv>
# ativação deste ambiente
source /path/to/<my_venv>/bin/activate

# PYTHONPATH
python -m site

# Servidor http python
python -m http.server [port]

# Documentação
python -m pydoc
# b para abrir documentação no browser
python -m pydoc -b
# ou especifique o módulo
python -m pydoc math.sin

# debug estilo gdb
python -m pdb <nomedoprograma.py>

# profiler
python -m profile <nomedoprograma.py>

#exibe um calendario
python -m calendar

# recebe entrada json e imprime
python -m json.tool

# codifica e decodifica um texto em base64
echo 'Hello World' | python -m base64 -e
echo 'SGVsbG8gV29ybGQK' | python -m base64 -d
```


# E mais uma infinidade de outros recursos

```python
# set comprehension
{value for value in something}

# dict comprehension 
{key:value for key,value in something}

# 3/2 agora retorna 1.5 

# notação para numeros em base oito e desesseis
# 0o99 
# 0x44

# Não dá mais pra trolar amigos
True, False = False,True
# SyntaxError: can't assign to keyword

# asyncio
# aqui uma utilização interessante
# http://compiletoi.net/fast-scraping-in-python-with-asyncio.html
```

## Considerações finais
Ainda existem  várias funcionalidades que infelizmente não serão apresentadas neste post devido a extensão do mesmo. Espero que tenham curtido e com o crescimento do numero de bibliotecas com suporte para o python 3, como Django, nltk, numpy e muitas outras, está esperando o que para dar suporte ao python 3 em seu projeto?

[Vamos mergulhar no Python 3?](http://www.diveintopython3.net/) Algumas ferramentas que podem te ajudar:

- [six](http://pythonhosted.org//six/)
- [2to3](https://docs.python.org/2/library/2to3.html)

E se tem duvida sobre suporte de alguma bilbioteca, confira [aqui](https://caniusepython3.com/). 

