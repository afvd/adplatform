
#import pyscript
#from pyscript import Element
import pandas as pd
import matplotlib.pyplot as plt


dataset = {'0':[0,1,2,3,2,1,0], '1':[5,4,3,2,1,0]}

def greetings(name):
    print(f'Hi, {name}')

def get_data(data_key):
    if data_key in dataset:
        data_frame = get_data_df(dataset[data_key])
        message = "loading Data for entered Unique Identifyer"
    else:
        message = "Invalid Unique Identifyer"
    return message, data_frame

def get_data_df(data):
    df = pd.DataFrame(data)
    return df

    #takes in a pandas dataframe "data" and a plot type
def get_data_plot(data):
    fig, ax = plt.subplots()
    plt.bar(data.index, data[0])
    # Naming the x-label
    plt.xlabel('Visit')
    # Naming the y-label
    plt.ylabel('Poem Score')
    # Naming the title of the plot
    plt.title('Patient Data - POEM score vs. Visit')
    return fig
