from graph import Greengraph
from argparse import ArgumentParser
from matplotlib import pyplot as plt

def process():
    parser = ArgumentParser(description = 'Plot the propotion of green space between two locations')
    
    parser.add_argument('--start','-s',type=str,required=True,
        help='The starting location')
    parser.add_argument('--end','-e',type=str,required=True,
        help='Then end location')
    parser.add_argument('--steps','-n',default=10,type=int,
        help='Number of satalite images to inspect between start and end locations - default = 10')
    parser.add_argument('--out','-o',default='green_between.png',
        help='Name of the .png output file the calculated graph will be written to -  default = green_between.png')

    arguments = parser.parse_args()



    mygraph = Greengraph(arguments.start,arguments.end)
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    plt.savefig(arguments.out)

if __name__ == "__main__":
    process()
