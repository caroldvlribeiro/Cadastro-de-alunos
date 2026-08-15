import curso

while True:
        print("\n===== SISTEMA ACADÊMICO =====")
        print("1 - Cadastrar Aluno")
        print("2 - Registrar Nota")
        print("3 - Calcular Média")
        print("4 - Listar Alunos")
        print("5 - Cadastrar Disciplina")
        print("6 - Listar Disciplinas")
        print("7 - Informações da Turma")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("Cadastrar Aluno:")
            nome = input("Nome do aluno:")
            idade = input("Idade do aluno:")
            cidade = input("Cidade do aluno:")
            curso.cadastrar_aluno(nome,idade,cidade)
            
        elif opcao == "2":
            print("Registrar nota")
            aluno = input("Aluno:")
            nota = int(input("Nota:"))
            curso.registrar_nota(aluno,nota)
            
        elif opcao == "3":
            print("Calcular Media do Aluno:")
            aluno = input("Aluno:")
            curso.calcular_media(aluno)
        
        elif opcao == "4":
            print("Listar Alunos Cadastrados:")
            curso.listar_alunos()
            
        elif opcao == "5":
            print("Cadastrar Disciplina:")
            disciplina = input("Nova disciplina:")
            curso.cadastrar_disciplina(disciplina)
            
        elif opcao == "6":
            print("Listar Disciplinas:")
            curso.listar_disciplinas()
        
        elif opcao == "7":
            print("Informações da Turma:")
            curso.informacoes_turma()
        
        elif opcao == "8":
            print("Saindo do Sistema")
            break
        
        else:
            print("Opção Invalida")


