from spmf import Spmf

spmf = Spmf("PrefixSpan", "contextPrefixSpan.txt", "output.txt", [1, "", True])
spmf.run()
print(spmf.decode_output())
print(spmf.to_pandas_dataframe(pickle=True))
spmf.to_csv("output.csv")
