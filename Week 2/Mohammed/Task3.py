
def main():
    dictionaries = [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
    dictionaries.sort(key= lambda item: item['color'])
    
    print(dictionaries)

main()
