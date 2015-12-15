from graph import Greengraph
from argparse import ArgumentParser
import pyplot as plt

def process():
    parser = ArgumentParser(description = 'Plot the propotion of green space between two locations')
    
    parser.add_argument('--start','-s')
    parser.add_argument('--end','-e')
    parser.add_argument('--steps','-n')
    parser.add_argument('--out','-o')

    arguments = parser.parse_args()



    graph = Greengraph(arguments.start,arguments.end)
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    plt.savefig(arguments.out)
