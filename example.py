from spmf import Spmf

spmf = Spmf("TKS", "input.text", "output.txt", [5, 4, "", "", 1])
spmf.run()
print(spmf.decode_output())
print(spmf.to_pandas_dataframe())
spmf.to_csv("output.csv")
