import os, csv, re

locales = { 'en' : 'en-US',
			'da' : 'da-DK', 
			'de' : 'de-DE',
			'fr' : 'fr-FR',
			'it' : 'it-IT',
			'nb' : 'nb-NO',
			'pl' : 'pl-PL',
			'sv-SE' : 'sv-SE' }

def mkdir(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)

''' Convert CSV to .strings files '''
def csv2strings(file, locale, dir):
	lproj = '{}/{}.lpoj'.format(dir, locale)
	lfile = '{}/Localizable.strings'.format(lproj)
	
	mkdir(lproj)
    
	fs = open(lfile, 'w') 
	with open(file, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[1]: 
				fs.write('"{}"="{}";\n'.format(row[0], re.sub(r'%\$\+s', '%@', row[1])))
	fs.close()
	print lfile
	
''' Convert CSV to xml files '''
def csv2xml(file, locale, dir):
	values = '{}/values-{}'.format(dir, locale)	
	lfile = '{}/strings.xml'.format(values)
	
	mkdir(values)
    
	fs = open(lfile, 'w')
	fs.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
	fs.write('<resources>\n')
	
	with open(file, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[1]: 
				fs.write('\t<string name="{}">{}</string>\n'.format(row[0], row[1]))
			
	fs.write('</resources>')
	fs.close();
	print lfile

''' Convert CSV to multiple CSV '''
def csv2csvs(file):
	fs = {};
	for code, locale in locales.items():
		print code
		print locale
		fs[code] = open('{}.csv'.format(locale), 'w')
		
	with open(file, 'rb') as f:
		reader = csv.reader(f)
		csv_content = list(reader)
		texts = [csv_content[i] for i in range(1, len(csv_content))]
		
		for text in texts:
			for code, locale in locales.items():
				index = csv_content[0].index(locale)
				fs[code].write('"{}","{}"\n'.format(text[0], text[index]))

	for code, locale in locales.items():
		fs[code].close()
	

if __name__ == '__main__':
	csv2csvs('translations.csv')

	ios_dir = 'ios'
	android_dir = 'android'
	
	''' iOS '''
	for locale, file in locales.items():
		csv2strings('{}.csv'.format(file), locale, ios_dir)
	
	''' Android '''
	for locale, file in locales.items():
		csv2xml('{}.csv'.format(file), locale, android_dir)