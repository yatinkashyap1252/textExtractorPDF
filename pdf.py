import fitz  # PyMuPDF

def pdf_to_text(pdf_path, txt_path):
   
    pdf_document = fitz.open(pdf_path)

   
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        
        for page_num in range(len(pdf_document)):
          
            page = pdf_document.load_page(page_num)
            
            text = page.get_text()
           
            txt_file.write(text)

    print(f"Text extracted and saved to {txt_path}")


pdf_path = 'ipdc.pdf' 
txt_path = 'ipdc_text.txt' 
pdf_to_text(pdf_path, txt_path)