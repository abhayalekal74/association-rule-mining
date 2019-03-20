from pprint import PrettyPrinter
from python_fp_growth.fp_growth import find_frequent_itemsets


MIN_LEN = 5 
MIN_SUPPORT = 0.001

if __name__=='__main__':
	import sys

	transactions = list()
	pp = PrettyPrinter(indent=4)

	with open(sys.argv[1], 'r') as f:
		cur = list()
		lines = f.readlines()
		total_lines = len(lines)
		min_occurences = MIN_SUPPORT * total_lines
		print ("Min support: {}, Total records: {}".format(min_occurences, total_lines))
		for line in lines:
			event = line.split(',')[2].strip()
			cur.append(event)
			if event == 'PAYMENT_SUCCESS':
				transactions.append(cur)
				cur = list()

	for itemset in find_frequent_itemsets(transactions, min_occurences, include_support  = True):
		if len(itemset[0]) >= MIN_LEN:
			print len(itemset[0]), itemset
