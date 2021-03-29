import os
import argparse
import csv
from main import ChocolateFeast


parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Please pass a txt or csv file with the input data")
parser.add_argument("output_file", help="Please pass a txt or csv file for the output to be written to")
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

if '/' not in output_file:
    output_file = os.path.join('/'.join(__file__.split('/')[0:-1]),output_file)

try:
    os.remove(output_file)
except:
    pass

with open(input_file, 'r') as data:
    for line in csv.DictReader(data):

        cf = ChocolateFeast(output_file=output_file)
        cf.cash = int(line['cash'])
        cf.price = int(line['price'])
        cf.wrappers_needed = int(line['wrappers_needed'])
        cf.chocolate_type = line['type']

        cf.main()

