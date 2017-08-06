from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_silence
# from pydub.playback import play

# sound = AudioSegment.from_file("10_Hours_of_Indoor_Shooting_Range_Small_Arms_Fire [GREY NOISE].wav", format="wav")
# sound = AudioSegment.from_file("gun_sounds_part1.wav", format="wav")
sound = AudioSegment.from_file("DOGS_BARKING_1_Hour_[random natural].wav", format="wav")
# sound = AudioSegment.from_file("dog_sounds_part1.wav", format="wav")

chunks = split_on_silence(
    sound,

    # split on silences longer than 1000ms (1 sec)
    min_silence_len=1000,

    # anything under -16 dBFS is considered silence
    silence_thresh=-16, 

    # keep 200 ms of leading/trailing silence
    keep_silence=200
)

output_chunks = [chunks[0]]
target_length = 4 * 1000

for chunk in chunks[1:]:
    if len(output_chunks[-1]) < target_length:
        output_chunks[-1] += chunk
    else:
        # if the last output chunk is longer than the target length,
        # we can start a new one
        output_chunks.append(chunk)

seconds_of_silence = AudioSegment.silent(duration=2500) # or be explicit
second_of_silence = AudioSegment.silent(duration=1000) # or be explicit

for i, chunk in enumerate(chunks):
    chunk_name = "dog_sounds/chunk{0}_3.wav".format(i)
    print("exporting", chunk_name)
    combined = second_of_silence + chunk + seconds_of_silence
    combined.export(chunk_name, format="wav")

    