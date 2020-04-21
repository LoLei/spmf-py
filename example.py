from spmf import Spmf

# Important: Use .text extension of text data input, it will fail with .txt
# https://www.philippe-fournier-viger.com/spmf/Using_a_TEXT_file_as_input.php
spmf = Spmf("TKS", "input.text", "output.txt", [5, 4, "", "", 1])
spmf.run()
print(spmf.decode_output())
