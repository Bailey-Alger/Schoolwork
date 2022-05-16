def show_homepage():
    print('      === DonateME Homeplate ===')
    print('--------------------------------------')
    print('| 1.  Login       | 2.  Register       |')
    print('--------------------------------------')
    print('| 3.  Donate      | 4.  Show Donations |')
    print('--------------------------------------')
    print('|              5.  Exit                |')
    print('--------------------------------------')


def donate(username):
    donation_amt = float(input('Enter amount to donate: '))
    donation = username + ' donated $' + str(donation_amt)
    print('Thank you!')
    return donation


def show_donations(donations):
    print('\n--- All Donations ---')
    if not donations:
        print('Currenctly, there are no donations')
    else:
        for donation in donations:
            print(donation)
