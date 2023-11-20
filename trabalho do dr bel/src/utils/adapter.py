import json
import os
import time
from docx import Document
import csv

class Adapter():
    def convert_files_json(self,file):
        with open(f'{file}', 'r') as json_file:
            json_data = json.load(json_file)

        text_data = json.dumps(json_data, indent=4) 
        file = file[0:-5]
        with open(f'{file}.txt', 'w') as txt_file:
            txt_file.write(text_data)
   

    def convert_files_docx(self,file):
        doc = Document(file)
        file = file[0:-4]
        with open(f'{file}.txt', 'w', encoding='utf-8') as txt_file:
            for para in doc.paragraphs:
                txt_file.write(para.text + '\n')


    def convert_files_csv(self,file):
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            file = file[0:-4]
            with open(f'{file}.txt', 'w', newline='', encoding='utf-8') as txt_file:
                for row in csv_reader:
                    txt_file.write('\t'.join(row) + '\n')
    
    def monitor_directory(self,directory_path):
        seen_files = set()
        while True:
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if file not in seen_files:
                    seen_files.add(file)
                    file_extension = os.path.splitext(file)[1]

                    if file_extension == '.json':
                        print(f"New text file found: {file_path}")
                        self.convert_files_json(file)
                    elif file_extension == '.csv':
                        print(f"New CSV file found:  {file_path}")
                        self.convert_files_csv(file)
                    elif file_extension == '.doc':
                        print(f"New CSV file found:  {file_path}")
                        self.convert_files_docx(file)
            
            time.sleep(5) 