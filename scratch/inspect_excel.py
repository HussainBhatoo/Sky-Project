import openpyxl
import json

path = r"c:\Study\Uni\Sem 2\Group project\CW_2\sky-team-registry\only_for_to_read_context_no_github_push\Agile Project Module UofW - Team Registry.xlsx"
wb = openpyxl.load_workbook(path, data_only=True)
sheet = wb.active

headers = [cell.value for cell in sheet[1]]
rows = []
for row in sheet.iter_rows(min_row=2, max_row=50, values_only=True):
    if any(row):
        rows.append(row)

print("Headers:", headers)
for row in rows[:5]:
    print(row)
