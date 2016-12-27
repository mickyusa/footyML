import subprocess
import glob
import os

## Scrapping all data
'''
for i in range(1993,2017,1):
	y = i + 1
	i, y = str(i), str(y)
	i, y = i[-2:], y[-2:]
	url = 'http://www.football-data.co.uk/mmz4281/{0}{1}/data.zip'.format(i,y)
	fileName = '{0}{1}.zip'.format(i,y)
	destFolder = '{0}{1}'.format(i,y)
	subprocess.check_output(['wget', url, '-O', fileName])
	subprocess.check_output(['unzip', fileName, '-d', destFolder])
	for fl in glob.glob("*.zip"):
		os.remove(fl)
'''

## CSV  

for fl in glob.glob("*/E0.csv"):
	