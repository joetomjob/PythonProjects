__author__ = 'zjb'

# you will do this once:
# for item in filename:
# it is not what you meant

# named constants are good
ID = 0
FNAME = 1
LNAME = 2
EMAIL = 3
COUNTRY = 4

COUNTRY_CODES = {
    'Bangladesh' : 'BGD',
    'China' : 'CHN',
    'Dominican Republic' : 'DOM',
    'Greece' : 'GRC',
    'Kazakhstan' : 'KAZ',
    'Nigeria' : 'NGA',
    'Philippines' : 'PHL',
    'Portugal' : 'PRT',
    'Ukraine' : 'UKR'
}

def parseName(parts):
    '''
    Take the list of tokens and return "F. Last"
    :param parts: List of tokens
    :return: string as specified
    '''
    first = parts[FNAME]
    last = parts[LNAME]
    return first[0] + '. ' + last

def parseEmail(parts):
    '''
    Take the list of tokens and return formatted string
    :param parts:
    :return: "User: <username> Domain: <domain>"
    '''
    # Instead of split('@') let's do this:
    email = parts[EMAIL]
    atloc = email.index('@') # or can use find()
    return "User: " + email[:atloc] + " Domain: " + email[atloc+1:]

def main():
    #datafile = input('Enter a file name: ')
    try:
        with open('data10.txt') as data:
            print(data.readline())
            for item in data:
                print('Data is : ' + item)
                parts = item.strip().split(',')
                print(parts)
                print(parseName(parts))
                print(parseEmail(parts))
                print(COUNTRY_CODES[parts[COUNTRY]])
            #value = int('six')
    except FileNotFoundError:
        print("that's not a file!")

main()
