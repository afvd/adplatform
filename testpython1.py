
from pyscript import Element

dataset = {'0':[0,1,2,3,2,1,0], '1':[5,4,3,2,1,0]}

def greetings(name):
    print(f'Hi, {name}')

def get_data(*args, **kwargs):
    result_place = Element('result')
    data_key = Element("unique_identifyer").value

    data = dataset[data_key]
    result_place.element.innerText = data
