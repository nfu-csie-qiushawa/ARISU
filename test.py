import PIL.Image,requests,os
from io import BytesIO
import google.generativeai as genai
api_key = os.getenv("GEMINI_TOKEN")
print(os.getenv("GEMINI_TOKEN"))
genai.configure(api_key = api_key)
response = requests.get("https://cdn.discordapp.com/attachments/1176160558819586120/1238143755257905234/GNGslbcWsAAufCd.png?ex=663e36ba&is=663ce53a&hm=1f85a2c488dcaa9dc2c2112d0b96d63d35cab0aaa6c780dc58ff036d64f8d0ba&")
img = PIL.Image.open(BytesIO(response.content))

model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)

print(response.text)