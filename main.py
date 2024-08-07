import os
from docx import Document
from config import *
from docx2pdf import convert



def replace_placeholder(doc, placeholder, replacement):
    for p in doc.paragraphs:
        if placeholder in p.text:
            p.text = p.text.replace(placeholder, replacement)

def create_documents(template_path, client_names, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for client_name in client_names:
        doc = Document(template_path)
        replace_placeholder(doc, '{2}', client_name)
        replace_placeholder(doc, '{1}', 'August 7th, 2024')
        replace_placeholder(doc, '{3}', '8/7/2024')

        output_path = os.path.join(output_folder, f'{client_name}_contract.docx')
        print(f'Saving file to {output_path}')  # Debug print
        doc.save(output_path)



if __name__ == '__main__':
    # Path to the template document


    # List of client names
    #client_names = ['Client A', 'Client B', 'Client C']  # Add all your client names here

    # Folder to save the generated documents
    clients_text = """
    4th Ave Loft Corp
    130 Hicks Street Owners Inc
    215 East 29th St Corp
    558 West 150th Street Condominium
    """

    # Split the text by new lines and filter out any empty lines
    client_names = [name.strip() for name in clients_text.splitlines() if name.strip()]

    # Print the list to verify
    # print(client_names)

    create_documents(template_path, client_names, output_folder)
    convert(folder_path)

# Example block of text

