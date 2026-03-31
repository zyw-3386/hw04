#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import whisper
import pyaudio
import wave
import numpy as np

# 录音参数
DURATION = 5
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
OUTPUT_FILE = "temp.wav"

# 加载模型
model = whisper.load_model("base")

print(f"🎤 开始录音 {DURATION} 秒...")

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

frames = []
for i in range(0, int(RATE / CHUNK * DURATION)):
    data = stream.read(CHUNK)
    frames.append(data)

print("✅ 录音结束，正在识别...")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(OUTPUT_FILE, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# 识别
result = model.transcribe(OUTPUT_FILE, language="zh")
print("\n识别结果：")
print(result["text"])

