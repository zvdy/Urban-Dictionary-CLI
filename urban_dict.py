import sys
import requests

# Make the request to the Urban Dictionary API even if the word has spaces

def get_urban_dict(word):
    word = word.replace(' ', '%20')
    url = 'http://api.urbandictionary.com/v0/define?term=' + word
    response = requests.get(url)
    return response.json()

# Print the definition of the word

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 urban_dict.py <word> <number of definitions>')
        print('To add spaces in the word, use %20 instead of a space')
        sys.exit(1)
    word = sys.argv[1]
    if len(sys.argv) > 2:
        num = int(sys.argv[2])
    else:
        num = 1
    data = get_urban_dict(word)
    if len(data['list']) == 0:
        print('No results found for ' + word)
        sys.exit(1)
    for i in range(num):
        print(data['list'][i]['definition'])

if __name__ == '__main__':
    main()
