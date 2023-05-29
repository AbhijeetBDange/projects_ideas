""" TO AUTOMATE THE BROWSER RENDERING JAVASCRIPT """
import time
from selenium import webdriver 
from io import BytesIO
from selenium.webdriver.chrome.service import Service
""" TO ESTABLISH HANDSHAKE AND REQUESTING INFORMATION FROM THE SERVER """
import requests

""" TO SAVE IMAGES IN BYTES IO DATA TYPE"""
import io

""" PILLOW LIBRARY TO WORK WITH IMAGES """
from PIL import Image





PATH="C:\\Users\\abhij\\OneDrive\\Desktop\\projekt\\chromedriver.exe"

service = Service(PATH)

wd=webdriver.Chrome(service=service)



# img_url = "https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*"


def get_images_from_web(wd, delay , max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0,document.Element.body.scrollHeight);")
        time.sleep(delay)
    url = "https://www.google.com/search?q=cat+images&rlz=1C1ONGR_enIN1057IN1057&sxsrf=APwXEddA1x-K8Yr9jh_8jCkqLX6HDOeL3A:1685156955973&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjfo4HuwpT_AhUv-TgGHfPNBTsQ_AUoAXoECAIQAw&biw=1539&bih=746&dpr=1.25#imgrc=pVdGkMEfAeoiMM"

    wd.get(url)

    image_urls = set()

    skips = 0

    while(len(image_urls) < max_images):
        scroll_down(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME , "r48jcc pT0Scc iPVvYb")

        for img in thumbnails[len(image_urls) + skips :max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            images = wd.find_elements(By.CLASS_NAME, "r48jcc pT0Scc iPVvYb")

            for image in images:

                if image.get_attribute('src') in image_urls :

                    max_images +=1
                    skips +=1
                    break
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"found image {len(image_urls)}")
                    # download_image()
                    print()
    return image_urls







def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content

        """ THIS WILL STORING A FILE IN MEMORY """
        image_file = io.BytesIO(image_content)

        image = Image.open(image_file)

        # this will concate file path with file name
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f,"JPEG")
        

        print("DONE")
    except Exception as e:
        print("FAILURE", e)




urls = get_images_from_web(wd, 2 , 5)


for i, url in enumerate(urls):
    download_image("img/", url, str(i)+".jpg")
wd.quit()
        





