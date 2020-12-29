#! /bin/bash

if [ ! -f /etc/modprobe.d/snd-blacklist.conf ]; then
	echo 'blacklist snd_bcm2835' > /etc/modprobe.d/snd-blacklist.conf
fi

if [ -f /boot/config.txt ]; then
	sed -i -e 's/dtparam=audio=on/#\0/' /boot/config.txt
fi
