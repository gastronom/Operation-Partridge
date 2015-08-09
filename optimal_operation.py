#!/usr/bin/env python
# optimal operation suggester class
# 2015aug09


class OptOps:

	opsStr = []

	def __init__(self, inputfile):
		fr = open(inputfile, 'r')  # filename 2bchanged
		data = fr.read()
		data = data.split('\n')
		for line in data:
			if len(line) >= 1:  # avoid null string in the end of file
				# self.opsStr.append(line)
				self.opsStr.append(translate2lower(line))
		fr.close

	def translate2lower(self, opName):
		spl = opName.split()
		lowerOp = ""
		for splphrase in spl:
			if ("(" not in splphrase) and (")" not in splphrase):
				lowerOp = lowerOp + splphrase.lower()

		return lowerOp



