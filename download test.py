import urllib.request
url = "https://raw.github.com/besser435/TEAW-Mod/master/TEAW%20v0.1.2.jar"
print ("download start")
filename, headers = urllib.request.urlretrieve(url, filename="C:\\Users\\brand\\OneDrive\\Python\\GitHub\\Random-Projects\\testfile.jar")
print ("download complete")
print ("download file location: ", filename)
#print ("download headers: ", headers)