import json
import glob

result = []
for f in glob.glob("../data/*.json"):
    with open(f, "r") as infile:
        for line in infile.readlines():
            result.append(json.loads(line))

with open("../data/jobs.json", "w") as outfile:
    json.dump(result, outfile)
