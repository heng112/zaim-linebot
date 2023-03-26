import sqlite3
import pandas as pd
import os

def req_input(input_str : str)-> list:
    
    conn = sqlite3.connect('../db/zaim.db')
    df = pd.read_sql(get_guery(shohin=input_str, filename="shohin.sql"), conn)
    result = df.to_dict(orient='records')
    return result


def get_guery(shohin: str, filename: str)->str:
    """
    SQLファイルに変数を挿入してクエリを作成する

    Args:
        num (int): 年齢
        category (str): 好きな果物
        filename (str): SQLファイルの名前

    Returns:
        str: SQLクエリ
    """
    with open(os.path.join("./", filename), "r") as f:
        return f.read().format(shohin=shohin)

    
