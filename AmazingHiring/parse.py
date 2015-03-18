import re
import codecs

emails = set()
regex1 = '[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+'
regex2 = "[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}"
p = re.compile(regex2, re.MULTILINE | re.IGNORECASE)
iLine = 0
for name in ["1", "2"]:
	fIn = codecs.open(name, "r", "utf-8")
	for line in fIn:
		iLine += 1
		for part in line.split(' '):
			if len(part) < 100:
				for email in re.findall(p, part):
					if not email in emails:
						emails.add(email)
						print(len(emails), iLine)
	fIn.close()

fOut = open("emails", "w")
for email in emails:
	print(email, file=fOut)
