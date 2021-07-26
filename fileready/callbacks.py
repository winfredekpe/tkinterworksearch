def dictfile():

    with open('file.txt', 'r+') as file:
        res = {}
        data = file.read().replace('\n', ' ').split(' ')
        keys = set(data)
        if('' in keys):
            keys.remove('')
        for k in keys:
            res[k] = 0
            for it in data:
                if(k == it):
                    res[k] += 1
    print(res)
