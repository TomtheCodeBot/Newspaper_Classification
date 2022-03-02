import pandas as pd

### This script is used to process data for anomalies, unfit for training.

### Removing duplicates that occurs in any file
def removeDuplicates(input_file, output_file):
    lines_seen = set()  ### holds lines already seen
    outfile = open(output_file, "w", encoding='latin-1')
    for line in open(input_file, "r", encoding='latin-1'):
        if line not in lines_seen:  ### not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

### Removing anomalies such as Nan, duplicates or short text
def removeAnomaly(input_file, output_file):
    data = pd.read_csv(input_file, error_bad_lines=False,encoding= 'latin1')
    data = data.loc[data['data'].str.len() > 11].dropna().drop_duplicates(subset=['ID'], keep='last').replace('\n','', regex=True)
    data = data.loc[data['data'].str.len() > 11].dropna().drop_duplicates(subset=['data'], keep='last')

    data.to_csv(output_file, index_label=False)

### Process data after scraping (reccommended)
def processFrame(input_file, output_file):
    removeDuplicates(input_file, output_file)
    removeAnomaly(output_file, output_file)