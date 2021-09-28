import os
from openpyxl import load_workbook

def load_spreadsheet():
  os.chdir(os.getenv('LOCATION'))
  wb = load_workbook(os.getenv('EXCEL_FILE'))
  sheet = wb.get_sheet_by_name('Sheet 1')
  return { 'wb': wb, 'sheet': sheet }

def save_spreadsheet(wb):
  wb.save(os.getenv('EXCEL_FILE_NEW'))
  print('Done')
  return