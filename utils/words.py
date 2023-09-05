import pandas as pd
import random as rd


class Words:
    def __init__(self, path):
        print("CARREGANDO BASE DE PALAVRAS...")
        self.words = pd.read_excel(path)

    def filter_by_size(self, tamanho):
        print(f"FILTRANDO PALAVRAS DE {tamanho} LETRAS...")
        self.words = self.words.query(f"TAMANHO == {tamanho}")
        self._re_index()

    def filter_by_class(self, table_result):
        for index, row in table_result.iterrows():
            if (row["CLASS"] == "wrong") & (
                    table_result.query(f"LETTER == '{row['LETTER']}' & (CLASS == 'right' | CLASS == 'place')").shape[
                        0] == 0):
                self.words = self.words[~self.words["PALAVRA"].str.contains(row["LETTER"])]
                self._re_index()
            elif row["CLASS"] == "place":
                self.words = self.words[(self.words["PALAVRA"].str.contains(row["LETTER"])) & (
                            self.words["PALAVRA"].str[int(row["POSITION"])] != row["LETTER"])]
                self._re_index()
            elif row["CLASS"] == "right":
                self.words = self.words[self.words["PALAVRA"].str[int(row["POSITION"])] == row["LETTER"]]
                self._re_index()

    def new_word(self):
        return self.words.loc[rd.randint(0, self.words.shape[0] - 1), "PALAVRA"]

    def _re_index(self):
        try:
            self.words = self.words.reset_index(drop=True)
        except:
            pass
