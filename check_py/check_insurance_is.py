import pandas as pd
import numpy as np


def check_iis_01(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_01', 'IIS_011', 'IIS_012', 'IIS_013']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_02(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_02', 'IIS_021', 'IIS_022', 'IIS_023', 'IIS_024']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_04(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_04', 'IIS_041', 'IIS_042']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_042(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_042', 'IIS_043', 'IIS_044', 'IIS_045']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_03(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_03', 'IIS_02', 'IIS_01']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_10(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_10', 'IIS_03', 'IIS_04', 'IIS_023', 'IIS_024']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_112(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_112', 'IIS_121', 'IIS_122', 'IIS_123']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_126(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_126', 'IIS_13', 'IIS_14']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_171(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_171', 'IIS_172', 'IIS_173', 'IIS_174',
                  'IIS_175', 'IIS_176', 'IIS_177', 'IIS_178']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_17(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_17', 'IIS_171', 'IIS_179', 'IIS_1710',
                  'IIS_1711']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_15(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_15', 'IIS_124', 'IIS_125']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_18(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_18', 'IIS_15', 'IIS_161', 'IIS_162',
                  'IIS_17']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_19(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_19', 'IIS_10', 'IIS_18']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_192(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_192', 'IIS_202', 'IIS_212']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_193(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_193', 'IIS_203', 'IIS_213']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_26(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_26', 'IIS_261', 'IIS_262', 'IIS_263']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_301(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_301', 'IIS_302', 'IIS_303']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_24(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_24', 'IIS_22', 'IIS_23', 'IIS_306']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_iis_40(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['IIS_40', 'IIS_31', 'IIS_32']
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    return df[default_list + check_list].loc[df['check'] != 0]


if __name__ == '__main__':
    print("This is a module for checking INSURANCE_INCOME_STATEMENT")


