import os
import shutil
from time import strftime
from sys import platform
from shutil import which

def n_files(directory):
    """Count the number of .doc, .docx, and .tmd files in a directory."""
    return sum(1 for file in os.listdir(directory) if file.endswith(('.doc', '.docx', '.tmd')))

def doc2pdf_libreoffice(doc, ending):
    """Convert documents to PDF using LibreOffice."""
    cmd = f"lowriter --convert-to pdf:writer_pdf_Export '{doc}'"
    os.system(cmd)
    new_file = doc.replace(ending, ".pdf")

    if os.path.exists(new_file):
        print(f"Converted: {new_file}")
    else:
        print(f"Failed to convert: {doc}")

def is_tool(name):
    """Check if a tool is installed and available."""
    return which(name) is not None

if __name__ == "__main__":
    print("\nPlease note that this will overwrite any existing PDF files")
    print("For best results, close Microsoft Word before proceeding\n")
    
    directory = os.getcwd()

    if n_files(directory) == 0:
        print("No files found for conversion.")
        exit()

    print("Starting conversion...\n")

    try:
        if not is_tool("libreoffice"):
            try:
                from win32com import client
                word = client.DispatchEx("Word.Application")
                word.Visible = False  # Run Word in the background
            except Exception as e:
                print(f"Microsoft Word COM error: {e}")
                exit()

        for file in os.listdir(directory):
            if file.endswith(('.doc', '.docx', '.tmd')):
                ending = os.path.splitext(file)[1]
                in_file = os.path.abspath(os.path.join(directory, file))

                if is_tool("libreoffice"):
                    doc2pdf_libreoffice(in_file, ending)
                else:
                    new_name = file.replace(ending, ".pdf")
                    new_file = os.path.join(directory, new_name)

                    try:
                        doc = word.Documents.Open(in_file)
                        doc.SaveAs(new_file, FileFormat=17)
                        doc.Close()
                        print(f"Converted: {new_name}")
                    except Exception as e:
                        print(f"Error converting {file}: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    print("\nConversion finished at " + strftime("%H:%M:%S"))
