import pandas as pd
import numpy as np


def check_sis_1(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_1', 'SIS_1_1', 'SIS_1_2', 'SIS_1_3']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_20(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_20', 'SIS_1', 'SIS_2', 'SIS_4',
                  'SIS_5', 'SIS_6', 'SIS_7_1', 'SIS_7_2',
                  'SIS_8', 'SIS_8_1', 'SIS_9', 'SIS_9_1',
                  'SIS_9_2', 'SIS_10', 'SIS_11']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_11_2(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_11_2', 'SIS_20', 'SIS_11_1']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_21(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_21', 'SIS_21_1', 'SIS_21_2', 'SIS_21_3']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_40(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_40', 'SIS_21', 'SIS_22', 'SIS_22_1',
                  'SIS_23', 'SIS_24', 'SIS_25', 'SIS_26',
                  'SIS_27', 'SIS_28', 'SIS_29', 'SIS_29_1',
                  'SIS_30', 'SIS_31', 'SIS_32']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_50_1(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_50_1', 'SIS_11_2', 'SIS_40']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_50(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_50', 'SIS_41', 'SIS_42', 'SIS_43',
                  'SIS_44']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_60(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_60', 'SIS_51', 'SIS_52', 'SIS_53',
                  'SIS_54', 'SIS_55']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_70(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_70', 'SIS_50_1', 'SIS_50', 'SIS_60',
                  'SIS_56', 'SIS_61', 'SIS_62']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_80(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_80', 'SIS_71', 'SIS_72']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_90(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_90', 'SIS_70', 'SIS_80']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_90_sub_items(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_90', 'SIS_91', 'SIS_92']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_200(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_200', 'SIS_201', 'SIS_202', 'SIS_203']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_400(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_400', 'SIS_203_1', 'SIS_301', 'SIS_302', 
                  'SIS_303', 'SIS_304', 'SIS_305', 'SIS_306', 
                  'SIS_307']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sis_400_sub_items(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SIS_400', 'SIS_401', 'SIS_402']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


if __name__ == '__main__':
    print("This is a module for checking SECURITY_INCOME_STATEMENT")


