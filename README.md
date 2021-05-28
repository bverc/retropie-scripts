# RetroPie Scripts

Useful bash scripts for use on RetroPie systems

Download the scripts:

    cd ~
    git clone https://github.com/bverc/retropie-scripts scripts

- `restart emulationstation.sh` Restart Emulation Station
- `safe shutdown.sh` Perform safe shutdown of the system
- `toggle bluetooth.sh` Turn Bluetooth on or off
- `toggle wifi.sh` Turn wifi on or off
- `toggle mute.sh` Mute or Unmute speakers
- `volume up.sh` Increase volume by 10%
- `volume down.sh` Decrease volume by 10%

## Usage

### 1. Run from bash

    cd scripts
    bash toggle\ mute.sh

### 2. Symlink into RetroPie Menu

Symlink scripts into retropiemenu folder so they are accessable from the Emulation Station menus

    ln -s ~/scripts/toggle\ mute.sh ~/RetroPie/retropiemenu/
    
### 3. Create new System for scripts

Create a new system in Emulation Station so all scripts appear in their own group.

Copy default es_systems.cfg and edit to ensure it is not replaced during upgrade

    sudo cp /etc/emulationstation/es_systems.cfg /opt/retropie/configs/all/emulationstation/es_systems.cfg
    sudo vi /opt/retropie/configs/all/emulationstation/es_systems.cfg
    
Add the following system entry:
```xml
  <system>
    <name>scripts</name>
    <fullname>Scripts</fullname>
    <path>/home/pi/scripts</path>
    <extension>.sh</extension>
    <command>bash %ROM%</command>
    <platform/>
    <theme>scripts</theme>
  </system>
```

restart emulationstation or reboot
    
If you wish, you can [create a theme for the new system](https://retropie.org.uk/docs/Add-a-New-System-in-EmulationStation/#step-2-create-a-theme-for-the-new-system) 
    
### 4. Run script from GPIO

Run a python script to run a bash script on GPIO button press. Some examples are provided:

- `gpio-script.py` maps scripts to GPIOs and runs script each time paired GPIO is pressed
- `gpio-shutdown.py` detects button press, waits 2 seconds and checks again before shutting down system

To run at boot, add to crontab.

    crontab -e
    
At the bottom of the file, add the line:

    @reboot python /home/pi/scripts/gpio-script.py

reboot
