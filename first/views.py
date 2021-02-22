import csv
import json
from django.shortcuts import render

# Create your views here.
def insert_words(request, *args, **kwagrs):
	if(request.method == "POST"):
		word = []
		word.append(request.POST["word"])
		with open("words.csv", "a", newline="") as cf:
			writer = csv.writer(cf, delimiter="|", )
			writer.writerow(word)

	file = open("words.csv", "r")
	lines = file.readlines()
	file.close()
	lines = [x.strip("\n") for x in lines]

	context = {
		"words": lines,
	}

	return render(request, "first/insert_word.html", context)


def paragraph_check(request, *args, **kwargs):
	file = open("words.csv", "r")
	lines = file.readlines()
	file.close()
	lines = [x.strip("\n") for x in lines]

	context = {
		"words": json.dumps(lines),
	}
	print(json.dumps(lines))
	return render(request, "first/paragraph.html", context)