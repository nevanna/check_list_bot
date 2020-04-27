import sys
import os

def get_inf_bar(data)->str:
		labels = data["labels"]
		inf_bar = []
		nb = "**%s**" % str(data["id_nb"])
		inf_bar.append(nb)
		_str = ""
		if len(labels) > 0:
			for l in labels:
				_str += "*"+ l + "* "
		if len(data["author"]) > 0:
			a_str = "*author: "
			for a in data["author"]:
				a_str += a + " "
			a_str+="*"
			inf_bar.append(a_str)
		if len(data["assignee_to"]) > 0:
			to_str = "***assignee to: "
			for to in data["assignee_to"]:
				to_str += to + " "
			to_str += "***"
			inf_bar.append(to_str)
		fin = ""
		for fragment in inf_bar:
			fin+= fragment + " "
		fin+= "\n"
		return fin

class DiscordTable(object):
	def __init__(self, data:dict):
		print("recived data->")
		print(data)
		print("\n\n")
		for t in data:
			self.table_name = data[t]["version"]
			break		
		self.data = data
	
	def get_table(self)->str:
		full = ""
		table_name_raw = "```tex\n$ %s\n```" % self.table_name
		full += table_name_raw
		opened_tasks = self.get_opened_tasks()
		if len(opened_tasks) > 0:
			head_line_open = "\n```ini\n[opened tasks]\n```"
			full += head_line_open
			full += opened_tasks
		closed_tasks = self.get_closed_tasks()
		if len(closed_tasks) > 0:
			head_line_close = "\n```ini\n[closed tasks]\n```"
			full += head_line_close
			full += closed_tasks
		return full
	
	def get_opened_tasks(self)->str:
		even = True
		opened_task = ""
		
		for t in self.data:
			if self.data[t]["status"] == 1:
				if even:
					msg_row = '```css\n%s\n```' % self.data[t]["msg"]
				else:
					msg_row = '```yaml\n%s\n```' % self.data[t]["msg"]
				inf_bar = get_inf_bar(self.data[t])
				opened_task += msg_row + inf_bar
				even = not even
		return  opened_task

	def get_closed_tasks(self)->str:
		closed_tasks = ""
		for t in self.data:
			if self.data[t]["status"] == 3:
				raw = "~~%s~~\n" % self.data[t]["msg"]
				closed_tasks += raw
		return closed_tasks
