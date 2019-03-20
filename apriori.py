from apyori import apriori
from pprint import PrettyPrinter


MIN_SUPPORT = 0.1
MIN_CONFIDENCE = 0.8
MIN_LEN = 6 


if __name__=='__main__':
	import sys

	event_batches = list()
	pp = PrettyPrinter(indent=4)

	with open(sys.argv[1], 'r') as f:
		cur_batch = list()
		for line in f.readlines():
			event = line.split(',')[2].strip()
			if event == 'PAYMENT_SUCCESS':
				event_batches.append(cur_batch)
				cur_batch = list()
			else:
				cur_batch.append(event)
	res = list(apriori(event_batches, min_support = MIN_SUPPORT, min_confidence = MIN_CONFIDENCE))
	for r in res:
		if len(r.items) >= MIN_LEN:
			print ("{},{},{}".format(r.support, r.ordered_statistics[0].confidence, list(r.items)))
