import tabula
import pandas as pd
import os
def extract_table_from_pdf(pdf_dir: str, pages: str ='all', save_path: str = 'csv/2022.csv'):
    all_pdfs = os.listdir(pdf_dir)
    all_pdfs.sort()
    transactions_df = pd.DataFrame(columns=['Date',	'Time',	'Descriptions',	'Channel',	'Amount',	'Balance',	'Details'])
    for pdf in all_pdfs:
        pdf_path = '/'.join([pdf_dir, pdf])
        df = tabula.read_pdf(pdf_path, pages=pages, silent=True)
        df.reverse()
        for page in df:
            page = page.iloc[::-1]
            page.replace('\r', ' ', regex=True, inplace=True)
            transactions_df = transactions_df.append(page, ignore_index=True)
    transactions_df.to_csv('csv/2022_FNC_Statement.csv', index=True)

if __name__ == '__main__':
    extract_table_from_pdf('pdf/')