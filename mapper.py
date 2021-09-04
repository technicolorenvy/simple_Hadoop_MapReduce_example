#!/usr/bin/env python
import sys

# pulled from nltk's stopwords -
# I'd prefer to use nltk for this, but ran into issues getting it to work
# w/ Hadoop. fix appears to be here
# https://stackoverflow.com/questions/10716302/how-to-import-nltk-corpus-in-hdfs-when-i-use-hadoop-streaming
# but opted to just hardcode for now
stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again',
  'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they',
  'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of',
  'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from',
  'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these',
  'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more',
  'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both',
  'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before',
  'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does',
  'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can',
  'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where',
  'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't',
  'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how',
  'further', 'was', 'here', 'than']

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stop_words:
            print '%s\t%s' % (word, "1")
