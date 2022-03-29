#-*-coding: utf-8 -*-
import requests
import json
import subprocess
import sys
import codecs
import os

class deepl:
	
	def voice(self,exe_path,text,id):
		cmd = f'{exe_path} -cid {id} -f {text}'
		subprocess.run(cmd,shell=True)

	def api(self,unknow):
		API_KEY = '#deeplapi_key'

		TEXT = unknow

		params = {
	    	        "auth_key": API_KEY,
	    	        "text": TEXT,
	    	        "source_lang": 'EN', 
	    	        "target_lang": 'JA' 
	    	    }

		request = requests.post("https://api-free.deepl.com/v2/translate", data=params) #フリー版のurlを使用しています
		result = request.json()
		
		with open(text, "w",encoding="UTF-8") as f:
			f.write(result["translations"][0]["text"])
		return 0


if __name__ == '__main__':
	path =input("exe絶対パス=")
	id = input("cid-id=")
	text = input("テキストファイルの絶対パス=")
	deepl = deepl()
	deepl.api(text)
	deepl.voice(path,cmd,id)