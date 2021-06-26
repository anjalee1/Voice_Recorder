
import sounddevice
from scipy.io.wavfile import write
import wavio


frequency = 44100
duration = 5
recording = sounddevice .rec(int(duration * frequency),
				samplerate=frequency, channels=2)
sounddevice .wait()
#using scipy
write("sc-recording.wav", frequency, recording)
#using wavio
wavio.write("wavio-recording.wav", recording, frequency, sampwidth=2)

#get sound device details
# a=sounddevice.query_devices(device=None,kind=None)
# print(a)
