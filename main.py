pip install docx2pdf
pip install python-docx


from docx2pdf import convert

# Path to the folder containing DOCX files
folder_path = '/path/to/your/folder'

# Convert all DOCX files in the folder to PDF
convert(folder_path)

from docx import Document

def replace_placeholder(doc, placeholder, replacement):
    for p in doc.paragraphs:
        if placeholder in p.text:
            p.text = p.text.replace(placeholder, replacement)

def create_documents(template_path, client_names, output_folder):
    for client_name in client_names:
        # Load the template document
        doc = Document(template_path)

        # Replace the placeholder with the client's name
        replace_placeholder(doc, '{CLIENT_NAME}', client_name)

        # Save the new document
        output_path = f'{output_folder}/{client_name}_contract.docx'
        doc.save(output_path)

if __name__ == '__main__':
    # Path to the template document
    template_path = 'template.docx'

    # List of client names
    client_names = ['Client A', 'Client B', 'Client C']  # Add all your client names here

    # Folder to save the generated documents
    output_folder = 'generated_contracts'

    create_documents(template_path, client_names, output_folder)

# Example block of text
clients_text = """
Client A
Client B
Client C
Client D
"""

# Split the text by new lines and filter out any empty lines
client_names = [name.strip() for name in clients_text.splitlines() if name.strip()]

# Print the list to verify
print(client_names)

