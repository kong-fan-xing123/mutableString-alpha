#!/usr/bin/python3.10

class String():
	def __init__(self, object: str=''):
		self.__listofthestring = list(object)
	def __getitem__(self,index):
		try:
			return self.__listofthestring[index]
		except BaseException as ncerr:
			raise IndexError('string index out of range') from ncerr
	def __setitem__(self,index,value):
		try:
			self.__listofthestring[index]=value
		except BaseException as ncerr:
			raise IndexError('string index out of range') from ncerr
	def __str__(self) -> str:
		return ''.join(self.__listofthestring)
	def __repr__(self) -> str:
		return "'" + ''.join(self.__listofthestring) + "'"
	def __eq__(self, o: object) -> bool:
		return ''.join(self.__listofthestring) == o
	def __ne__(self, o: object) -> bool:
		return not self == o
	def __add__(self,o):
		try:
			return self.__class__(''.join(self.__listofthestring) + o)
		except:
			return NotImplemented
	def __radd__(self,o):
		try:
			return self.__class__(''.join(self.__listofthestring) + o)
		except:
			return NotImplemented
	def format(self,*pargs,**kwargs):
		res=''.join(self.__listofthestring)
		return self.__class__(res.format(*pargs,**kwargs))
	def __mul__(self,other):
		try:
			return self.__class__(''.join(self.__listofthestring) * other)
		except:
			return NotImplemented
	def __rmul__(self,other):
		try:
			return self.__class__(''.join(self.__listofthestring) * other)
		except:
			return NotImplemented



