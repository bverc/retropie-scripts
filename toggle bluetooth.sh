#!/bin/bash

bluetooth=$(rfkill -r -n -o soft list bluetooth)

if [ $bluetooth = "blocked" ] ; then
  rfkill unblock bluetooth
  echo "bluetooth unblock"
else
  rfkill block bluetooth
  echo "bluetooth block"
fi
