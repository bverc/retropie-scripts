# RetroPie Scripts

Useful bash scripts for use on RetroPie systems

Download the scripts:

    cd ~
    git clone https://github.com/bverc/retropie-status-overlay scripts

- **restart emulationstation.sh** Restart Emulation Station
- **safe shutdown.sh** Perform safe shutdown of the system
- **toggle bluetooth.sh** Turn Bluetooth on or off
- **toggle wifi.sh** Turn wifi on or off
- **toggle mute.sh** Mute or Unmute speakers
- **volume up.sh** Increase volume by 10%
- **volume down.sh** Decrease volume by 10%

Use these scripts directly from bash, or you may symlink them into retropiemenu folder so they are accessable from the Emulation Station menus

    ln -s safe\ shutdown.sh ~/RetroPie/retropiemenu
