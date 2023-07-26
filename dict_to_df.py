import pandas as pd

def dict_to_df(dict_qs, mode_type):
    dict_qs = pd.DataFrame.from_dict(dict_qs, orient='index').reset_index(level=0)
    dict_qs.columns = [f'{mode_type}', 'ID']
    return dict_qs