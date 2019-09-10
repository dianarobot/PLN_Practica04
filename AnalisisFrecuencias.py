#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diana Rocha Botello
"""
import nltk
import collections
import string
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

class AnalisisFrecuencia():

	def __init__(self):
		self.tokenListbySentence = []
		self.tokenList = []
		self.tokenListStemming = []
		self.tokenListLemmati = []
		self.diccionarioDF = {}
		self.lematizacionD = {}

	def tokenizeFile (self, fileName):
		toktok = ToktokTokenizer()
		# Tokenizador de oraciones
		es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
		with open(fileName, 'r', encoding='utf8') as f:
			content = f.read()
			# Obtener oraciones de un parrafo
			parrafo = content
			oraciones = es_tokenizador_oraciones.tokenize(parrafo)
			# Obtener tokens de cada oraciónn
			for s in oraciones:
				tokenSentence = toktok.tokenize(s)
				self.tokenListbySentence.append(tokenSentence)
				for t in tokenSentence:
					self.tokenList.append(t)
			f.close()

	def reduccionDimensionalidad(self):
		print("Número de Tokens Antes de la Reducción: "+str(len(self.tokenList)))
		for stopWord in stopwords.words("spanish"):
			for token in self.tokenList:
				if stopWord == token or  token in string.punctuation:
					self.tokenList.remove(token)
		print("Número de Tokens Después de la Reducción: "+str(len(self.tokenList)))

	def reduccionDimensionalidadBySentence(self):
		for stopWord in stopwords.words("spanish"):
			i=0
			for sentence in self.tokenListbySentence:
				for token in sentence:
					if stopWord == token.lower() or token in string.punctuation or token in ['¿','¡', '——']:
						self.tokenListbySentence[i].remove(token)
				i+=1
		print(self.tokenListbySentence)
