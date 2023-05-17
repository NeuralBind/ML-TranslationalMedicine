#!/usr/bin/env python3
"""Reproduce your result by your saved model.

This is a script that helps reproduce your prediction results using your saved
model. This script is unfinished and you need to fill in to make this script
work. If you are using R, please use the R script template instead.

The script needs to work by typing the following commandline (file names can be
different):

python3 run_model.py -i unlabelled_sample.txt -m model.pkl -o output.txt

"""

# author: Chao (Cico) Zhang
# date: 31 Mar 2017

import argparse
import sys

# Start your coding

# import the library you need here
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pandas as pd
import joblib
# End your coding


def main():
    """Main function."""
    '''
    parser = argparse.ArgumentParser(description='Reproduce the prediction')
    parser.add_argument('-i', '--input', required=True, dest='input_file',
                        metavar='unlabelled_sample.txt', type=str,
                        help='Path of the input file')
    parser.add_argument('-m', '--model', required=True, dest='model_file',
                        metavar='model.pkl', type=str,
                        help='Path of the model file')
    parser.add_argument('-o', '--output', required=True,
                        dest='output_file', metavar='output.txt', type=str,
                        help='Path of the output file')
    # Parse options
    args = parser.parse_args()

    if args.input_file is None:
        sys.exit('Input is missing!')

    if args.model_file is None:
        sys.exit('Model file is missing!')

    if args.output_file is None:
        sys.exit('Output is not designated!')
    '''
    # Start your coding

    # suggested steps
    # Step 1: load the model from the model file
    #with open(args.input_file, 'r') as f:
      # Read the CSV file and save it as a DataFrame
    data_frame = pd.read_csv('Validation_set.csv')
    Test = data_frame.drop(data_frame.filter(like='Unnamed'), axis=1)
    samples = data_frame.iloc[:, 0]



    # Step 2: apply the model to the input file to do the prediction
    #with open(args.model_file, 'rb') as f:

    model = joblib.load('rf_bio.pkl')

    # Load or preprocess your input data as needed
    predictions = model.predict(Test)
    # Step 3: write the prediction into the desinated output file
    #with open(args.output_file, 'w') as f:
    with open("predictions_rf.txt", 'w') as f:
        f.write('"Sample"\t"Subgroup"\n')  # Write the header line
        for sample, prediction in zip(samples, predictions):
            f.write(f'"{sample}"\t"{prediction}"\n')

    # End your coding


if __name__ == '__main__':
    main()


