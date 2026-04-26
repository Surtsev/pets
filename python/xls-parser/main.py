import sys
import os
import pandas as pd

def main(file_path: str):
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist or incorrect path. Returning...")
        return 
    df = pd.read_excel(file_path)

    df_str = df.astype(str)

    result = df_str.values.tolist()
    for i,row in enumerate(result):
        print(f"{i}: {row}")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        main(file_path)
    else:
        print("Пожалуйста, укажите путь к файлу Excel")
        print("Пример: python main.py '/путь/к/файлу.xlsx'")
