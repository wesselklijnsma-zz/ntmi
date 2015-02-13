# python lab2.py -c [path] -n [value] -m [value]
# Assignment 2
# Marco Schaap 5871352
from __future__ import division
import sys, getopt, operator, re


def readfile(file):

    paragraphs = {}
    paragraph = ""
    flag = 1
    i = 0
    
    with open(file,'r') as f:

        for line in f:   
            if line.strip() != '' and flag == 1:
                paragraph += 'START ' 
                paragraph += line
                flag = 0
            elif line.strip() != '' and flag == 0:
                paragraph += line
            elif line.strip() == '' :
                line += 'STOP '
                paragraph += line 
                paragraphs[i] = paragraph.replace('\n', ' ')
                paragraph = "";
                flag = 1
                i += 1
    
    paragraphs = [paragraphs[p] for p in paragraphs if len(re.findall(r'\w+', paragraphs[p])) > 1]
    return paragraphs
    




def setNgrams(n, text):
    words = []
    ngrams = {}


    for paragraph in text:
        for word in paragraph.split(): 
            words.append(word)

        for i in range (0, (len(words) - n)):
            ngram = ''
            for j in range(0, n):
                ngram += words[i+j] + " "

            ngram = ngram.rstrip()

            if(ngram in ngrams):
                ngrams[ngram] += 1
            else:
                ngrams[ngram] = 1
        words = []

    return ngrams

def sumList():
    print 'The sum is: ', sum(ngrams.values())

def freq(m, ngrams):
    sortedNgrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(0,m):
        print sortedNgrams[i]

def probN(sequence, training):
    n = len(sequence.split())
    p = 0
    ngrams = setNgrams(n, training)
    ngrams1 = setNgrams(n-1, training)

    lastWord = sequence.rsplit()[-1]
    head = sequence.replace(lastWord, '').rstrip()
    sequence = sequence.rstrip()
    if sequence in ngrams and head in ngrams1:
        print ngrams[sequence]
        print ngrams1[head]
        p = ngrams[sequence]/ngrams1[head]

    return p


def main(argv):
    inputfile = ''
    file2 = 'test.txt'


    try:
        opts, args = getopt.getopt(argv,"c:n:m:", ["ifile="])
    except getopt.GetoptError:
        print 'lab1.py -c <inputfile> -n <value> -m <value>'

    for opt, arg in opts:
        if opt in ("-c", "--ifile"):
            inputfile = arg
        elif opt == "-n":
            n = int(arg)
        elif opt == "-m":
            m = int(arg)

    text = readfile(inputfile)
    with open(file2, 'r') as f:
        for line in f:
            print line 
            print probN(line, text)

if __name__ == "__main__":
    main(sys.argv[1:])
