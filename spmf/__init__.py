"""
Python 3 Wrapper for SPMF
http://www.philippe-fournier-viger.com/spmf

Inspiration from:
https://github.com/fandu/maximal-sequential-patterns-mining
http://forum.ai-directory.com/read.php?5,5510
"""

__author__ = "Lorenz Leitner"
__version__ = "1.2"
__license__ = "GNU GPL v3.0"

import pandas as pd
import os
import subprocess
import tempfile


class Spmf:
    def __init__(self,
                 algorithm_name,
                 input_direct=None,
                 input_type="normal",
                 input_filename="",
                 output_filename="spmf-output.txt",
                 arguments=[],
                 spmf_bin_location_dir="."):
        self.executable_dir_ = spmf_bin_location_dir
        self.executable_ = "spmf.jar"

        if not (os.path.isfile(os.path.join(self.executable_dir_,
                                            self.executable_))):
            raise FileNotFoundError(self.executable_ + " not found. Please" +
                                    " use the spmf_bin_location_dir argument.")

        self.agorithm_name_ = algorithm_name
        self.input_ = self.handle_input(
            input_direct, input_filename, input_type)
        self.output_ = output_filename
        self.arguments_ = [str(a) for a in arguments]
        self.patterns_ = []
        self.df_ = None

    def handle_input(self, input_direct, input_filename, input_type):
        if input_filename:
            return input_filename
        if type(input_direct) == str:
            if input_type == "normal":
                file_ending = ".txt"
            elif input_type == "text":
                file_ending = ".text"
            return self.write_temp_input_file(input_direct,
                                              file_ending)
        if type(input_direct) == list:
            if input_type == "normal":
                seq_spmf = ""
                for seq in input_direct:
                    for item_set in seq:
                        for item in item_set:
                            seq_spmf += str(item) + ' '
                        seq_spmf += str(-1) + ' '
                    seq_spmf += str(-2) + '\n'
                return self.write_temp_input_file(seq_spmf, ".txt")
            if input_type == "text":
                seq_str = ""
                for seq in input_direct:
                    seq_str += seq + ". "
                return self.write_temp_input_file(seq_str, ".text")
        raise TypeError("no correct input format found (required: " +
                        "list or str, or input file via" +
                        " input_filename parameter)")

    def write_temp_input_file(self, input_text, file_ending):
        tf = tempfile.NamedTemporaryFile(delete=False)
        tf.write(bytes(input_text, 'UTF-8'))
        name = tf.name
        os.rename(name, name + file_ending)
        return name + file_ending

    def run(self):
        """
        Start the SPMF process
        Calls the Java binary with the previously specified parameters
        """
        subprocess_arguments = [
            "java", "-jar",
            os.path.join(self.executable_dir_, self.executable_),
            "run",
            self.agorithm_name_,
            self.input_, self.output_]
        subprocess_arguments.extend(self.arguments_)

        proc = subprocess.check_output(subprocess_arguments)
        proc_output = proc.decode()
        print(proc_output)
        if "java.lang.IllegalArgumentException" in proc_output:
            raise TypeError("java.lang.IllegalArgumentException")

    def parse_output(self):
        """
        Parse the output of SPMF and saves in in member variable patterns_
        -1 separates itemsets
        -2 indicates end of a sequence
        http://data-mining.philippe-fournier-viger.com/introduction-to-sequential-rule-mining/#comment-4114
        """
        lines = []
        with open(self.output_, "r") as f:
            lines = f.readlines()

        patterns = []
        for line in lines:
            line = line.strip()
            patterns.append(line.split(" -1 "))

        self.patterns_ = patterns
        return patterns

    def to_pandas_dataframe(self, pickle=False):
        """
        Convert output to pandas DataFrame
        pickle: Save as serialized pickle
        """
        # TODO: Optional parameter for pickle file name

        if not self.patterns_:
            self.parse_output()

        patterns_dict_list = []
        for pattern_sup in self.patterns_:
            pattern = pattern_sup[:-1]
            sup = pattern_sup[-1:][0]
            sup = sup.strip()
            if not sup.startswith("#SUP"):
                print("support extraction failed")
            sup = sup.split()
            sup = sup[1]

            patterns_dict_list.append({'pattern': pattern, 'sup': int(sup)})

        df = pd.DataFrame(patterns_dict_list)
        self.df_ = df

        if pickle:
            df.to_pickle(self.output_.replace(".txt", ".pkl"))
        return df

    def to_csv(self, file_name, df=None, list_as_string=True):
        """
        Save output as csv
        Either use member variable if it has already been set,
        or re-set it using to_pandas_dataframe, or use given dataframe
        list_as_string: Fix CSV output so that '[]' is not present
        """
        if self.df_ is None and df is None:
            self.df_ = self.to_pandas_dataframe()

        if df is not None:
            self.df_ = df

        if not list_as_string:
            self.df_.to_csv(file_name, sep=';', index=False)
        else:
            df = self.df_
            for _, row in df.iterrows():
                row['pattern'] = ','.join(row['pattern'])

            df.to_csv(file_name, sep=';', index=False)
