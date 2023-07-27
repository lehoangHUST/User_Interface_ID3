import pandas as pd
import logging 
from utils.general import check_exits, makedirs_folder


"""     
    File to prerocessing dataset:
        - Dataset Weather
        - Dataset Tic-Tac
        - ........
"""

class Data_CSV:
    def __init__(self, file_csv, index_col):
        try:
            exist = check_exits(file_csv)
            if exist:
                self.df = pd.read_csv(file_csv, index_col = index_col, parse_dates = True)
            else:
                self.df = None
                raise Exception
        except Exception as err:
                logging.error(f"{file_csv} not found.")


    def preprocessing_data(self):
        """
            Split data to X_train and Y_train (Y_train is label)
        """
        if self.df is not None:
            X_train, Y_train = self.df.iloc[:, :-1], self.df.iloc[:, -1]
            return X_train, Y_train
        else:
            return None, None
        

    def get_attributes(self):
        cols = {}
        features, label = {}, {}
        if self.df is not None:
            for name_col in self.df.columns:
                cols[name_col] = list(self.df[name_col].unique())
        # Split label and features
        for idx, (key, value) in enumerate(cols.items()):
            if idx ==  len(cols) - 1:
                label[key] = value
            else:
                features[key] = value
        return features, label


class Weather(Data_CSV):
    def __init__(self, file_csv, index_col):
        super().__init__(file_csv, index_col)
    

    def preprocessing_data(self):
        return super().preprocessing_data()
        

    def get_attributes(self):
        return super().get_attributes()


class Tic_Tac_Toe(Data_CSV):
    def __init__(self, file_csv, index_col):
        super().__init__(file_csv, index_col)
        # self.save_csv()

    
    def preprocessing_data(self):
        return super().preprocessing_data()


    def get_attributes(self):
        return super().get_attributes()


    def save_csv(self):
        """
            Format csv
        """
        n_df = {
            'id': [i for i in range(1, len(self.df) + 1)]
        }
        if self.df is not None:
            name_columns = self.df.columns.to_list()
            for idx, name_col in enumerate(name_columns):
                n_df[name_col] = self.df.iloc[:, idx]
        
        df = pd.DataFrame(n_df)
        df.to_csv('tic-tac-toe.csv', index=False)