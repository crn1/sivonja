import os
import subprocess
from datetime import date
os.system('cls')

def pokreni_komandu(komanda):
    proces = subprocess.Popen(komanda, stdout=subprocess.PIPE, shell=True)
    (output, err) = proces.communicate()
    status = proces.wait()

print('=== Sivonja ===\n')

print('Sivonja kompresuje jezgro...')
pokreni_komandu('tar --force-local --exclude-vcs --overwrite -C C:/laragon/www/wordpress/wp-content/plugins/ -cf C:/laragon/www/wordpress/wp-content/themes/planeta/inc/tgm/plugins/planeta-core.zip planeta-core')

print('Sivonja kompresuje Planetu...')
pokreni_komandu('tar --force-local --exclude-vcs --overwrite -C C:/laragon/www/wordpress/wp-content/themes/planeta -cf planeta.zip .')

print('Sivonja pravi bekap...')
danas = date.today()
pokreni_komandu('mkdir backup')
pokreni_komandu('tar --force-local --exclude-vcs --overwrite -C C:/laragon/www/wordpress/wp-content/themes/planeta -cf backup/planeta-' + str(danas) + '.zip .')

for i in range(1, 3):
    print('Sivonja kopira jezgro u wordpress-demo-' + str(i) + '...')
    pokreni_komandu('cp -ruv C:/laragon/www/wordpress/wp-content/plugins/planeta-core/* C:/laragon/www/wordpress-demo-' + str(i) + '/wp-content/plugins/planeta-core/')
    print('Sivonja kopira Planetu u wordpress-demo-' + str(i) + '...')
    pokreni_komandu('cp -ruv C:/laragon/www/wordpress/wp-content/themes/planeta/* C:/laragon/www/wordpress-demo-' + str(i) + '/wp-content/themes/planeta/')

print('Sivonja zavrsio!')
