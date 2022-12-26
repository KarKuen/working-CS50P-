import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'([0-9]|10|11|12):?([0-5][0-9])? (AM|PM) to ([0-9]|10|11|12):?([0-5][0-9])? (AM|PM)', s):

        if match.group(1) == '12' and match.group(3) == 'AM':
            if match.group(2) == None and match.group(6) == 'AM':
                return('00:00 to ' + '{0:0=2d}'.format(int(match.group(4))) + ':00')
            elif match.group(2) == None and match.group(6) == 'PM' and match.group(4) == '12':
                return('00:00 to 12:00')
            elif match.group(2) == None and match.group(6) == 'PM':
                return('00:00 to ' + str(int(match.group(4)) + 12) + ':00')
            elif match.group(4) == '12' and match.group(6) == 'AM':
                return('00:' + match.group(2) + ' to ' + '00:' + match.group(5))
            elif match.group(4) == '12' and match.group(6) == 'PM':
                return('00:' + match.group(2) + ' to ' + '12:' + match.group(5))
            elif match.group(6) == 'AM':
                return('00:' + match.group(2) + ' to ' + '{0:0=2d}'.format(int(match.group(4))) + ':' + match.group(5))
            elif match.group(6) == 'PM':
                return('00:' + match.group(2) + ' to ' + '{0:0=2d}'.format(int(match.group(4)) + 12) + ':' + match.group(5))

        elif match.group(1) == '12' and match.group(3) == 'PM':
            if match.group(2) == None and match.group(6) == 'AM':
                return('12:00 to ' + '{0:0=2d}'.format(int(match.group(4))) + ':00')
            elif match.group(2) == None and match.group(6) == 'AM' and match.group(4) == '12':
                return('12:00 to 00:00')
            elif match.group(2) == None and match.group(6) == 'PM':
                return('12:00 to ' + str(int(match.group(4)) + 12) + ':00')
            elif match.group(4) == '12' and match.group(6) == 'AM':
                return('12:' + match.group(2) + ' to ' + '00:' + match.group(5))
            elif match.group(4) == '12' and match.group(6) == 'PM':
                return('12:' + match.group(2) + ' to ' + '12:' + match.group(5))
            elif match.group(6) == 'AM':
                return('12:' + match.group(2) + ' to ' + '{0:0=2d}'.format(int(match.group(4))) + ':' + match.group(5))
            elif match.group(6) == 'PM':
                return('12:' + match.group(2) + ' to ' + '{0:0=2d}'.format(int(match.group(4)) + 12) + ':' + match.group(5))

        elif match.group(4) == '12' and match.group(6) == 'PM':
            if match.group(2) == None and match.group(3) == 'AM':
                return(match.group(1) + ' to 12:00')
            elif match.group(2) == None and match.group(6) == 'PM':
                return(match.group(1) + ' to 12:00')
            if match.group(1) == '12' and match.group(3) == 'AM':
                return('00:' + match.group(2) + ' to ' + '12:' + match.group(5))
            elif match.group(1) == '12' and match.group(3) == 'PM':
                return('12:' + match.group(2) + ' to ' + '12:' + match.group(5))
            elif match.group(3) == 'AM':
                return('{0:0=2d}'.format(int(match.group(1))) + ':' + match.group(2) + ' to ' + '12:' + match.group(5))
            elif match.group(3) == 'PM':
                return('{0:0=2d}'.format(int(match.group(1)) + 12) + ':' + match.group(2) + ' to ' + '12:' + match.group(5))

        elif match.group(4) == '12' and match.group(6) == 'AM':
            if match.group(2) == None and match.group(3) == 'AM':
                return(match.group(1) + '00:00 to ')
            elif match.group(2) == None and match.group(6) == 'PM':
                return(match.group(1) + '00:00 to ')
            if match.group(1) == '12' and match.group(3) == 'AM':
                return('00:' + match.group(2) + ' to ' + '00:' + match.group(5))
            elif match.group(1) == '12' and match.group(3) == 'PM':
                return('12:' + match.group(2) + ' to ' + '00:' + match.group(5))
            elif match.group(3) == 'AM':
                return('{0:0=2d}'.format(int(match.group(1))) + ':' + match.group(2) + ' to ' + '00:' + match.group(5))
            elif match.group(3) == 'PM':
                return('{0:0=2d}'.format(int(match.group(1)) + 12) + ':' + match.group(2) + ' to ' + '00:' + match.group(5))

        elif ':' not in s:

            if (match.group(3) == 'AM') and (match.group(6) == 'AM'):
                return('{0:0=2d}'.format(int(match.group(1))) + ':00' + ' to ' + '{0:0=2d}'.format(int(match.group(4))) + ':00')

            elif (match.group(3) == 'AM') and (match.group(6) == 'PM'):
                return('{0:0=2d}'.format(int(match.group(1))) + ':00' + ' to ' + str((int(match.group(4)) + 12)) + ':00')

            elif (match.group(3) == 'PM') and (match.group(6) == 'AM'):
                return('{0:0=2d}'.format(int(match.group(1)) + 12) + ':00' + ' to ' + '{0:0=2d}'.format(int(match.group(4))) + ':00')

            else:
                return(str(int(match.group(1)) + 12) + ':00' + ' to ' + str(int(match.group(4)) + 12) + ':00')

        else:

            if (match.group(3) == 'AM') and (match.group(6) == 'AM'):
                return('{0:0=2d}'.format(int(match.group(1))) + ':' + match.group(2) + ' to ' + '{0:0=2d}'.format(int(match.group(4))) + ':' + match.group(5))

            elif (match.group(3) == 'AM') and (match.group(6) == 'PM'):
                return('{0:0=2d}'.format(int(match.group(1))) + ':' + match.group(2) + ' to ' + str('{0:0=2d}'.format(int(match.group(4)) + 12)) + ':' + match.group(5))

            elif (match.group(3) == 'PM') and (match.group(6) == 'AM'):
                return(str('{0:0=2d}'.format(int(match.group(1)) + 12)) + ':' + match.group(2) + ' to ' + '{0:0=2d}'.format(int(match.group(4))) + ':' + match.group(5))

            else:
                return(str('{0:0=2d}'.format(int(match.group(1)))) + ':' + match.group(2) + ' to ' + str('{0:0=2d}'.format(int(match.group(4)) + 12))) + ':' + match.group(5)

    else:
        raise ValueError




if __name__ == "__main__":
    main()