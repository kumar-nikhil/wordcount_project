import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'key': 'value'})


def about(request):
    return render(request, 'about1.html')


def result(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            #Increment
            worddict[word] += 1
        else:
            #add
            worddict[word] = 1

    sorted_words = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    print(worddict)
    return render(request, 'result.html', {'fulltext': fulltext,
                                           'count': len(wordlist),
                                           'sortedWords': sorted_words})
