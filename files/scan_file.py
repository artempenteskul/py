def scanner(filename, function):
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        function(line)
    file.close()

