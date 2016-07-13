from cbe import CoinbaseExchange
import json
import datetime


def get_stats():
	coin = CoinbaseExchange()

	start = datetime.datetime(2016, 1, 1)
	end = datetime.datetime(2016, 6, 10)
	gran = 60 * 60 * 24

	stats = coin.getProductHistoricRates(start.isoformat(), end.isoformat(), gran)

	return stats

def stats_to_csv(stats):
	format = '%Y-%m-%d'
	print "Date,Low,High,Open,Close,Volume"
	for row in stats:
		date = datetime.datetime.fromtimestamp(row[0]).strftime(format)
		low = row[1]
		high = row[2]
		opn = row[3]
		close = row[4]
		volume = row[5]
		print '{},{},{},{},{},{}'.format(date, low, high, opn, close, volume)


if __name__ == '__main__':
	stats_to_csv(get_stats())


