# excel_helper.py
import os
import pandas as pd

def manage_excel(data, folder_path, file_name, sheet_name="Sheet1", mode="overwrite"):
    """
    Automates Excel management: Creates folders, handles paths, and safely
    saves data based on your chosen mode ('overwrite' or 'append').
    """
    # 1. Handle paths and directories automatically
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"📁 Created folder: {folder_path}")
        
    excel_filepath = os.path.join(folder_path, file_name)
    df = pd.DataFrame(data)
    
    # 2. OVERWRITE MODE: Wipes the file or creates a clean fresh copy
    if mode == "overwrite":
        df.to_excel(excel_filepath, sheet_name=sheet_name, index=False)
        print(f"🔄 Overwrote/Created clean file at: {excel_filepath}")
        
    # 3. APPEND MODE: Seamlessly glues data to the bottom in real-time
    elif mode == "append":
        if os.path.exists(excel_filepath):
            with pd.ExcelWriter(
                excel_filepath, 
                engine="openpyxl", 
                mode="a", 
                if_sheet_exists="overlay"
            ) as writer:
                start_row = writer.sheets[sheet_name].max_row
                df.to_excel(
                    writer, 
                    sheet_name=sheet_name, 
                    index=False, 
                    header=False, 
                    startrow=start_row
                )
            print(f"➕ Appended new rows to existing file at: {excel_filepath}")
        else:
            # Fallback if file doesn't exist yet
            df.to_excel(excel_filepath, sheet_name=sheet_name, index=False)
            print(f"🆕 File didn't exist. Created clean file at: {excel_filepath}")
            
    return excel_filepath
