'''scipy在统计上的应用'''
import numpy
import scipy

scores = numpy.array([114, 100, 104, 89, 102, 91, 114, 114, 103, 105,
108, 130, 120, 132, 111, 128, 118, 119, 86, 72, 111, 103, 74, 112, 107,
103, 98, 96, 112, 112, 93])
xmean = scipy.mean(scores)
sigma = scipy.std(scores)
n = scipy.size(scores)
print (xmean, xmean - 2.576*sigma /scipy.sqrt(n), \
xmean + 2.576*sigma / scipy.sqrt(n) )

from scipy import stats
result=scipy.stats.bayes_mvs(scores)
print(result)
#get help
#help(scipy.stats.bayes_mvs)
