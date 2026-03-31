#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import whisper

# 加载模型 (使用 medium 模型中文效果最好，也可以用 tiny 更快)
model = whisper.load_model("medium")

# 测试1：识别一个本地音频文件（请把路径换成你电脑上的实际音频文件路径）
# 你可以先录一句“你好，语音识别测试成功”的音频放到桌面，命名为 test.wav
result = model.transcribe(r"C:\Users\Administrator\Desktop\clone voice.mp3", language="zh")

# 打印结果
print("识别结果如下：")
print(result["text"])

