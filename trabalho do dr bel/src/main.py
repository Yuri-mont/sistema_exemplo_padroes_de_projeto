from utils.user_json_handler import UserJsonHandler
from utils.memento import Memento
from utils.facade import Facade
from utils.adapter import Adapter


def menu():
    manipulador_usuarios = UserJsonHandler()
    memento = Memento()
    adapter = Adapter()
    facade  = Facade()
    
    while True:
        print("\n1. Registrar um novo usuário")
        print("2. Ver todos os usuários registrados")
        print("3. Deletar um usuário")
        print("4. Listar arquivos")
        print("5. Apagar um arquivo")
        print("6. Recuperar um arquivo")
        print("7. Importar um arquivo")
        print("8. criar um arquivo")
        print("9. Exportar um arquivo")
        print("10. visualizar um arquivo")
        print("11. Editar um arquivo")
        print("12. Sair")
        
        escolha = input("Digite sua escolha: ")
        
        if escolha == '1':
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            manipulador_usuarios.write_to_json(nome, email, senha)
        elif escolha == '2':
            usuarios = manipulador_usuarios.read_from_json()
            print("\nUsuários lidos do usuarios.json:")
            for usuario in usuarios:
                print(usuario)
        elif escolha == '3':
            email = input("Digite o email do usuário a ser deletado: ")
            senha = input("Digite a senha do usuário a ser deletado: ")
            manipulador_usuarios.delete_user_from_json(email, senha)
        elif escolha == '4':
            memento.print_files('files')

        elif escolha == '5':
            memento.print_files('files')
            file = input("Digite o numero do arquivo: ")
            memento.delete_file(file)

        elif escolha == '6':
            memento.print_files('backup')
            file = input("Digite o numero do arquivo: ")
            memento.restore_file(file)

        elif escolha == '7':
            path = input("Digite o caminho do arquivo desejado: ")
            facade.move_files_to_sistem(path)
            
        elif escolha == '8':
            path = input("Digite o caminho de exportação do arquivo desejado: ")
            facade.move_files_from_sistem(path)

        elif escolha == '9':

            nome = input("Digite o nome do arquivo desejado: ")
            facade.create_file(nome)
        
        elif escolha == '10':
            nome = input("Digite o nome do arquivo desejado: ")
            facade.create_file(nome)

        elif escolha == '11':
            nome = input("Digite o nome do arquivo desejado: ")
            facade.create_file(nome)
        
        elif escolha == '12':
            print("Encerrando o programa.")
            break
        else:
            print("Escolha inválida. Por favor, digite uma opção válida.")

if __name__ == "__main__":
    menu()
    