import matplotlib.pyplot as plt

if __name__ == '__main__':

    time = ['01:00 AM', '02:00 AM', '03:00 AM', '04:00 AM', '05:00 AM', '06:00 AM', '07:00 AM', '08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM', '12:00 AM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM', '06:00 PM', '07:00 PM', '08:00 PM', '09:00 PM', '10:00 PM', '11:00 PM', '12:00 PM']
    tokyo = [18.1, 18.0, 17.7, 17.6, 17.3, 17.1, 16.8, 17.3, 17.5, 17.7, 17.5, 17.6, 17.4, 17.3, 18.2, 17.9, 17.8, 17.7, 17.4, 17.2, 17.3, 16.7, 16.4, 15.6]
    kyoto = [13.6, 13.5, 13.3, 13.1, 12.9, 12.8, 13.3, 14.1, 16.2, 18.2, 19.6, 20.3, 21.2, 21.8, 21.3, 20.7, 20.0, 19.4, 18.5, 18.6, 18.5, 17.9, 17.7, 17.5]

    plt.plot(time, tokyo)
    plt.plot(time, kyoto)
    plt.xlabel('time')
    plt.xticks(rotation=90)
    plt.ylabel('temperature')
    plt.title('Temperature of Tokyo and Kyoto')
    plt.legend(['Tokyo', 'Kyoto'])
    plt.savefig('01.png')
