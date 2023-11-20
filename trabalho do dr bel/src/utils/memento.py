import os 
import shutil

class Memento():
    
    def get_files(self,dir):
        directory_path = dir
        files_in_directory = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
        return files_in_directory
    
    def print_files(self,dir):
        contador = 1
        files_in_directory = self.get_files(dir)
        for file in files_in_directory:
            print(f'[{contador}]. {file}')
            contador+=1

    def delete_file(self,filenumber):
        list_files = self.get_files('files')
        file = list_files[int(filenumber) -1]
        shutil.move(file,'backup')
        
    def restore_file(self,filenumber):
        list_files = self.get_files('backup')
        file = list_files[int(filenumber) - 1]
        shutil.move(file,'files')
        
    