from urllib2 import Request, urlopen
import urllib2, json, time






class Utils(object):

	@staticmethod
	def request(symbol):

		request = 'http://www.google.com/finance/info?infotype=infoquoteall&q=' + symbol
		
		try:
			content =json.loads( urlopen(Request(request)).read().decode('utf-8')[4:])
		except urllib2.HTTPError, err:
  			if err.code == 400:
  				return False
		else:
			return content


	@staticmethod
	def get_value(content, key):
		return content[0][key]





class Stock():

	def __init__(self, symbol):

		data = Utils.request(symbol)
		if data == False:
			raise Exception
		else:
			self._symbol    = Utils.get_value(data, 't')
			self._id 	    = Utils.get_value(data, 'id')
			self._exchange  = Utils.get_value(data, 'e')
			self._name      = Utils.get_value(data, 'name')
			self._type      = Utils.get_value(data, 'type')


	def getCurrentPrice(self):
		data = Utils.request(self._symbol)
		return Utils.get_value(data, 'l')


	def getValue(self, value):
		data  = Utils.request(self._symbol)
		return Utils.get_value(data, value)






class Historical(Stock):


	@staticmethod
	def getHistorical():
		print 'gh'


	@staticmethod
	def saveHistorical():
		print 'sh'








# ========================================================================================================================

msft = Stock('msft')
aapl = Stock('aapl')
goog = Stock('goog')
fb = Stock('fb')

print 'msft price: ' + msft.getCurrentPrice()
print 'aapl price: ' + aapl.getCurrentPrice()
print 'goog price: ' + goog.getCurrentPrice()
print 'fb price: ' + fb.getCurrentPrice()

print 'msft hi52: ' + msft.getValue('hi52')
print 'msft lo52: ' + msft.getValue('lo52')

msft.getHistorical()

# TODO :
# - multiple stocks, move to list/array, and call prices only once using concatonated request string



