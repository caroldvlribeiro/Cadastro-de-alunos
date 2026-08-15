# Sistema de Cadastro de Alunos — Desenvolvimento Web III

## 📚 Sobre o projeto

Este projeto foi desenvolvido como atividade da disciplina **Desenvolvimento Web III**, com o objetivo de colocar em prática os principais tipos de coleções da linguagem **Python**:

* **Lista (`list`)**
* **Tupla (`tuple`)**
* **Conjunto (`set`)**
* **Dicionário (`dict`)**

O sistema permite realizar o cadastro de alunos, registrar notas, calcular médias, cadastrar disciplinas e consultar informações da turma por meio de um menu interativo.

## 🎯 Objetivos

* Praticar a utilização de diferentes tipos de coleções em Python.
* Criar um sistema de cadastro utilizando listas e dicionários.
* Armazenar múltiplas notas para cada aluno.
* Calcular a média e verificar a situação do aluno.
* Utilizar `set` para evitar disciplinas duplicadas.
* Utilizar tuplas para armazenar informações fixas.
* Trabalhar com funções, estruturas condicionais e estruturas de repetição.

## ⚙️ Funcionalidades

### 👨‍🎓 Cadastro de alunos

Permite cadastrar:

* Nome;
* Idade;
* Cidade;
* Notas.

Os alunos são armazenados em uma **lista**, enquanto as informações individuais de cada aluno são organizadas em um **dicionário**.

Exemplo:

```python
aluno = {
    "nome": "Carol",
    "idade": 20,
    "cidade": "Praia Grande",
    "notas": []
}
```

### 📋 Listagem de alunos

Exibe todos os alunos cadastrados e suas respectivas informações, incluindo as notas registradas.

### 📝 Registro de notas

Permite adicionar uma ou mais notas para um aluno.

As notas são armazenadas em uma **lista dentro do dicionário do aluno**.

### 📊 Cálculo da média

O sistema calcula a média das notas cadastradas para um aluno.

A situação é definida da seguinte forma:

* Média **maior ou igual a 6** → Aprovado;
* Média **menor que 6** → Reprovado.

### 📖 Cadastro de disciplinas

As disciplinas são armazenadas utilizando um **conjunto (`set`)**.

Essa estrutura impede que a mesma disciplina seja cadastrada mais de uma vez.

```python
disciplinas = set()
```

### 📚 Listagem de disciplinas

Exibe todas as disciplinas cadastradas no sistema.

### 🏫 Informações da turma

O sistema também armazena informações fixas utilizando **tuplas**:

```python
curso = ("Desenvolvimento Web III", "FATEC")
turma = ("Ciclo III", 2026)
```

Essas informações não precisam ser alteradas durante a execução do programa.

### 🚪 Encerramento

O menu possui uma opção para encerrar a execução do sistema.

## 🖥️ Menu do sistema

```text
===== SISTEMA ACADÊMICO =====
1 - Cadastrar Aluno
2 - Registrar Nota
3 - Calcular Média
4 - Listar Alunos
5 - Cadastrar Disciplina
6 - Listar Disciplinas
7 - Informações da Turma
8 - Sair
```

## 🗂️ Estrutura do projeto

O projeto é dividido em dois arquivos principais:

```text
📁 projeto/
│
├── 📄 curso.py
└── 📄 main.py
```

### `curso.py`

Responsável pelos:

* Dados do sistema;
* Cadastro de alunos;
* Registro de notas;
* Cálculo de médias;
* Listagem de alunos;
* Cadastro de disciplinas;
* Listagem de disciplinas;
* Informações da turma.

### `main.py`

Responsável pelo:

* Menu principal;
* Interação com o usuário;
* Recebimento das opções;
* Execução das funções do arquivo `curso.py`;
* Controle do loop do programa.

## 🧩 Coleções utilizadas

| Coleção | Utilização                                      |
| ------- | ----------------------------------------------- |
| `list`  | Armazenar os alunos e as notas                  |
| `dict`  | Armazenar as informações de cada aluno          |
| `set`   | Armazenar disciplinas sem duplicação            |
| `tuple` | Armazenar informações fixas do curso e da turma |

## ▶️ Como executar

É necessário ter o **Python** instalado.

Clone ou baixe o projeto e, dentro da pasta, execute:

```bash
python main.py
```

O sistema exibirá o menu principal e poderá ser utilizado através das opções apresentadas.

## 🛠️ Tecnologias utilizadas

* **Python 3**
* Listas
* Tuplas
* Conjuntos
* Dicionários
* Funções
* Estruturas condicionais
* Estrutura de repetição `while`

## 👩‍💻 Autora

**Carol**

Projeto desenvolvido para a disciplina **Desenvolvimento Web III — FATEC**.
