# ARISU
虎尾科技大學程式練功坊discord群的輔助機器人。


目前功能
- 在頻道內 tag 機器人開啟新對話

正在進行
- 群組管理整合
- 程式解題輔助
- Discord Online Judge 計畫


# 安裝
需求
- Python 3.11 以上
```env
aiohttp==3.9.5
aiosignal==1.3.1
annotated-types==0.6.0
attrs==23.2.0
cachetools==5.3.3
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
colorama==0.4.6
discord.py==2.3.2
frozenlist==1.4.1
google-ai-generativelanguage==0.6.2
google-api-core==2.19.0
google-api-python-client==2.128.0
google-auth==2.29.0
google-auth-httplib2==0.2.0
google-generativeai==0.5.2
googleapis-common-protos==1.63.0
grpcio==1.63.0
grpcio-status==1.62.2
httplib2==0.22.0
idna==3.7
multidict==6.0.5
numpy==1.26.4
opencv-python==4.9.0.80
pillow==10.3.0
proto-plus==1.23.0
protobuf==4.25.3
pyasn1==0.6.0
pyasn1_modules==0.4.0
pycparser==2.22
pydantic==2.7.1
pydantic_core==2.18.2
PyNaCl==1.5.0
pyparsing==3.1.2
python-dotenv==1.0.1
requests==2.31.0
rsa==4.9
tqdm==4.66.4
typing_extensions==4.11.0
uritemplate==4.1.1
urllib3==2.2.1
yarl==1.9.4
```

本地部屬這個專案

```bash
git clone https://github.com/nfu-csie-qiushawa/ARISU.git
cd ARISU
pip install -r requirements.txt
```

你需要配置你的.env檔案在專案目錄(記得把example拿掉)
```env
#Discord Setting
DISCORD_TOKEN=機器人的token #https://discord.com/developers/applications

#Gemini Setting
GEMINI_TOKEN=gemini的token #https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw

#Judge0 Setting (還沒實裝)
# JUDGE0_TOKEN=
# JUDGE0_TOKEN_HOST=
```
運行機器人
```bash
python main.py
```
