# import sounddevice as sd
# import numpy as np

# # Recording parameters
# duration = 5  # seconds
# sample_rate = 44100

# print("Recording...")
# audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
# sd.wait()  # Wait until recording is finished
# print("Recording complete")

# # audio_data now contains your recording as a NumPy array
# # print(f"Audio data shape: {audio_data.shape}")
# import sounddevice as sd
# print(sd.query_devices())  # List all devices
# print(sd.default.device)   # Show default input/output
import sounddevice as sd

# Replace `device_id` with a valid input device from `query_devices()`
sd.default.device = (1, None)  # Example: Use device ID 2 for input
sd.default.samplerate = 44100   # Set sample rate explicitly

print("Recording...")
audio_data = sd.rec(int(5 * 44100), samplerate=44100, channels=2)
sd.wait()
print("Done!")