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

本地部屬這個專案

```bash
git clone https://github.com/nfu-csie-qiushawa/ARISU.git
cd ARISU
pip install -r requirements.txt
```

你需要配置你的.env檔案在專案目錄(記得把example拿掉)
```env
#TOKEN
DISCORD_TOKEN=機器人的token #https://discord.com/developers/applications
GEMINI_TOKEN=gemini的token #https://ai.google.dev/gemini-api/docs/api-key?hl=zh-tw
```
運行機器人
```bash
python main.py
```
