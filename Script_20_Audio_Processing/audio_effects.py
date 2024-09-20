from pydub import AudioSegment

beat = AudioSegment.from_wav('src/beat.wav')

beat_low = beat.low_pass_filter(2000)
beat_low.export('beat_low.wav')

beat_left = beat_low.pan(-1) # Playing more on the left speeker
beat_right = beat_low.pan(1) # Playing more on the right speeker
beat_left.export('beat_left.wav')

beat_final = beat_left + beat_right + beat_low
beat_final.export('beat_final.wav')