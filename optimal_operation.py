#!/usr/bin/env python
# optimal operation suggester class
# 2015aug09


class OptOps:

	opsStr = []
	lopsStr = []

	def __init__(self, inputfile):
		fr = open(inputfile, 'r')  # filename 2bchanged
		data = fr.read()
		data = data.split('\n')
		for line in data:
			if len(line) >= 1:  # avoid null string in the end of file
				self.opsStr.append(line)
				self.lopsStr.append(self.translate2lower(line))
		fr.close

	def translate2lower(self, opName):
		spl = opName.split()
		lowerOp = ""
		for splphrase in spl:
			if ("(" not in splphrase) and (")" not in splphrase):
				lowerOp = lowerOp + splphrase.lower()

		return lowerOp

	def clustering(self):
		prefix1 = []
		for ope in self.lopsStr:
			newprefix = True
			for pre in prefix1:
				if ope.startswith(pre[0]):
					pre.append(ope)
					newprefix = False
					break
			if newprefix:
				newpre = []
				newpre.append(ope[0])
				newpre.append(ope)

