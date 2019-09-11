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
					self.pageR.update({word.lower():values})
				pageRankExist = self.pageR.get(word.lower(), -1)
				for w in token:
					if w != word:
						pageRankExist[2].append(w.lower())
				self.pageR.update({word.lower():pageRankExist})
		#print(self.pageR)

	def updateValorActual(self):
		for k, v in self.pageR.items():
			v[0] = v[1]
			self.pageR.update({k:v})
		#print(self.pageR)

	def printDiccionarioPageRank(self):
		for k,v in sorted(self.pageR.items(), key=lambda x: x[1][1]):
			print(k+" -> Actual: "+str(v[1])+" Anterior: "+str(v[1]))


	def doPageRank(self, iteraciones):
		self.definePageRankStructure()
		for x in range(iteraciones):
			self.updateValorActual()
			for key, values in self.pageR.items():
				PR  = 0 # se utiliza para guardar el valor del page rank
				PR_L = 0 # se utiliza para guardar el valor de PR(X)/L(X)
				for backLink in values[2]:
					backLink_link = self.pageR.get(backLink, -1)
					#print(backLink)
					#print(backLink_link)
					if len(backLink_link[2]) > 0:
						PR_L = backLink_link[0] / len(backLink_link[2])
					else:
						PR_L = backLink_link[0]
					PR += PR_L
				values[1] = PR
				self.pageR.update({key:values})
			print("----------------ITERACIÓN "+str(x+1)+"----------------")
			self.printDiccionarioPageRank()
			print("-------------------------------------------")

if __name__ == "__main__":
	n = int(input("Ingrese el número de iteraciones: "))
	p = PageRank()
	p.getTokenizeSentence()
	p.doPageRank(n)
    