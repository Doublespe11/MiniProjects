# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:14:13 2019

@author: Michał
"""

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("alarm.wav")
play(song)