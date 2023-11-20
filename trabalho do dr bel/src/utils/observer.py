import hashlib
import json
import os
import time

from adapter import Adapter

class Observer:
    directory_path = 'files'
    hashes_file = 'file_hashes.json'
    adapter = Adapter()
    @staticmethod
    def send_email(self,email, arquivo):
        print(f'Olá portador do email {email} o arquivo {arquivo} foi alterado.\nIsso é um email real não um print\n')

    # Function to calculate file hash
    def get_file_hash(self,file_path):
        with open(file_path, 'rb') as file:
            file_hash = hashlib.md5()
            while chunk := file.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()

    def observador(self):
        if not os.path.exists(self.hashes_file):
            initial_hashes = {}
        else:
            with open(self.hashes_file, 'r') as json_file:
                initial_hashes = json.load(json_file)

        while True:
            files_in_directory = [os.path.join(self.directory_path, file) for file in os.listdir(self.directory_path) if os.path.isfile(os.path.join(self.directory_path, file))]
            
            new_files = [file for file in files_in_directory if file not in initial_hashes]
            for new_file in new_files:
                initial_hashes[new_file] = self.get_file_hash(new_file)
                self.adapter.monitor_directory('files',new_file)
            
            deleted_files = [file for file in initial_hashes if file not in files_in_directory]
            for deleted_file in deleted_files:
                del initial_hashes[deleted_file]
                print(f"Arquivo '{deleted_file}' foi excluido.")

            for file_path in initial_hashes:
                current_hash = self.get_file_hash(file_path)
                if current_hash != initial_hashes[file_path]:
                    try:
                        with open('usuarios.json', 'r') as file:
                            users = json.load(file)
                    except Exception as e:
                        print(f"ERRO: {e}")
                    for user in users:
                        self.send_email(self,user['email'], arquivo= file_path)
                    initial_hashes[file_path] = current_hash

            # Update the JSON file with the new hashes
            with open(self.hashes_file, 'w') as json_file:
                json.dump(initial_hashes, json_file, indent=4)

            time.sleep(2)

observer = Observer()
observer.observador()