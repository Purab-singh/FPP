def dicttocs(dictionary):

    pairs = []
    for  value in dictionary.items():
        print(value)
        pairs.append(value[0] + '=' + value[1])
        print(pairs)

    result = ';'.join(pairs)
    print(result)
    print(';'.join( ['='.join(i) for i in dictionary.items()]))

dicttocs({'a': 'b', 'c': 'd', 'e': 'f' ,'g':'h'})