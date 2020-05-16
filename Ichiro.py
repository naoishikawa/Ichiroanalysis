import pandas
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

pandas.options.display.max_columns = 30
pandas.options.display.max_rows = 10

url = "http://npb.jp/bis/players/11913885.html"
df = pandas.io.html.read_html(url)

atbats = df[1].drop([9])
atbats = atbats.drop(columns='所属球団')
atbats.columns = ["YEAR","GAME", "PA", "AB", "R", "H", "2B", "3B", "HR", "TB", "RBI", "SB", "CS", "SH", "SF", "BB", "HP", "SO", "GDP", "AVG", "SLG", "OBP"]

for index, item in atbats.iteritems():
   atbats[index] = atbats[index].fillna(0).astype(np.float64)

# atbats["OPS"] = atbats["SLG"] + atbats["OBP"]
# sns.pointplot(x="YEAR", y="OPS", data=atbats)

atbats["BB_SO"] = atbats["BB"] / atbats["SO"]
sns.pointplot(x="YEAR", y="BB_SO", data=atbats)


# In[ ]:




