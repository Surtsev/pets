import sys
import os
import pandas as pd
import datetime as dt
from enum import Enum


class Days(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


def main(file_path: str):
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist or incorrect path. Returning...")
        return
    df = pd.read_excel(file_path)

    df_str = df.astype(str)

    result = df_str.values.tolist()
    now = dt.datetime.now()
    print(now.weekday())
    print(now)
    for i, row in enumerate(result):
        print(f"{i}: {row}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        main(file_path)
    else:
        print("Пожалуйста, укажите путь к файлу Excel")
        print("Пример: python main.py '/путь/к/файлу.xlsx'")
