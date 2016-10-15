import cPickle as pickle

with open('.cache.dat') as fin:
	cache = pickle.load(fin)
	for k, v in cache.iteritems():
		print("%s\t%s" % (k, v))

