import os

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

def printPrompt():
    hazelnutArt = ' ____ \n/    \\\n|    |\n\\____/'
    print('Welcome to Hazelnut!')
    print(hazelnutArt)
    print('Search for information from the City of Kingston website here.')
    print('The most relevant topics will be returned.')

def getUserSearch():
    searchWord = input('Search word: ')
    #potential for error catching or processing here
    return searchWord


def runSearch(numSearches):
    doneSearch = False
    searchWord = getUserSearch()
    #get top N searches
    print('Top',numSearches,'results for',searchWord)
    #print search results 1-numSearches
    while not doneSearch:
        userResponse = input('For more results, press "+". To search another word, press "n".')
        if userResponse == '+':
            print('next',numSearches,'results:')
        elif userResponse == 'n':
            #clear screen
            return

while(1):
    clrscr()
    printPrompt()
    runSearch(5)
    


