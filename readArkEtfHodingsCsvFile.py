import pandas as pd

x = pd.read_csv("./Ark_Etf_Holdings/05-05-2022/ARK_SPACE_EXPLORATION_&_INNOVATION_ETF_ARKX_HOLDINGS.csv")
print( x[x["ticker"]=="TRMB"]["weight (%)"] )