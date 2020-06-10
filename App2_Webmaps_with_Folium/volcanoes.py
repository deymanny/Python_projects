#converting text file to csv file

import pandas as pd

read_file = pd.read_csv ("App2_webmap/volcanoes.txt")
read_file.to_csv ("App2_webmap/volcanoes.csv", index=None)