import google.generativeai as genai
import os,discord,requests
from PIL import Image
import requests, json
from io import BytesIO
api_key = os.getenv("GEMINI_TOKEN")
print(os.getenv("GEMINI_TOKEN"))
genai.configure(api_key = api_key)
def askToGemini_text(message:str, chat:genai.ChatSession, channelId):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(change_history([message], "user", channelId))
    return response.text
def askToGemini_img(message:str, url, channelId):
    print(url)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    rgb_im = img.convert('RGB')
    change_history(message, 'user', channelId)
    model = genai.GenerativeModel('gemini-pro-vision')
    res = model.generate_content([message, rgb_im])
    return res.text
def change_history(res, role, channelId):
    with open("database\chat_history.json", 'r', encoding='utf-8') as db:
        data = json.load(db)
    if f"{channelId}" not in data["history"]:
        data["history"][f"{channelId}"]=[]
    data["history"][f"{channelId}"].append({
            'role':role,
            'parts':res
        })
    with open("database\chat_history.json", 'w', encoding='utf-8') as db:
        json.dump(data, db, indent=4)
    return data["history"][f"{channelId}"]
def get_history(channelId):
    with open("database\chat_history.json", 'r', encoding='utf-8') as db:
        data = json.load(db)
    return data["history"][f"{channelId}"]