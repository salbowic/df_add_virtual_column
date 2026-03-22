import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # Check new_column validity
    if not re.match(r'^[a-zA-Z_]+$', new_column):
        return pd.DataFrame([])
    
    # Check if role contains only allowed characters: letters, underscores, spaces, numbers, dots, +, -, *
    if not re.match(r'^[a-zA-Z0-9_\.\s\+\-\*]+$', role):
        return pd.DataFrame([])
    
    # Extract variables from role
    vars_in_role = re.findall(r'[a-zA-Z_]+', role)
    for v in vars_in_role:
        if v not in df.columns:
            return pd.DataFrame([])
            
    # Check if any column label is incorrect
    for col in df.columns:
        if not re.match(r'^[a-zA-Z_]+$', str(col)):
            return pd.DataFrame([])

    # evaluate
    try:
        new_result = df.eval(role)
        df_new = df.copy()
        df_new[new_column] = new_result
        return df_new
    except Exception:
        return pd.DataFrame([])

