def time_converter(time):
    li = time.split(':')

    if int(li[0]) == 0:
        return '12:'+time[3:] + ' a.m.'
    elif int(li[0]) == 12:
        return time[0:2] + ':' + time[3:] + ' p.m.'
    elif int(li[0]) >= 13:
        hour = int(li[0]) - 12
        return str(hour) + ':' + time[3:] + ' p.m.'
    elif int(li[0]) < 12:
        return time[1:2] + ':' + time[3:] + ' a.m.'

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")