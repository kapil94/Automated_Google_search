import bs4,requests
from requests_html import HTMLSession
import sys,os,re
import webbrowser

os.chdir('/home/kapil/Desktop')

##### to take search keyword as 
def index():
	if len(sys.argv)>1:
		
		search_obj=requests.get('https://www.google.com/search?q='+sys.argv[1])
		bs4_obj=bs4.BeautifulSoup(search_obj.text,'html.parser')
		
		
		if sys.argv[1]+".html" not in os.listdir():
		
			file_obj=open('/home/kapil/Desktop/'+sys.argv[1]+'.html','x')
			file_obj.write(str(bs4_obj))
		
def getfile(filename):
	li=[]
	split_list=[]
	file_obj=open('/home/kapil/Desktop/'+filename,'r')
	bs4_obj=bs4.BeautifulSoup(file_obj.read(),'html.parser')
	
	li=list(bs4_obj.select('div > span > a'))
	
	li=map(str,li)
	li=list(li)	
	
	# to filter url
	for i in range(0,len(li)):
		split_list.insert(i,li[i].split('=')[2].split(';')[0].split('&')[0])
	
	
	
	# To check top 5 search and open in new tab
	for i in range(0,5):
		if requests.get(split_list[i]).status_code==200:
			webbrowser.open_new_tab(split_list[i])
		
	
	
	

index()
getfile(sys.argv[1]+'.html')




