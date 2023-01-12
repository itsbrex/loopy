import matplotlib.pyplot as plt
import numpy as np
from loopy import LoopyPreset, LoopyPatternCore, PRESET_DIR, DEFAULT_SR, preview_chord, LoopySidechain
from loopy.utils import preview_wave, seq_note_parser
import os
import librosa
"""
lead = LoopyPreset(os.path.join(PRESET_DIR, 'Ultrasonic-LD-Stars.wav'))
# preset.preview('A5')

pattern_type = LoopyPatternCore(num_bars=4)
pattern_type.add_note('G4', 1/4, 0, lead)
pattern_type.add_note('G4', 1/4, 1, lead)
pattern_type.add_note('A4', 1/4, 2, lead)
pattern_type.add_note('B4', 1/8, 3, lead)
pattern_type.add_note('D5', 1/4, 3.5, lead)
pattern_type.add_note('D5', 1/4, 4.5, lead)
pattern_type.add_note('B4', 1/8, 5.5, lead)
pattern_type.add_note('D5', 1/4, 6, lead)
pattern_type.add_note('E5', 1/4, 7, lead)

y = pattern_type.render()
# y, sr = librosa.load('./dry.wav', sr=44100, mono=False)
# y = np.transpose(y)
# Design filter

from loopy.effect import LoopyLowpass, LoopyHighpass, LoopyReverb

lp = LoopyHighpass(freq=500)
y = lp(y)
# print(y_filted.shape)

rv = LoopyReverb(wet_level=0.25)
y_reverb = rv(y)
# print(y_reverb.shape)

preview_wave(y)
preview_wave(y_reverb)

from loopy import LoopySidechain
sides = LoopySidechain(interp_order=2)
sides.forward(np.random.rand(DEFAULT_SR*15, 2))

seq = [84, 84, 84, 0, 76, 76, 76, 0, 76, 76, 76, 0, 74, 74, 72, 72, 79, 79, 72, 72, 72, 0, 74, 74, 74, 0, 74, 0, 74, 0, 72, 72, 76, 76, 76, 0, 84, 84, 84, 0, 84, 0, 84, 0, 81, 0, 79, 0, 81, 0, 79, 79, 79, 0, 79, 79, 79, 0, 79, 0, 79, 0, 76, 0, 81, 81, 81, 0, 81, 81, 81, 0, 81, 0, 81, 0, 79, 0, 76, 0, 79, 0, 79, 79, 79, 0, 76, 76, 76, 0, 76, 0, 74, 0, 72, 0, 74, 74, 74, 0, 81, 81, 81, 0, 81, 0, 81, 81, 81, 0, 79, 79, 79, 0, 0, 0, 0, 0, 0, 0, 0, 0, 76, 0, 74, 0, 72, 0]
notes = seq_note_parser(seq)
print(notes)
"""
key_name_list = ('A2', 'A3', 'C4', 'E4', 'G4')
y = preview_chord(key_name_list, play_now=False)

sd = LoopySidechain(attain=0.3, interp_order=2)

y = sd(y)
preview_wave(y)