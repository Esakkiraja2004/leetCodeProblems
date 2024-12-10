words = ["$easy$","$problem$"]
seperators = "$"
r =[]
for x in words:
    r.append(x.split(seperators))
res = [item for sub in r for item in sub if item != ""]
print(res)