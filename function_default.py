def askme(prompt,retries=4,complaint='please yes or not'):
	while True:
		msg = raw_input(prompt)
		if msg in ('y','yes','yeah'):
			return True
		if msg in ('n','none','not'):
			return False
		retries = retries-1
		if retries < 0 :
			raise IOError('You exceeds the limit')
		print complaint