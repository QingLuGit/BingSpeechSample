import sys, string, os, subprocess
for i in range(0, 22):
	try:
		subprocess.check_call([r"SpeechToText-WPF-Sample.exe", str(i)])
	except subprocess.CalledProcessError:
		print(i)
