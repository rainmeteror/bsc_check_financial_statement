
import pandas as pd
import numpy as np


# Cashflow Direct
def check_ccfd_20(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFD_20', 'CCFD_1A', 'CCFD_1', 'CCFD_2',
                  'CCFD_3', 'CCFD_4', 'CCFD_5', 'CCFD_6', 
                  'CCFD_7']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ccfd_30(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFD_30', 'CCFD_21', 'CCFD_22', 'CCFD_23',
                  'CCFD_24', 'CCFD_25', 'CCFD_26', 'CCFD_27']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ccfd_40(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFD_40', 'CCFD_31', 'CCFD_32', 'CCFD_33',
                  'CCFD_34', 'CCFD_35', 'CCFD_36', 'CCFD_36A']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ccfd_50(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFD_50', 'CCFD_20', 'CCFD_30', 'CCFD_40']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ccfd_70(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFD_70', 'CCFD_50', 'CCFD_60', 'CCFD_61']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


# Cashflow Indirect
def check_ccfi_8(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFI_8', 'CCFI_1', 'CCFI_2', 'CCFI_2B',
                  'CCFI_3', 'CCFI_4', 'CCFI_4B', 'CCFI_5', 
                  'CCFI_6' 'CCFI_6B', 'CCFI_7']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ccfi_20(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFI_20', 'CCFI_8', 'CCFI_9', 'CCFI_10',
                  'CCFI_11', 'CCFI_12', 'CCFI_13', 'CCFI_14', 
                  'CCFI_15' 'CCFI_16', 'CCFI_17']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ccfi_30(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFI_30', 'CCFI_21', 'CCFI_22', 'CCFI_23',
                  'CCFI_24', 'CCFI_25', 'CCFI_26', 'CCFI_27']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ccfi_40(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFI_40', 'CCFI_31', 'CCFI_32', 'CCFI_33',
                  'CCFI_34', 'CCFI_35', 'CCFI_36', 'CCFI_37']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ccfi_50(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFI_50', 'CCFI_20', 'CCFI_30', 'CCFI_40']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_ccfi_70(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CCFI_70', 'CCFI_50', 'CCFI_60', 'CCFI_61']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


if __name__ == '__main__':
    print("This is a module for checking COMPANY_CASHFLOW_STATEMENTS")

