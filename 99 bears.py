def bottles():

    for i in range(99, 0, -1):

        if i == 1:
            print('1 bottle of bear on the wall, 1 bottle of bear!')
            print('So take it down and pass it around - no more bottles of beer on the wall.')

        elif i == 2:
            print('2 bottles of bear on the wall, 2 bottles of bear!')
            print('So take one down and pass it around - one more bottle of beer on the wall')

        else:
            print('{0} more bottles of bear on the wall, {0} bottles of bear!'.format(i))
            print('So take one down and pass it around - {} more bottle of beer on the wall'.format(i-1))


bottles()
