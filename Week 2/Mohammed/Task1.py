
def main():
    simple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    simple_list.sort( key=lambda item : item[1])
    print(simple_list)

main()

