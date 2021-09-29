################User permissions################ 

# sudo ls 
# sudo su, exit
# adduser andzl
# deluser andzl
# passwd andzl
# deluser --remove-home andzl


# d rwx rwx rwx (user, group, other)
# root@mateo21-desktop:/home# ls -l
# total 24
# ---------- -- prop    grpProp
# drwx------  2 root    root    16384 2007-09-19 18:22 lost+found
# drwxr-xr-x 65 mateo21 mateo21  4096 2007-11-15 22:40 mateo21
# drwxr-xr-x  2 patrick patrick  4096 2007-11-15 23:00 patrick

# addgroup amis
# usermod -aG amis patrick ! 
# usermod -g amis patrick (patrick dans le groupe amis, attention : change le groupe de patrick)
# usermod -G amis,paris,collegues patrick
# usermod -g patrick patrick
# delgroup amis

# chown: gestion des propriétaires d'un fichier(seul par root)
# chown patrick rapport.txt
# chgrp amis rapport.txt
# chown patrick:amis rapport.txt
# chown -R mateo21:mateo21 /home/patrick/

# chmod : modifier les droits d'accès
# chmod 600 rapport.txt
# chmod g+w,o-w rapport.txt
# chmod go-r rapport.txt
# chmod u=rwx,g=r,o=- rapport.txt
# chmod -R 700 /home/mateo21

# drwxr-xr-x  2 nethasenfra network   6 Sep 24 15:07 netyunush
# chown -R netyunush:network /appnetautomation/users/netyunush
# chmod -R 755 /appnetautomation/users/netyunush