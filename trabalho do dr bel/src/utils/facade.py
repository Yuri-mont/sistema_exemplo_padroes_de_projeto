import os
import shutil
from memento import Memento
class Facade():
    memento = Memento()

    def create_file(self,nome):
        with open(f'files/{nome}.txt','w') as file:
            file.close
    
    def edit_Document(self,nome,content):#fazer funfar
        with open(f'files/{nome}.txt','+a') as file:
            lines = file.readlines()
            for line in lines:
                print(f'[{lines.index(line)}].{line}')
            file.close


    def inspect_Document(self,nome):
        with open(f'files/{nome}.txt','r') as file:
            lines = file.readlines()
            file.close
        for line in lines:
            print(line)

    def move_files_to_sistem(self,caminho):
        if '.txt' in caminho or '.csv' in caminho or '.json' in caminho:
             shutil.move(f'/{caminho}','files')
        else:
            return 'Arquivo com extensão nao permitida no sistema'
    
    def move_files_from_sistem(self,caminho):
        lista = Facade.memento.get_files(self,'files')
        for i in lista:
            print(f'[{lista.index(i)}].{i}')
        try:
            numero = input("Digite o numero do arquivo: ")
            arquivo = lista[int(numero) -1]
            if 'nome':
             shutil.move(f'{caminho}/{arquivo}','files')
            else:
                return 'Arquivo com extensão nao permitida no sistema'
        except ValueError:
            print('Insira um valor int existente')
        

    
    
