#!/bin/bash

DEVICE=`amixer scontrols | grep -Po "(?<=')(Master|Speaker|HDMI|PCM)(?=')"`

amixer -M set $DEVICE 10%-
