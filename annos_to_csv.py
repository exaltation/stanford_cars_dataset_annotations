import sys
import os
import argparse
from scipy.io import loadmat

parser = argparse.ArgumentParser()
parser.add_argument('phase', type=str, help="Phase: train or test", choices=['train', 'test'])

args = parser.parse_args(sys.argv[1:])

mat_file = 'cars_{}_annos.mat'.format(args.phase)
csv_file = 'cars_{}_annos.csv'.format(args.phase)
images_dir = os.path.abspath(os.path.join( os.path.dirname(os.path.dirname(__file__)), 'cars_{}'.format(args.phase) ))

mat_data = loadmat(mat_file)
annotations = mat_data['annotations'][0]
with open(csv_file, mode='w') as csv_data:
    for annotation in annotations:
        x1 = annotation[0][0][0]
        y1 = annotation[1][0][0]
        x2 = annotation[2][0][0]
        y2 = annotation[3][0][0]
        fname = annotation[-1][0]
        csv_data.write("{},{},{},{},{},{}\n".format(os.path.join(images_dir, fname),x1,y1,x2,y2,"car"))