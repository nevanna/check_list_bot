import sys
import os
import json


# FD = "data_file2.json"
FD = "databasse.json"
class Storage(object):
	content = {}
	def __init__(self):
	# 	data = {"president3": {
	# 	"name": "Zaphod Beeblebrox",
	# 	"species": "Betelgeusian"
	# 	}
	# }
		self.get_storage()

	def get_storage(self):
		try:
			with open(FD, "r") as f:
				content_tmp = json.load(f)
				if not content_tmp or len(content_tmp.keys()) == 0:
					self.content = {}
				else:
					self.content = content_tmp
			# return self.content
		except Exception as e:
			with open(FD, "w") as f:
				json.dump(self.content, f)
				# return self.content

	def save_to_storage(self):
		print(self.content)
		print(type(self.content))
	# 	with open(FD, "w") as f:
	# # 	cool_data = json.dumps(data, separators=(',', ':'), sort_keys=True, indent=4)
	# 		print("try save")
	# 		print(self.content)
	# 		json.dump(self.content, f)

	def debug_send(self):
		super_string = ""
		for k in self.content:
			super_string += self.content[k]["msg"] + "\n"
		return super_string





