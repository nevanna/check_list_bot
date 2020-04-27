import sys
import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./KEYS/check-list-bot-firebase-adminsdk-2b9fs-236aadf3f6.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# FD = "data_file2.json"
FD = "databasse.json"
class Storage(object):
	content = {}
	server = "funexpected"
	tables = 'tables'
	# def __init__(self):
	# 	self.get_storage()

	def get_storage_from_db(self, table_name):
		print("get_storage_from_db")
		col_ref = db.collection(self.server).document(self.tables).collection(table_name)
		d = col_ref.stream()
		if not d:
			print("no tables or documents")
		print("got_storage_from_db")
		print(d)
		print("here_8")
		return d
		# for t in d:
		# 	print(u'{} => {}'.format(t.id, t.to_dict()))
		# print("here_9")

	def get_idx(self, task):
		# return plus one because for users are more comfourtable to start count with 1
		d = self.get_storage_from_db(task["version"])
		idx = 1
		if not d:
			return 1
		print("here_10")
		for t in d:
			print(u'{} => {}'.format(t.id, t.to_dict()))
			idx += 1
			print("here_11_01", idx)
		print("here_11", idx)
		return idx

	def push_task(self, task):
		print(task)
		task["id_nb"] = str(self.get_idx(task))
		print("here_12", task["id_nb"])
		db.collection(self.server).document(self.tables).collection(task["version"]).add(task)

	# def update_task(self, task, new_data):
	# 	# later
	# 	d = self.get_storage_from_db(task)
	# 	for t in d:
	# 		l = t.to_dict()
	# 		if l["id_nb"] == task["id_nb"]:
	# 			db.collection(self.server).document(self.tables).collection(task["version"]).document(t.id).update(task)
	# 			break

	def get_table(self, table_name)->dict:
		table = self.get_storage_from_db(table_name)
		tasks = {}
		if table:
			print("i have table and try to workt with it")
			for t in table:
				# print(u'{} => {}'.format(t.id, t.to_dict()))
				tasks[str(t.id)] = t.to_dict()
				print(t.to_dict())
				print("here_9")
			print(tasks)
		return tasks
	
	def add_push(self, task):
		# Classified = db.collection("server").document('versions').set({"202.0" : "vers"})
		server = "funexpected"
		content = 'tables'
		table_name = '2.3.0'
		
		Classified = db.collection(server).document(content).collection(table_name).add({
		"message" :"msg",
		"from" : "anna",
		"date2": {"day": "20", "month" : "april"}
	})

	def add_anotherdb(self):
		doc_ref = db.collection(u'users').document(u'aturing')
		doc_ref.push().set({
			u'first': u'Alan',
			u'middle': u'Mathison',
			u'last': u'Turing',
			u'born': 1912
		})

	def read_data(self):
		doc_ref = db.collection(u'funexpected')
		doc = doc_ref.get()
		doc2 = doc_ref.stream()
		print(doc)
		print(doc2)
		# for el in doc:
		# 	print(el.to_dict())
		# print(doc.to_dict())

		col_ref = db.collection(u'funexpected').document('tables').collection("2.3.0")
		d = col_ref.stream()
		print(len(d))
		for t in d:
			print(u'{} => {}'.format(t.id, t.to_dict()))
