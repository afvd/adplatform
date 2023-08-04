
import pyscript
from pyscript import Element
import pandas as pd
import matplotlib.pyplot as plt


dataset = {'0':[0,1,2,3,2,1,0], '1':[5,4,3,2,1,0]}

def greetings(name):
    print(f'Hi, {name}')

def get_data(*args, **kwargs):
    result_place = Element('result')
    data_key = Element("unique_identifyer").value

    data = dataset[data_key]
    result_place.element.innerText = data
    make_table(data)

def make_table(data):
    df = pd.DataFrame(data)
    plt.hist(df[0])
    plt.show()
