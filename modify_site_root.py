import re, os

httpdFile = open('/etc/apache2/httpd.conf', 'r')
httpdFile_new = open('/etc/apache2/httpd.conf_new', 'w')
siteRoot = raw_input('Enter the new site root: ')
replacements = {'^DocumentRoot ".+"$': 'DocumentRoot "{0}"'.format(siteRoot), '^\<Directory ".+"\>$': '<Directory "{0}">'.format(siteRoot)}

for line in httpdFile:
    for src, target in replacements.iteritems():
        line = re.sub(src, target, line)
    httpdFile_new.write(line)
httpdFile.close()
httpdFile_new.close()

os.remove('/etc/apache2/httpd.conf')
os.rename('/etc/apache2/httpd.conf_new', '/etc/apache2/httpd.conf')