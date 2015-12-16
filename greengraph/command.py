from graph import Greengraph
from argparse import ArgumentParser
from matplotlib import pyplot as plt

def process():
    parser = ArgumentParser(description = 'Plot the propotion of green space between two locations')
    
    parser.add_argument('--start','-s',type='str',required=True)
    parser.add_argument('--end','-e',type='str',required=True)
    parser.add_argument('--steps','-n',default=10,type='int')
    parser.add_argument('--out','-o',default='green_between.png')

    arguments = parser.parse_args()



    mygraph = Greengraph(arguments.start,arguments.end)
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    plt.savefig(arguments.out)
