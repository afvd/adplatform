def greetings(name):
    print(f'Hi, {name}')

def get_data(*args, **kwargs):
    result_place = Element['result']
    #result_place.write(f"{Element('name').value} is a good human from {Element('countries').value}")
    data = dataset[Element("unique_identifyer").value]
    print(data)

dataset = {"00000":[0,1,2,3,2,1,0], "00001":[5,4,3,2,1,0]}
#greetings('John Doe')
get_data
