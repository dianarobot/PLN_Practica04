#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diana Rocha Botello
"""
from AnalisisFrecuencias import AnalisisFrecuencia

class PageRank():
	def __init__(self):
		self.a = AnalisisFrecuencia()
		self.pageR = {}

	def getTokenizeSentence(self):
		self.a.tokenizeFile("analizame.txt")
		self.a.reduccionDimensionalidadBySentence()

	def definePageRankStructure(self):
		for token in self.a.tokenListbySentence:
			i=0
			for word in token:
				pageRankExist = self.pageR.get(word.lower(), -1)
				if pageRankExist == -1:
					values = []
					values.append(0)
					values.append(1)
					values.append([])
					if (i+1) < len(token):
						values[2].append(token[i+1].lower())
					if (i-1) > -1:
						values[2].append(token[i-1].lower())
					self.pageR.update({word.lower():values})
				else:
					if (i+1) < len(token):
						pageRankExist[2].append(token[i+1].lower())
					if (i-1) > -1:
						pageRankExist[2].append(token[i-1].lower())
					self.pageR.update({word.lower():pageRankExist})
				i+=1
		print(self.pageR)

	def updateValorActual(self):
		for k, v in self.pageR.items():
			v[0] = v[1]
			self.pageR.update({k:v})
		#print(self.pageR)

	def doPageRank(self, iteraciones):
		self.definePageRankStructure()
		for x in range(iteraciones):
			self.updateValorActual()
			for key, values in self.pageR.items():
				PR  = 0 # se utiliza para guardar el valor del page rank
				PR_L = 0 # se utiliza para guardar el valor de PR(X)/L(X)
				for backLink in values[2]:
					backLink_link = self.pageR.get(backLink, -1)
					print(backLink)
					print(backLink_link)
					if len(backLink_link[2]) > 0:
						PR_L = backLink_link[0] / len(backLink_link[2])
					else:
						PR_L = backLink_link[0]
					PR += PR_L
				values[1] = PR
				self.pageR.update({key:values})
			print("----------------ITERACIÓN "+str(x)+"----------------")
			print(self.pageR)
			print("-------------------------------------------")
		print(self.pageR)

if __name__ == "__main__":
	p = PageRank()
	p.getTokenizeSentence()
	p.doPageRank(2)