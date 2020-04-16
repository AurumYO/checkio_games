def time_converter(time):
    time, daytime = time.split(' ')
    hour, minutes = time.split( ':' )
    if daytime == 'a.m.':
        if int(hour) == 12:
            return '00:' + minutes
        elif 0 <= int(hour) < 10:
            return '0' + hour + ':' + minutes
        else:
            return time
    elif daytime == 'p.m.':
        if int(hour) < 12:
            return str(int(hour) + 12) + ':' + minutes
        else:
            return time

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter( '10:00 a.m.' ) == '10:00'
    assert time_converter('11:15 p.m.') == '23:15'
    assert time_converter('12:01 a.m.') == '00:01'
    print("Coding complete? Click 'Check' to earn cool rewards!")