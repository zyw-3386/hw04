# hw04 开源语音识别 ASR 调研与实现
任务一：
大模型Chat gpt生成文案，详见text_gen.md文件

任务二：（剪映克隆音频，详见网盘链接）
登录剪映电脑版，点击AI视频生成，进入即梦AI网页，模式选择配音生成，点克隆声音，上传录好的音频，并输入配音文案（任务一），生成之后选择自己喜欢的音频文件下载。

任务三：（详见experiment_log.md文件）
安装环境:
运行“conda create -n whisper-env python=3.10”
运行“conda activate whisper-env”
运行“pip install openai-whisper”
运行“conda install ffmpeg”
运行“pip install pyaudio”
本地音频识别：
运行“python asr_test.py”得出结果
运行“python realtime.py”得出结果
