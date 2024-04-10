import json
import os

def extract_content_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        content_list = []

        for item in data.get('library', []):
            # Extrahiert Text aus HTML-Elementen
            if item.get('type') == 'text' and 'html' in item:
                content_list.append(item['html'])
            # Für Multiple-Choice-Elemente
            elif item.get('type') == 'multiplechoice' and 'items' in item:
                for sub_item in item['items']:
                    content_list.append(sub_item['html'])

        return content_list

def extract_from_all_files(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    content = extract_content_from_json(file_path)
                    # Schreibt den extrahierten Inhalt in die zentrale .txt-Datei
                    for line in content:
                        f.write(line + '\n')
                    f.write('\n')  # Fügt eine Leerzeile zwischen den Inhalten der Dateien hinzu
                    print(f"Inhalte aus {file} extrahiert und zu {output_file} hinzugefügt.")

def main():
    directory = r'C:\Users\mausz\OneDrive\Desktop\Bachelorarbeit\Unterlagen\Inhalt_Datasource\to_konvert\EASY_BUSINESS_-_Wirtschaftsrecht\content'
    output_file = r'C:\Users\mausz\OneDrive\Desktop\Bachelorarbeit\Unterlagen\Inhalt_Datasource\Zusammengefasste_Inhalte_Wirtschaftsrecht.txt'
    extract_from_all_files(directory, output_file)

if __name__ == "__main__":
    main()
