import json
import requests

class Argo():
	def __init__(self, server, username, password, verify):
		self.server = server 
		self.username = username 
		self.password = password
		self.verify = verify
		credentials = {"username": self.username, "password": self.password}
		data = json.dumps(credentials)
		self.s = requests.Session()
		r = self.s.post(f"{self.server}/api/v1/session", data=data, verify=self.verify)
		r_json = json.loads(r.text)
		self.token = r_json['token']
		self.headers = requests.structures.CaseInsensitiveDict()
		self.headers["Accept"] = "application/json"
		self.headers["Authorization"] = f"Bearer {self.token}"

	def account_info(self):
		
		r = self.s.get(f"{self.server}/api/v1/account", headers = self.headers, verify=self.verify)

		return json.loads(r.text)

	def can_i(self, resource, action, subresource):
		r = self.s.get(f"{self.server}/api/v1/account/can-i/{resource}/{action}/{subresource}", headers = self.headers, verify=self.verify)

		return json.loads(r.text)