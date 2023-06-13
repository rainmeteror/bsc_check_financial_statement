import pandas as pd
import numpy as np


def check_itmes(df: pd.DataFrame,
                items: str,
                sub_items: list,
                default_list: list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']) -> pd.DataFrame:
    
    items = items.upper()
    sub_items = [x.upper() for x in sub_items]
    sub_items.insert(0, items)
    print("CHECK ITEM & SUB-ITEMS " + sub_items[0])
    
    df['check'] = df[sub_items[0]] - np.sum(df[i] for i in sub_items[1:])
    
    
    return df[default_list + sub_items].loc[df['check'] != 0]


def check_cbs_110(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_110', 'CBS_111', 'CBS_112']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_120(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_120', 'CBS_121', 'CBS_123']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_130(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_130', 'CBS_131', 'CBS_132', 'CBS_133', 
                  'CBS_134', 'CBS_135', 'CBS_136', 'CBS_137', 
                  'CBS_139']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_140(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_140', 'CBS_141', 'CBS_149']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_150(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_150', 'CBS_151', 'CBS_152', 'CBS_153', 
                  'CBS_154', 'CBS_155']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])


    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_100(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_100', 'CBS_110', 'CBS_120', 'CBS_130', 'CBS_140', 'CBS_150']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_210(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_210', 'CBS_211', 'CBS_212', 'CBS_213', 
                  'CBS_214', 'CBS_215', 'CBS_216', 'CBS_219']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])

    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])

    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_221(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_221', 'CBS_222', 'CBS_223']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_224(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_224', 'CBS_225', 'CBS_226']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_227(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_227', 'CBS_228', 'CBS_229']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])

    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_220(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_220', 'CBS_221', 'CBS_224', 'CBS_227']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_230(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_230', 'CBS_231', 'CBS_232']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_240(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_240', 'CBS_241', 'CBS_242']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_250(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_250', 'CBS_251', 'CBS_252', 'CBS_253',
                  'CBS_254', 'CBS_255', 'CBS_2691']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    

    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_260(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_260', 'CBS_261', 'CBS_262', 'CBS_263',
                  'CBS_268', 'CBS_269']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_200(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_200', 'CBS_210', 'CBS_220', 'CBS_230',
                  'CBS_240', 'CBS_250', 'CBS_260']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_270(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_270', 'CBS_100', 'CBS_200']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_310(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_310', 'CBS_311', 'CBS_312', 'CBS_313',
                  'CBS_314', 'CBS_315', 'CBS_316', 'CBS_317',
                  'CBS_318', 'CBS_319', 'CBS_320', 'CBS_321',
                  'CBS_322', 'CBS_323', 'CBS_324']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_330(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_330', 'CBS_331', 'CBS_332', 'CBS_333',
                  'CBS_334', 'CBS_335', 'CBS_336', 'CBS_337',
                  'CBS_338', 'CBS_339', 'CBS_340', 'CBS_341',
                  'CBS_342', 'CBS_343']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_300(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_300', 'CBS_310', 'CBS_330']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_411(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_411', 'CBS_411A', 'CBS_411B']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_419(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_419', 'CBS_4191', 'CBS_4192']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_421(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_421', 'CBS_421A', 'CBS_421B']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_410(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_410', 'CBS_411', 'CBS_412', 'CBS_413', 
                  'CBS_414', 'CBS_415', 'CBS_416', 'CBS_417', 
                  'CBS_418', 'CBS_419', 'CBS_420', 'CBS_421',
                  'CBS_429']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_430(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_430', 'CBS_4301', 'CBS_431', 'CBS_432']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_400(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_400', 'CBS_410', 'CBS_430']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_cbs_440(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['CBS_440', 'CBS_300', 'CBS_400']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


if __name__ == '__main__':
    print("This is a module for checking COMPANY_BALANCE_SHEET")



