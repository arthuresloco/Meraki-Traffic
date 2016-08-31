import csv
from matplotlib import pyplot as plt

filename = 'traffic (1).csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	applications, sents, recieveds = [], [], []

	for row in reader:
		application = (row[0])
		sent = int(row[6])
		recieved = int(row[7])

		applications.append(application)
		sents.append(sent)
		recieveds.append(recieved)

print(applications)

for index, column_header in enumerate(header_row):
		print(index, column_header)

# Plot Data
fig = plt.figure(dpi=128, figsize = (10, 6))
plt.plot(recieveds, c = 'red')
plt.plot(sents, c='blue')
#plt.fill_between(recieveds, sents, facecolor = 'blue', alpha=0.1)

#format plot
plt.title("Application Sent and Recieved Data", fontsize=24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()



print(applications)
#print(sents)
#print(recieveds)