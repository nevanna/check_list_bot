# -*- coding: utf-8 -*-

import sys
import datetime
from storage.storage import Storage

from enum import Enum

status = {"undifined" : 0,
			"open" : 1,
			"progress" : 2,
			"closed" : 3,
			}

# class Status(Enum):
# 	is_undifined = 0
# 	is_open = 1
# 	is_closed = 2
# 	in_progress = 3

class Task(object):
	def __init__(self, arg, author):
		print(author)
		self.msg = ""
		self.id_nb = 0
		self.version = ""
		self.labels = []
		self.assignee_to = []
		self.author = [author]
		self.date_of_creation = {}
		self.status = status["undifined"]
		self.date_of_closing = {}
		s = ""
		for el in arg:
			s += str(el) + " "
		print(s)
		self._parse_str(s)
		self.set_date_of_creation()
		self.set_status("open")
		_task = self.get_task_as_dictionary()
		st = Storage()
		st.push_task(_task)
		# self.set_id_nb(idx)
		
	def print_params(self):
		params = [self.msg, self.id_nb, self.version, self.labels, self.assignee_to, self.author, self.date_of_creation, self.status, self.date_of_closing]
		# params = [self.msg, self.version, self.labels, self.assignee_to, self.status,]
		print(params)

	def set_status(self,st):
		self.status = status[st]
	def get_status(self):
		return self.status
	
	def set_date_of_creation(self):
		self.date_of_creation = self.time_dict(datetime.datetime.now())
		pass
	def get_date_of_creatino(self):
		return self.date_of_creation

	def set_label(self, label):
		self.labels.append(label)
	def get_labels(self):
		return self.labels
	
	def close_task(self):
		self.status = status["closed"]
		self.date_of_closing = self.time_dict(datetime.datetime.now())
	
	def set_author(self, who):
		self.author = who
	def get_author(self):
		return self.author
	
	# def set_id_nb(self, idx):
	# 	self.id_nb = idx
	
	# def get_id_nb(self):
	# 	return self.id_nb	
	

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
		"status": self.status,
		"date_of_closing": self.date_of_closing }
		return dic

	def time_dict(self, date_time):
		if not date_time:
			return{"year": 0,
			"month": 0,
			"day": 0,
			"hour":0, 
			"minute": 0,
			"second": 0}
		else:
			return {"year": date_time.year,
			"month": date_time.month,
			"day": date_time.day,
			"hour":date_time.hour, 
			"minute": date_time.minute,
			"second": date_time.second}
		# year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None
