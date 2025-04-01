from spire.doc import *
from spire.doc.common import *


# Criando um documento
document = Document() 

# Carregue um arquivo Word DOCX
document.LoadFromFile(r"C:\Users\tabat\Documents\GitHub\conversao_arquivos\PHP e BD.docx") 

# Salve o arquivo em um arquivo PDF
document.SaveToFile( "WordToPdf.pdf" , FileFormat.PDF) 
document.Close()
