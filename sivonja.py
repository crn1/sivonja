import os
import subprocess
os.system('cls')

def pokreni_komandu(komanda):
    proces = subprocess.Popen(komanda, stdout=subprocess.PIPE, shell=True)
    (output, err) = proces.communicate()
    status = proces.wait()

print('=== Sivonja ===\n')

print('Sivonja kompresuje jezgro...')
pokreni_komandu('tar --force-local --exclude-vcs --overwrite -C C:/laragon/www/wordpress/wp-content/plugins/ -cf C:/laragon/www/wordpress/wp-content/themes/planeta/inc/tgm/plugins/planeta-core.zip planeta-core')

for i in range(1, 3):
    print('Sivonja kopira Planetu u wordpress-demo-' + str(i) + '...')
    pokreni_komandu('cp -ruv C:/laragon/www/wordpress/wp-content/themes/planeta/* C:/laragon/www/wordpress-demo-' + str(i) + '/wp-content/themes/planeta/')

print('Sivonja kompresuje Planetu...')
pokreni_komandu('tar --force-local --exclude-vcs --overwrite -C C:/laragon/www/wordpress/wp-content/themes/planeta -cf planeta.zip .')

print('Sivonja zavrsio!')
