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
- 安裝 [git](https://git-scm.com/downloads)
- 安裝 [Python 3.11](https://www.python.org/downloads/) 以上
- 申請 [discord bot token](https://discord.com/developers/applications)
- 申請 [gemini api token](https://ai.google.dev/)
  
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
BOT_ID=機器人的id
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
