#!/bin/bash

DEVICE=`amixer scontrols | grep -Po "(?<=')(Master|Speaker|HDMI|PCM)(?=')"`

amixer set $DEVICE toggle
