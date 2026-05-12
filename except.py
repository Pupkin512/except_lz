import pandas as pd, main

class Expect:
    def init(self, fp: str, expc: list, expt: dict):
        self.fp = fp
        self.expc = expc
        self.expt = expt
#--------------------------------------------------------------------------------------
    def val(self):
        try:
            self.df = pd.read_csv(self.fp)
        except FileNotFoundError:
            raise ValueError("Файл '{self.fp}' не найден.")
        except pd.errors.EmptyDataError:
            raise ValueError("Файл пуст (нет данных или заголовков).")
        except Exception as e:
            raise ValueError("Ошибка при чтении CSV: {e}")
        if self.df.empty:
            raise ValueError("DataFrame пуст.")
        actual_col = list(self.df.columns)
        if set(actual_col) != set(self.expc):
            miss = set(self.expc) - set(actual_col)
            xtr = set(actual_col) - set(self.expc)
            msg = "Несовпадение колонок."
            if miss:
                msg += " Отсутствуют: {mis}."
            if xtr:
                msg += " Лишние: {ext}."
            raise ValueError(msg)
        for col, expdt in self.expt.items():
            actdt = str(self.df[col].dtype)
            if actdt != expdt:
                raise ValueError("Несовпадение типа в колонке '{col}'. "
                    "Ожидался {expdt}, получен {actdt}.")
        return "Прошел проверку"
if __name__ == "__main__":
    main()