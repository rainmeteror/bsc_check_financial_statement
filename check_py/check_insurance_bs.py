import pandas as pd
import numpy as np


def check_ibs_110(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IBS_110', 'IBS_111', 'IBS_112']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ibs_120(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IBS_120', 'IBS_121', 'IBS_129', 'IBS_1291']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


if __name__ == '__main__':
    print("This is a module for checking INSURANCE_BALANCE_SHEET")




