def print_menu():
    print('1. km to miles')
    print('2. miles to km')

def km_miles():
    km = float(input('Enter distance in km : '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles : '))
    km = miles * 1.609
    print('Distance in km: {0}'.format(km))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do ? : ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
