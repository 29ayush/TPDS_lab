from string import maketrans
#import matplotlib.pyplot as plt
import re,os
engext = ".e"
freext = ".f"
dir_name = "Desktop/training"


def getstop():
    words = []
    with open('stopwords','r') as file: 
        content = file.readlines()
    words = [x.strip() for x in content]  
    words.remove('')
    return words

punctuation = '\n!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~1234567890'
punctuation = maketrans(punctuation," "*len(punctuation))
    
stopwords   = getstop()

os.chdir(dir_name)

def counter():
    word_count = {}
    j = 0 
    for item in os.listdir("."): # loop through items in dir
        if item.endswith(engext): # check for ".tar" extension
            with open(item,'r') as file:
                filedata = file.read()
                filedata = filedata.translate(punctuation)
               # for word in stopwords:
                #    filedata = filedata.replace(word, "")
                words = re.split(" *",filedata)       
                for word in words:
                    if word not in word_count.keys():
                        c = 0
                    else :
                        c = word_count[word]
                    word_count[word] = c+1
            #return word_count
        print(j)
        j = j+1
    return word_count


def plot(x):
    y = [i for i in range(len(x))]
    plt.plot(x,y,"ro")
    plt.show()

word_count = counter()
print (word_count)
plot(word_count.values())

