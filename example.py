from spmf import Spmf

# spmf = Spmf("TKS", "min.text", "output.txt", [5, 2, 5, "", 1])
# spmf = Spmf("TKS", "contextPrefixSpan.txt", "output.txt", [5, "", "", "", ""])
spmf = Spmf("PrefixSpan", "contextPrefixSpan.txt", "output.txt", [1, "", True])
spmf.run()
print(spmf.decode_output())
print(spmf.to_pandas_dataframe(pickle=True))
spmf.to_csv("output.csv")
