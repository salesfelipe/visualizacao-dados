file = open("cc_requisitos_obrigatoras.csv")



# var links = [
# 				{ "source": "Um no", "target": "Outro no"}
# 		];

targets = []
sources = []

print "["
i = 0
for line in file:

	temp = line.split(",")
	if i == 1:
		print '{ "source": ' +  temp[0] + ', "target": ' + temp[1] + '},' 

	i = 1
print "]"