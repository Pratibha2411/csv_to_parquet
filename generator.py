import pandas as pd
import sys


# csv_file = "hrdata.csv"
csv_file = sys.argv[1]
# parquet_file = "hrdata.parquet"
parquet_file = sys.argv[2]

df = pd.read_csv(csv_file)
output = df.to_parquet(parquet_file)
df.head()
