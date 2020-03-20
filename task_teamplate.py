# -*- coding: utf-8 -*-

import sys
import datetime


from enum import Enum

class Status(Enum):
	is_undifined = 0
	is_open = 1
	is_closed = 2
	in_progress = 3

class Task(object):
	def __init__(self, arg, idx, author):
		print(author)
		self.msg = ""
		self.id_nb = 0
		self.version = ""
		self.labels = []
		self.assignee_to = []
		self.author = [str(author.name) + "#" + str(author.discriminator)]
		self.date_of_creation = {}
		# self.status = Status.is_undifined
		self.date_of_closing = {}
		s = ""
		for el in arg:
			s += str(el) + " "
		print(s)
		self._parse_str(s)
		self.set_date_of_creation()
		# self.set_status(Status.is_open)
		print(idx)
		self.set_id_nb(idx)
		
	def print_params(self):
		params = [self.msg, self.id_nb, self.version, self.labels, self.assignee_to, self.author, self.date_of_creation, self.status, self.date_of_closing]
		# params = [self.msg, self.version, self.labels, self.assignee_to, self.status,]
		print(params)

	def set_status(self,status):
		self.status = status
	def get_status(self):
		return self.status
	
	def set_date_of_creation(self):
		self.date_of_creation = datetime.datetime.now()
		pass
	def get_date_of_creatino(self):
		return self.date_of_creation

	def set_label(self, label):
		self.labels.append(label)
	def get_labels(self):
		return self.labels
	
	def close_task(self):
		self.status = Status.is_closed
		self.date_of_closing = datetime.datetime.now()
	
	def set_author(self, who):
		self.author = who
	def get_author(self):
		return self.author
	
	def set_id_nb(self, idx):
		self.id_nb = idx
	def get_id_nb(self):
		return self.id_nb	
	

	def __extractor(self, s, i):
		while (s[i]!= ' ' and s[i] != '	'):
			i += 1
		return i
	#unparsed meesage
	def _parse_str(self, s):
		i = 0
		saw_version = False
		read_version = False
		read_labels = False
		read_who = False
		while i < len(s):
			if s[i] == '$' and saw_version == False:
				i+=1
				read_version = True
			if read_version == True and saw_version == False:
				while (s[i]!= ' ' and s[i] != '	'):
					# if not s[i].isnumeric() and s[i] != ".":
					self.version+=s[i]
					i += 1
				saw_version = True
				read_version = False
			if s[i] == "#":
				i+=1
				read_labels = True
			if read_labels:
				tmp_i = self.__extractor(s, i)
				self.labels.append(str(s[i:tmp_i:]))
				i = tmp_i
				read_labels = False
			if s[i] =='@':
				i+=1
				read_who = True
			if read_who == True:
				tmp_i_2 = self.__extractor(s, i)
				self.assignee_to.append(str(s[i:tmp_i_2:]))
				i = tmp_i_2
				read_who = False
			# print(read_labels, read_who, read_version)
			if read_labels == False and read_who == False and read_version == False:
				self.msg += s[i]
			i += 1

	def get_task_as_dictionary(self):
		# return self.status and create frome date tome a normal dict
		dic = {"msg" : self.msg,
		"id_nb": self.id_nb ,
		"version": self.version,
		"labels": self.labels,
		"assignee_to": self.assignee_to,
		"author": self.author,
		"date_of_creation": self.date_of_creation,
		# "status": self.status,
		"date_of_closing": self.date_of_closing }
		return dic

