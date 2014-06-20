import re, os

#This script modifies the apache site root.  Customize by modifying path to httpd.conf or replacement kv pairs.

httpdFilePath = '/etc/apache2/httpd.conf'
temporaryHttpdFilePath = '/etc/apache2/httpd.conf_new'

httpdFile = open(httpdFilePath, 'r')
httpdFile_new = open(temporaryHttpdFilePath, 'w')
siteRoot = raw_input('Enter the new site root: ')
replacements = {'^DocumentRoot ".+"$': 'DocumentRoot "{0}"'.format(siteRoot), '^\<Directory ".+"\>$': '<Directory "{0}">'.format(siteRoot)}

for line in httpdFile:
    for src, target in replacements.iteritems():
        line = re.sub(src, target, line)
    httpdFile_new.write(line)
httpdFile.close()
httpdFile_new.close()

os.remove(httpdFilePath)
os.rename(temporaryHttpdFilePath, httpdFilePath)