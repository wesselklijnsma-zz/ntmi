# python lab2.py -c [path] -n [value] -m [value]
# Assignment 2
# Marco Schaap 5871352

import sys, getopt, operator


ngrams = {}


def readfile(file):

    paragraphs = ""
    paragraph = ""
    flag = 1
    
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
                 # print paragraph
                paragraphs += paragraph.replace('\n', ' ')
                paragraph = ""
                flag = 1

    paragraphs = paragraphs.rstrip()
    return paragraphs
    




def setNgrams(n, text):
    words = []
    ngrams = {}

    with open(text,'r') as f:
        for line in f:
            for word in line.split(): 
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

    return ngrams

def sumList():
    print 'The sum is: ', sum(ngrams.values())

def freq(m):
    sortedNgrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(0,m):
        print sortedNgrams[i]

def main(argv):
    inputfile = ''

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
    print text
    #setNgrams()


if __name__ == "__main__":
    main(sys.argv[1:])
