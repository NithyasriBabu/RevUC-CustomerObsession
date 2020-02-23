import pandas as pd
import numpy as np

#%% Read Products
pcols = {'PRODUCT_ID': np.int32, 'DEPARTMENT': str, 'COMMODITY' : str, 'BRAND_TYPE': str, 'ORGANIC': str}
products = pd.read_csv('data/5000_products.csv',skiprows=[0],names=pcols.keys(), dtype= pcols)

products.DEPARTMENT = products.DEPARTMENT.str.strip()
products.COMMODITY = products.COMMODITY.str.strip()
products.ORGANIC = products.ORGANIC.map({'N':False, 'Y' : True})

products.to_csv('data/5000_products_prosessed.csv',index=False)

#%% Read Transactions
tcols = { 'HSHD_ID': np.int32, 'BSKT_ID' : np.int32, 'DATE': str, 'PRODUCT_ID' : np.int32, 'SPEND' : np.float32,
         'UNITS': np.int32,'STORE_REGION': str,'WEEK_NUM': np.int32,'YEAR': str}

transactions = pd.read_csv('data/5000_transactions.csv',skiprows=[0],names=tcols.keys(), dtype= tcols)
transactions.STORE_REGION = transactions.STORE_REGION.str.strip()

transactions.to_csv('data/5000_transactions_prosessed.csv',index=False)

#%% Read Households
hcols = { 'HSHD_ID': np.int32, 'LOYALTY': str, 'AGE_RANGE': str, 'MARIAL_STATUS': str, 'INCOME_RANGE': str, 
         'HOMEOWNER': str, 'HSHD_COMP' : str, 'HH_SIZE' : str, 'CHILDREN' : str}
hcols_navalues = {'HH_SIZE': ['null'],'CHILDREN': ['null']}

households = pd.read_csv('data/5000_households.csv',skiprows=[0],names=hcols.keys(), dtype= hcols,
                         na_values=hcols_navalues)

households.AGE_RANGE = households.AGE_RANGE.str.strip()
households.MARIAL_STATUS = households.MARIAL_STATUS.str.strip()
households.INCOME_RANGE = households.INCOME_RANGE.str.strip()
households.HOMEOWNER = households.HOMEOWNER.str.strip()
households.HSHD_COMP = households.HSHD_COMP.str.strip()
households.HH_SIZE = households.HH_SIZE.str.strip()
households.CHILDREN = households.HH_SIZE.str.strip()

households.AGE_RANGE.replace({'null': 'NA','NOT AVAILABLE': 'NA'},inplace=True)
households.MARIAL_STATUS.replace({'null': 'NA','Unknown':'NA'},inplace=True)
households.INCOME_RANGE.replace({'null': 'NA','nan':'NA'},inplace=True)
households.HOMEOWNER.replace({'null': 'NA'},inplace=True)
households.HSHD_COMP.replace({'null': 'NA'},inplace=True)
households.HH_SIZE.replace({'null': '0'},inplace=True)
households.CHILDREN.replace({'NOT AVAILABLE': '0','nan': '0','null': '0'},inplace=True)

labels = ['RECENT INDEPENDENTS','ADULTING','ACTUAL ADULTS','GETTING OLDER','LATE BABY BOOMERS','BABY BOOMERS','SILENT','NA']
age_range_ordered_list = sorted(households.AGE_RANGE.unique().tolist())
map_values = dict(zip(age_range_ordered_list, labels))

households.AGE_RANGE = households.AGE_RANGE.map(map_values)

income_labels = {'UNDER 35K': 'LOW',
                 '35-49K': 'ABOVE LOW',
                 '50-74K': 'MODERATE',
                 '75-99K': 'ABOVE MODERATE',
                 '100-150K': 'HIGH',
                 '150K+': 'VERY HIGH',
                 'NA': 'NA'}

households.INCOME_RANGE = households.INCOME_RANGE.map(income_labels)

households.to_csv('data/5000_households_prosessed.csv',index=False)