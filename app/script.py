import time

from data_workers.main_classes.extractor import Extractor
from data_workers.main_classes.transformer import Transformer
from data_workers.main_classes.writer import Writer


class Trans(Transformer):
    def __init__(self):
        pass

    def filter(self, data_frame, key, value):
        new_df = []
        for row in data_frame:
            if row[key] == value:
                new_df.append(row)
        return new_df

    def delete(self, data_frame, key, value):
        new_df = []
        for row in data_frame:
            if row[key] != value:
                new_df.append(row)
        return new_df

    def add(self, data_frame, key, value):
        for row in data_frame:
            row[key] = value
        return data_frame


class Batia:
    def __init__(self):
        self.writer = Writer()
        self.extractor = Extractor()
        self.trans = Trans()

    def test(self):
        # executor
        df = self.extractor.get_data_msq()
        # writer
        print(df)
        self.writer.create_json(df)
        self.writer.create_csv(df)
        # worker
        a = self.trans.filter(data_frame=df, key='id_code', value='41261')
        b = self.trans.delete(data_frame=df, key='id_code', value='41261')
        df = self.trans.add(df, 'created_at', time.time())
        self.writer.create_json(df)
        self.writer.create_csv(df)


if __name__ == '__main__':
    Batia().test()
