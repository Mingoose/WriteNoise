import music21
import wav2midi2wav.audio_to_midi_melodia as a2m

a2m.audio_to_midi_melodia('StarWars60.wav', 'StarWars60.mid', 120, smooth=0.25, minduration=0.1, savejams=False)
score = music21.converter.parse('StarWars60.mid')
key = score.analyze('key')
print(key.tonic.name, key.mode)