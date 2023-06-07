
import pandas as pd
import numpy as np


def check_bis_3(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_3', 'BIS_1', 'BIS_2']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_bis_6(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_6', 'BIS_4', 'BIS_5']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_bis_12(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_12', 'BIS_10', 'BIS_11']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_bis_14a(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_14A', 'BIS_3', 'BIS_6', 'BIS_7',
                  'BIS_8', 'BIS_9', 'BIS_12', 'BIS_13']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_bis_15(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_15', 'BIS_14A', 'BIS_14']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_bis_17(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_17', 'BIS_15', 'BIS_16']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_bis_20(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_20', 'BIS_18', 'BIS_19']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_bis_21(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_21', 'BIS_17', 'BIS_20']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[2:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_bis_22(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_21', 'BIS_22', 'BIS_22A']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[2:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_bis_22a(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['BIS_22', 'BIS_22A']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[2:])
    
    return df[default_list + check_list].loc[df['check'] < 0]


if __name__ == '__main__':
    print("This is a module for checking BANK_INCOME_STATEMENT.")
