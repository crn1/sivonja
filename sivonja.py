import os
import subprocess
from datetime import date
os.system('cls')

danas = date.today()

def pokreni_komandu(komanda):
    proces = subprocess.Popen(komanda, stdout=subprocess.PIPE, shell=True)
    (output, err) = proces.communicate()
    status = proces.wait()

print('=== Sivonja ===\n')

print('Sivonja kompresuje jezgro...')
pokreni_komandu('cd C:/laragon/www/wordpress/wp-content/plugins/ && zip -rq9 ../themes/planeta/inc/tgm/plugins/planeta-core planeta-core/* -x *.git*')

print('Sivonja kompresuje Planetu...')
pokreni_komandu('cd C:/laragon/www/wordpress/wp-content/themes/planeta/ && zip -rq9 %USERPROFILE%/Desktop/planeta_backup/planeta' + str(danas) + ' . -x *.git*')

for i in range(1, 4):
    print('Sivonja kopira jezgro u wordpress-demo-' + str(i) + '...')
    pokreni_komandu('cp -ruv C:/laragon/www/wordpress/wp-content/plugins/planeta-core/* C:/laragon/www/wordpress-demo-' + str(i) + '/wp-content/plugins/planeta-core/')
    print('Sivonja kopira Planetu u wordpress-demo-' + str(i) + '...')
    pokreni_komandu('cp -ruv C:/laragon/www/wordpress/wp-content/themes/planeta/* C:/laragon/www/wordpress-demo-' + str(i) + '/wp-content/themes/planeta/')

print('Sivonja zavrsio!')
