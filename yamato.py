import pyautogui
from region import run
import pytesseract
import openai

#　画像から文字列抽出
def img_to_str(x, y, width, height):
    img = pyautogui.screenshot(region = (x, y, width, height))
    str = pytesseract.image_to_string(img, lang="jpn")
    scraping = "".join(str.split())
    print(scraping)
    img.save("test.png")
    return scraping

# chatgptに投げる
def main(x, y, width, height):
    openai.api_key = ""
    string = img_to_str(x, y, width, height)
    gpt_model = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": string}
        ]   
    )

    return string, f"{gpt_model}: {response['choices'][0]['message']['content']}"
    # print(response['usage'])

        


