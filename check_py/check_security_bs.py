import pandas as pd
import numpy as np


def check_sbs_111(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_111', 'SBS_111_1', 'SBS_111_3']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_111_4(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_111_4', 'SBS_112', 'SBS_113', 'SBS_114', 
                  'SBS_115', 'SBS_116']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_117_2(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_117_2', 'SBS_117_3', 'SBS_117_4']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_117(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_117', 'SBS_117_0', 'SBS_117_1', 'SBS_117_2',
                  'SBS_117_5', 'SBS_117_6', 'SBS_117_7', 'SBS_118',
                  'SBS_120', 'SBS_121', 'SBS_121_1', 'SBS_121_2',
                  'SBS_121_3', 'SBS_122', 'SBS_129', 'SBS_129_1',
                  'SBS_129_2']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_129_3(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_129_3', 'SBS_129_4', 'SBS_129_5']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_130(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_130', 'SBS_131', 'SBS_132', 'SBS_133',
                  'SBS_134', 'SBS_135', 'SBS_136', 'SBS_137', 
                  'SBS_138', 'SBS_139']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_110(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_110', 'SBS_111', 'SBS_111_4', 'SBS_117',
                  'SBS_129_3', 'SBS_130']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_211(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_211', 'SBS_211_1', 'SBS_211_2', 'SBS_211_3', 
                  'SBS_211_4', 'SBS_211_5', 'SBS_211_6', 'SBS_211_7']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_212(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_212', 'SBS_212_1', 'SBS_212_2', 'SBS_212_3', 
                  'SBS_212_4', 'SBS_212_5', 'SBS_212_6']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_210(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_210', 'SBS_211', 'SBS_212']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_221(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_221', 'SBS_222', 'SBS_223A', 'SBS_223B']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_224(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_224', 'SBS_225', 'SBS_226A', 'SBS_226B']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_220(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_220', 'SBS_221', 'SBS_224', 'SBS_227', 'SBS_240A']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_230(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_230', 'SBS_231', 'SBS_232A', 'SBS_232B']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_255_2(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_255_2', 'SBS_255_3', 'SBS_240']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_250(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_250', 'SBS_251', 'SBS_252', 'SBS_253', 
                  'SBS_253_1', 'SBS_254', 'SBS_255', 'SBS_256']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_200(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_200', 'SBS_210', 'SBS_220', 'SBS_255_2', 
                  'SBS_250', 'SBS_260']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_311(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_311', 'SBS_312', 'SBS_313']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_310(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_310', 'SBS_311', 'SBS_314', 'SBS_315', 
                  'SBS_316', 'SBS_317', 'SBS_318', 'SBS_319', 
                  'SBS_320', 'SBS_321', 'SBS_322', 'SBS_323', 
                  'SBS_324', 'SBS_325', 'SBS_326', 'SBS_327', 
                  'SBS_328', 'SBS_329', 'SBS_329_1', 'SBS_329_2', 
                  'SBS_329_3', 'SBS_330', 'SBS_331', 'SBS_331_1', 
                  'SBS_332']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_341(df: pd.DataFrame) -> pd.DataFrame:
    defaul_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_341', 'SBS_342', 'SBS_343']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[defaul_list + check_list].loc[df['check'] != 0]


def check_sbs_340(df: pd.DataFrame) -> pd.DataFrame:
    default_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_340', 'SBS_341', 'SBS_344', 'SBS_345', 
                  'SBS_346', 'SBS_347', 'SBS_348', 'SBS_349', 
                  'SBS_350', 'SBS_350_1', 'SBS_351', 'SBS_352', 
                  'SBS_353', 'SBS_353_1', 'SBS_353_2', 'SBS_354', 
                  'SBS_355', 'SBS_356', 'SBS_357']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[default_list + check_list].loc[df['check'] != 0]


def check_sbs_300(df: pd.DataFrame) -> pd.DataFrame:
    defaul_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_300', 'SBS_310', 'SBS_340']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[defaul_list + check_list].loc[df['check'] != 0]


def check_sbs_411_1(df: pd.DataFrame) -> pd.DataFrame:
    defaul_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_411_1', 'SBS_411_1A', 'SBS_411_1B']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[defaul_list + check_list].loc[df['check'] != 0]


def check_sbs_417_1(df: pd.DataFrame) -> pd.DataFrame:
    defaul_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_417_1', 'SBS_417_2_1', 'SBS_417_2_2']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[defaul_list + check_list].loc[df['check'] != 0]


def check_sbs_417(df: pd.DataFrame) -> pd.DataFrame:
    defaul_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_417', 'SBS_417_1', 'SBS_417_2']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[defaul_list + check_list].loc[df['check'] != 0]


def check_sbs_410(df: pd.DataFrame) -> pd.DataFrame:
    defaul_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_410', 'SBS_411', 'SBS_412', 'SBS_413',
                  'SBS_414', 'SBS_414_1', 'SBS_415', 'SBS_416',
                  'SBS_417', 'SBS_418']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[defaul_list + check_list].loc[df['check'] != 0]


def check_sbs_420(df: pd.DataFrame) -> pd.DataFrame:
    defaul_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_420', 'SBS_420_1', 'SBS_420_2', 'SBS_420_3']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[defaul_list + check_list].loc[df['check'] != 0]


def check_sbs_400(df: pd.DataFrame) -> pd.DataFrame:
    defaul_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_400', 'SBS_410', 'SBS_420']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[defaul_list + check_list].loc[df['check'] != 0]


def check_sbs_440(df: pd.DataFrame) -> pd.DataFrame:
    defaul_list = ['SECURITY_CODE', 'REPORT_DATE', 'FREQ_CODE', 'AUDITED']
    check_list = ['SBS_440', 'SBS_300', 'SBS_400']
    print("CHECK ITEM & SUB-ITEMS " + check_list[0])
    
    df['check'] = df[check_list[0]] - np.sum(df[i] for i in check_list[1:])
    
    
    return df[defaul_list + check_list].loc[df['check'] != 0]


if __name__ == '__main__':
    print("This is a module for checking SECURITY_BALANCE_SHEET")


