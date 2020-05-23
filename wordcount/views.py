
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')


def countpage(request):
    ft=request.GET['fulltext']
    # fulltext means the textarea box name,

    #now lets count each word and store it in dictionary, 
    wordlist=ft.split()    #first spilt the word
       
    worddict={}                 #creating dict

    for word in wordlist:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word]=1


# sorting the dictionary from big valur to small
    sorteddict = sorted(worddict.items(), key=operator.itemgetter(1),reverse=True) 

# geting first key value pair
    max_word=sorteddict[0]
    # max_word=next(iter(sorteddict))
    # max_word=list(sorteddict.keys())[0]
    # new_lst = list(sorteddict)
    # max_word= new_lst[0]


    return render(request,'count.html', {'typedtext':ft, 'count':len(wordlist), 'sortdict':sorteddict, 'max_word':max_word })




def aboutpage(request):
    return render(request,'about.html')