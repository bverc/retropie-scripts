# RetroPie Scripts

Useful bash scripts for use on RetroPie systems

Download the scripts:

    cd ~
    git clone https://github.com/bverc/retropie-scripts scripts

- **restart emulationstation.sh** Restart Emulation Station
- **safe shutdown.sh** Perform safe shutdown of the system
- **toggle bluetooth.sh** Turn Bluetooth on or off
- **toggle wifi.sh** Turn wifi on or off
- **toggle mute.sh** Mute or Unmute speakers
- **volume up.sh** Increase volume by 10%
- **volume down.sh** Decrease volume by 10%

## Usage

### 1. Run from bash

    cd scripts
    bash toogle mute.sh

### 2. Symlink into RetroPie Menu

Symlink scripts into retropiemenu folder so they are accessable from the Emulation Station menus

    ln -s safe\ shutdown.sh ~/RetroPie/retropiemenu
    
### 3. Run script from GPIO

Run a python script to run a script on GPIO button press. And example python script has been provided in `gpio-script.py`.

To run at boot, add to crontab.

    crontab -e
    
At the bottom of the file, add the line:

    @reboot python /home/pi/scripts/gpio-script.py

reboot
