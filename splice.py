from pydub import AudioSegment
# sound = AudioSegment.from_file("10_Hours_of_Indoor_Shooting_Range_Small_Arms_Fire [GREY NOISE].wav", format="wav")
sound = AudioSegment.from_file("DOGS_BARKING_1_Hour_[random natural].wav", format="wav")

halfway_point = len(sound) // 22
first_half = sound[:halfway_point]

# create a new file "first_half.mp3":
first_half.export("dog_sounds_part1.wav", format="wav")