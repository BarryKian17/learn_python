from urllib.request import urlretrieve;

link = input('image link : ')

file_name = input('Image name : ')

urlretrieve(link,'image/'+file_name+'.jpg')