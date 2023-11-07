myList = ['helloo', 123, True,123.2]

myStr = myList[0]
i = myStr.find('o')
print(myStr.find('o', i+1))

url1 = '<a href="https://google.com">hello</a>'
url2 = '<div><a href="https://heights.edu/">school</a>'
url3 = '<data-attr="stuff"><a href="abc"><a>'

def urlSlice(a):
    i1 = a.find('href=')
    i2 = a.find('"', i1+6)
    return a[i1+6:i2]

myList = [url1,url2,url3]

for i in myList:
    print(urlSlice(i))
