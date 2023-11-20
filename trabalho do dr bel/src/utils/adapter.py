import json
import os
import time
from docx import Document
import csv

class Adapter:
    def convert_files_json(self, file):
        with open(f"{file}", "r") as json_file:
            json_data = json.load(json_file)

        text_data = json.dumps(json_data, indent=4)
        file = file[0:-5]
        with open(f"{file}.txt", "w") as txt_file:
            txt_file.write(text_data)

    def convert_files_docx(self, file):
        doc = Document(f"{file}")
        file = file[0:-5]
        with open(f"{file}.txt", "w", encoding="utf-8") as txt_file:
            for para in doc.paragraphs:
                txt_file.write(para.text + "\n")

    def convert_files_csv(self, file):
        with open(f"{file}", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            file = file[0:-4]
            with open(
                f"{file}.txt", "w", newline="", encoding="utf-8"
            ) as txt_file:
                for row in csv_reader:
                    txt_file.write("\t".join(row) + "\n")

    # oi bel nao sei se vai ler isso, eu acredito que se eu usasse o obeserver pra notificar o adapter seria mais eficiente vou tentar fazer aqui caso de tempo eu mando ainda hoje.

    def monitor_directory(self, directory_path, file):
        """ seen_files = set()
        while True:
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if file not in seen_files:
                    seen_files.add(file)
                    file_extension = os.path.splitext(file)[1] """

        if ".json" in file:
            print(f"New text file found: {directory_path}{file}")
            print(file)
            self.convert_files_json(file)
        elif ".csv in file":
            print(f"New CSV file found:  {directory_path}{file}")
            print(file)
            self.convert_files_csv(file)
        elif ".doc" in file:
            print(f"New docx file found:  {directory_path}{file}")
            print(file)
            self.convert_files_docx(file)

        #time.sleep(5)


adapter = Adapter()
if __name__ == "__main__":
    adapter.monitor_directory("files")
