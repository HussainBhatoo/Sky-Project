import openpyxl
import os

def audit_excel(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    print(f"Auditing Original Excel: {os.path.basename(file_path)}\n")
    
    try:
        workbook = openpyxl.load_workbook(file_path, data_only=True)
        # Check all sheets
        for sheet_name in workbook.sheetnames:
            print(f"--- Sheet: {sheet_name} ---")
            sheet = workbook[sheet_name]
            
            # Assume first row is header
            rows = list(sheet.rows)
            if not rows:
                continue
                
            headers = [cell.value for cell in rows[0]]
            print(f"Headers: {headers}")
            
            # Print sample data (first 3 rows)
            for i, row in enumerate(rows[1:4], start=2):
                print(f"Sample Row {i}: {[cell.value for cell in row]}")
            
            # Find column indices specifically for 'Team Leader' and 'Department Head'
            team_col = None
            leader_col = None
            head_col = None
            
            for i, h in enumerate(headers):
                if not h: continue
                h_lower = str(h).lower()
                if 'team' in h_lower and 'name' in h_lower:
                    team_col = i
                if h_lower == 'team leader':
                    leader_col = i
                if h_lower == 'department head':
                    head_col = i
            
            if team_col is not None:
                gaps = []
                for row_idx, row in enumerate(rows[1:], start=2):
                    team_val = row[team_col].value
                    leader_val = row[leader_col].value if leader_col is not None else 'N/A'
                    head_val = row[head_col].value if head_col is not None else 'N/A'
                    
                    if team_val:
                        if leader_col is not None and not leader_val:
                            gaps.append(f"Row {row_idx}: Team '{team_val}' has no Team Leader.")
                        if head_col is not None and not head_val:
                            gaps.append(f"Row {row_idx}: Team '{team_val}' has no Department Head.")
                
                if gaps:
                    for g in gaps:
                        print(f"[GAP FOUND] {g}")
                else:
                    print("No management gaps detected (Team Leaders & Dept Heads are all present).")
            else:
                print("Could not identify Team column.")
            print("\n")
            
    except Exception as e:
        print(f"Failed to audit: {str(e)}")

# Path to the original registry
excel_path = r"c:\Study\Uni\Sem 2\Group project\CW_2\sky-team-registry\only_for_to_read_context_no_github_push\Agile Project Module UofW - Team Registry.xlsx"
audit_excel(excel_path)
