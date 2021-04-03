# Automated_Google_search
To automate google search by python

The program uses bs4 module,webbrowser module and requests.

Prerequisite:

Program will only work if a command line argument is passed while running a program.
  
  i.e Search.py Goku

Here Goku- is a search keyword

Algorithm:

1. Create requests object by passing command line argument i.e search keyword.
2. Create a bs4 object from the request object by passing it as a text to bs4 BeautifulSoup module.
3. Create an .html page by appending bs4 object text in it.
4. Now open the previously created .html file in read mode and pass it as parameter to bs4 BeautifulSoup module.
5. Now filter the bs4 object to look for divs which contains spans which contain anchor tags (anchor tags contain the search result links).
6. Store the filtered result from previous step into a list.
7. Note that the list items are of bs4 type change the list items to string type.
8. Now filter the list items by removing unwanted symbols and store it in another list.
9. To get top 5 search results pass the filtered list to request.get method and check if status is 200.
10. If status of request.get method is 200 then the top 5 search results will open in browser tabs at a same time.
