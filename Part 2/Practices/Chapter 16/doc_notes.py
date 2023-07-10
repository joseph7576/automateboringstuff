# While PDF files are great for laying out text in a way that’s easy for people to print and read, 
# they’re not straightforward for software to parse into plaintext.

'''PyPDF ( has old version )

general things to do with this packages -> cannot directly edit pdfs: 

- Open one or more existing PDFs (the source PDFs) into PdfFileReader objects.
- Create a new PdfFileWriter object.
- Copy pages from the PdfFileReader objects into the PdfFileWriter object.
- Finally, use the PdfFileWriter object to write the output PDF.
'''

'''python-docx
i used this package sometimes ago hehehe


Creating PDFs from Word Documents
The PyPDF2 module doesn’t allow you to create PDF documents directly, 
but there’s a way to generate PDF files with Python if you’re on Windows and have Microsoft Word installed.
You’ll need to install the Pywin32 package by running pip install pywin32==224. 
With this and the docx module, you can create Word documents and then convert them to PDFs with the following script.
'''

# useful chapter for me!
# not doing the practices tho :/