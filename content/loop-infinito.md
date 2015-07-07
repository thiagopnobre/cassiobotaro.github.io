Title: Loop Infinito  
Date: 2015-06-27 18:00  
Category: Python  
Tags: python, OO
Slug: loop-infinito  
Author: Cássio Botaro  
Summary: Entendendo o comportamento da linguagem, detectando um problema e apresentando a solução.

![loop](../images/infinite_loop.png
"Loop infinito")

##O problema

Vamos começar analisando o seguinte código:

```python
class Exemplo(object):

    def __init__(self):
        super(Exemplo, self).__init__()
        self.interno = {}

    def __getitem__(self, chave, default=None):
        return self.interno.get(chave, default)

    def __setitem__(self, chave, valor):
        self.interno[chave] = valor
```

Criando uma instância do exemplo e manipulando-a, as coisas parecem legais:

```bash
>>> instancia_exemplo = Exemplo()
>>> instancia_exemplo['chave1'] = 'valor1'
>>> instancia_exemplo['chave2'] = 'valor2'
>>> instancia_exemplo.get('chave1')
    'valor1' 
```

Até que você decide mudar a notação para se recuperar um valor:

```bash
>>> instancia_exemplo['chave1']
    'valor1'
>>> instancia_exemplo['chave3']
>>> instancia_exemplo['chave2']
    'valor2'
```

Opa! Uma chave não existentente não deveria dar um erro?

Se reparar a implemenação de dunder item (`_getitem__`) vai ver que eu tenho um valor default que é retornado quando eu não encontro essa chave e este valor por padrão é None.

Mas tudo bem, quando esta classe foi implementada, talvez essa seja o intuito.

No código onde utilizo essa instancia eu simplesmente verifico se chave passada retorna valor nulo(None).

Mas ai vem um desavisado, e vendo o `__getitem__` na classe decidi itera-la.

```bash
>>> for indice in instancia_exemplo:
...    print indice 
>>>
```
E Pam!

![Pane](../images/panic.gif "Pane no sistema")

Seu programa entra em loop infinito. 

## Como funciona o Python em termos de iteração?

Vamos  começar por conceitos. Iterável, é tudo aquilo que pode ser percorrido, não confunda com iterador que é um padrão de projeto. Em Python, listas, tuplas, geradores e dicionarios podem ser percorridos.

Mas como posso definir para o interpretador que algo pode ser percorrível?

Algo que pode ser percorrível em Python, possui uma função `__iter___` que retorna um iterador. Um iterador é um padrão de projeto aplicado em containers e seguem um protocolo para este container ser percorrido.

Uma outra opção é  a existência da função `__getitem__` **que aceite itens numéricos e lançam IndexError indicando que o percurso foi finalizado**.

Dito isso já dá pra se ter uma idéia do que aconteceu em nosso código. Quando o laço de repetição(for) foi iniciado o interpretador tentou atribuir exaustivamente valores de 0..n para `__getitem__` que continuava responder None e nenhuma exceção foi lançada.

## A solução

Não há solução, porque não é um problema, apenas uma confusão causada sobre interpretação de iteráveis.

Porém analisando o código acima, acho que o grande problema neste código é a tentiva de suprimir uma exceção. Para casos em que isto ocorre o proprio dicionário já nos fornece um método chamado `get`.

É até dificil falar que a solução é o metódo get, pois este exemplo também nos faz pensar sobre a classe Exemplo que é basicamente um dicionário e caso algum estado ou ação seja adicionado ao objeto, talvez uma melhor reescrita seria através de herança.   

## Moral da história

Seja cuidadoso ao reescrever os `special methods`, lembrem-se que o maquinário para a execução destes métodos está presente no interpretador e que existe um protocolo estabelecido.

Lembre-se também que suprimir exceções podem fazer com que erros sejam silenciados e isto não é pythônico.

## Créditos

Este post só se tornou possível após consulta de duas fontes:

[Resposta do Alex Martelli](http://stackoverflow.com/questions/926574/why-does-defining-getitem-on-a-class-make-it-iterable-in-python)

[Palestra do Luciano Ramalho](https://www.youtube.com/watch?v=ULj7ejvuzI8)


