import json

class UserJsonHandler:
    def write_to_json(self, nome, email, senha):
        user_data = {
            "nome": nome,
            "email": email,
            "senha": senha
        }
        
        try:
            with open('usuarios.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []
       
        user_emails = [user['email'] for user in users]
        if email in user_emails:
            print(f"Usuario de '{email}' já é cadastrado.")
            return
        users.append(user_data)
        
        try:
            with open('usuarios.json', 'w') as file:
                json.dump(users, file, indent=2)
            print("Usuario cadastrado!")
        except Exception as e:
            print(f"ERRO: {e}")

    def read_from_json(self):
        try:
            with open('usuarios.json', 'r') as file:
                users = json.load(file)
            return users
        except Exception as e:
            print(f"ERRO: {e}")
            return []
    def delete_user_from_json(self,email,senha):
        try:
            with open('usuarios.json', 'r') as file:
                usuarios = json.load(file)
        except FileNotFoundError:
            usuarios = []
            
        usuarios_atualizados = [usuario for usuario in usuarios if usuario['email'] != email or usuario['senha'] != senha ] 
        if len(usuarios) == len(usuarios_atualizados):
            print(f"Usuário com o email '{email}' e senha fornecida não encontrado.")
        else:
            try:
                with open('usuarios.json', 'w') as file:
                    json.dump(usuarios_atualizados, file, indent=2)
                print(f"Usuário com o email '{email}' foi removido.")
            except Exception as e:
                print(f"ERRO: {e}")
    

        