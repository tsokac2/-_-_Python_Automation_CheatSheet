from pydub import AudioSegment

original = AudioSegment.from_wav('src/beat.wav')
print(type(original))
print(original)

reversed = original.reverse()
reversed.export('beat_reversed.wav')
reversed = reversed + 15

# print(dir(original))

first_two = original[0:2000]
first_two.export('first_two.wav')

print(len(original))

merged = original + AudioSegment.silent(1000) + reversed
merged.export('merged.wav')

