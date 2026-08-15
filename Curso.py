alunos = []
curso = ("desenvolvimento Web III","FATEC")
disciplinas = set()
turma = ("Ciclo III",2026)

def cadastrar_aluno(nome,idade,cidade):
    aluno = {
        "nome":nome,
        "idade":idade,
        "cidade":cidade,
        "notas":[]
        }
    alunos.append(aluno)
    print("Aluno Cadastrado")
    
def registrar_nota(aluno, nota):
    if aluno in alunos:
        aluno["notas"].append(nota)
    else:
        print("Aluno não encontrado")

def calcular_media(aluno):
    if aluno in alunos:
        if len(aluno["notas"]) > 0:
            media = sum(aluno["notas"]) / len(aluno["notas"])

            if media >= 6:
                print(f"Média: {media:.2f}\nAluno Aprovado")
            else:
                print(f"Média: {media:.2f}\nAluno Reprovado")
        else:
            print("Aluno ainda não possui notas.")
    else:
        print("Aluno não encontrado")

def listar_alunos():
    if alunos:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Cidade: {aluno['cidade']}")
            print(f"Notas: {aluno['notas']}")
            print("--------------------")
    else:
        print("Nenhum aluno cadastrado.")
        
def cadastrar_disciplina(disciplina):
    disciplinas.add(disciplina)
        
def listar_disciplinas():
    if disciplinas:
        print("Disciplinas cadastradas:")

        for disciplina in disciplinas:
            print(f"- {disciplina}")
    else:
        print("Nenhuma disciplina cadastrada.")
        
def informacoes_turma():
    print(f"Turma: {turma[0]}")
    print(f"Ano: {turma[1]}")
    print(f"Curso: {curso[0]}")
    print(f"Instituição: {curso[1]}")

    print("\nDisciplinas:")
    listar_disciplinas()
    
