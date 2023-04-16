import requests , os
import urllib.parse
from datetime import date

from woking_func import *
from config.config import configure_params

"""
I intentionally named it as 'woking' instead of working
"""

class color:
   PURPLE = '\033[95m'
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   CWHITE  = '\33[37m'
   RED = '\u001b[31m'

def get_file_contents(filename): #Reading api key function
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)
        return False


def retrive_data(topic):
    api_key = get_file_contents('config/API_KEY.txt')
    if not api_key == False:
        try:
            global title , content
            topic = urllib.parse.quote(topic) #url formatting given topic string
            # today = date.today() #getting current date
            url = "https://gnews.io/api/v4/search" #base URL
            params = {
                'token' : api_key, # API KEY
                'q' : topic, # query
                'lang' : configure_params.language , # limiting language to english 
                'country' : configure_params.country , # limiting country to india
                'max' : 1, # limiting to only one news 
                'from' : configure_params.from_date #setting news date
            }
            data = (requests.get(url , params=params)).json() #getting response in JSON 
            base = data['articles'][0] # setting base directory in retrived JSON 
            title = str(base['title']) 
            content = str(base['description']) 
            src_url = str(base['url']) # url of the news source 
            img_src = str(base['image']) # url of the image 
            publish_date = str(base['publishedAt']) # published date
            
            json_maker(title , data) # making a json backup file for news response
            os.system('cls' if os.name == 'nt' else 'clear') # if system is windows ('nt' is returned wehn os.name) then use 'cls' or use 'clear' ('clear' is used in all unix systems)  
            print(f"Title: {title} \n Content: {content} \n Source: {src_url} \n Article was published at: {publish_date} \n IMG SOURCE: {img_src}")
            return img_src

        except Exception as retrive_data_error:
            print(retrive_data_error)
            return False
    else:
        print(color.RED + "API KEY NOT VALID" + color.CWHITE)

def main(TOPIC):
    try:
        
        img_source = retrive_data(TOPIC) # Getting image url

        if not img_source == False: 
            imageName = name_create(title) # conditioning title to use as a image name returns "imageName" as a universal file name 
        
            if not imageName == False:
                is_image_downloaded = img_downloader(img_source , imageName) # Downloading image returns "True" if downloaded
        
                if not is_image_downloaded == False:
                    borders_added = add_borders(imageName) # adds borders to image returns "True" if added

                    if not borders_added == False:
                        is_resized = resize(imageName) # resizes image returns "True" if resized

                        if not is_resized == False:
                            is_image_pasted = pasteimg(imageName) #pastes image returns "True" if pasted

                            if not is_image_pasted == False:
                                written = write(imageName , title)
                                write_content(imageName , content)
        print(color.GREEN + "Successfully Created Images" + color.CWHITE)

    except Exception as main_error:
        print(color.RED + "main error: " + str(main_error) + color.CWHITE)


os.system('cls' if os.name == 'nt' else 'clear')
main(str(input("ENTER TOPIC: ")))



# retrive_data('Cybersecurity')

