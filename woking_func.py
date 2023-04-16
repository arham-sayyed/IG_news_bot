# Import the Image and ImageDraw modules from the PIL library
from PIL import Image, ImageDraw , ImageFont
import time , urllib.request , os , json
from pprint import pprint
from config.config import *

"""
I intentionally named it as 'woking' instead of working
"""

class color:
   PURPLE = '\033[95m'
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   CWHITE  = '\33[37m'
   RED = '\u001b[31m'

# demo = "This code first splits the input string into a list of words. Then it loops through the words and adds them to a temporary string until the length of the temporary string is greater than 6 words. When this happens, it appends the temporary string to a list of smaller strings and clears the temporary string. Finally, it appends the remaining words in the temporary string to the list of smaller strings and prints the result."
# title = "This code first splits the input string into a list of words. Then it loops through the words and adds them to a temporary string until the length of the "

def name_create(sep_name):
    try:
        name_file = sep_name.replace(" " , "-")
        name_file = name_file.replace( "." , "")
        name_file = name_file.replace("<" , "")
        name_file = name_file.replace(">" , "")
        name_file = name_file.replace(":" , "")
        name_file = name_file.replace('"' , "")
        name_file = name_file.replace("/" , "")
        name_file = name_file.replace("\\" , "") #escaping backslash "\"
        name_file = name_file.replace("|" , "")
        name_file = name_file.replace("?" , "")
        name_file = name_file.replace("*" , "")
        name_file = name_file.replace("%" , "")
        name_file = name_file.replace("#" , "")
        name_file = name_file.replace("@" , "")
        name_file = name_file.replace("!" , "")
        name_file = name_file.replace("}" , "")
        name_file = name_file.replace("{" , "")
        name_file = name_file.replace("+" , "")
        name_file = name_file.replace("-" , "")
        name_file = name_file.replace("=" , "")
        name_file = name_file.replace(")" , "")
        name_file = name_file.replace("(" , "")
        name_file = name_file.replace("&" , "")
        name_file = name_file.replace("$" , "")
        name_file = name_file.replace("_" , "")
        name_file = name_file.replace("'" , "")
        name_file = name_file.replace("`" , "")
        name_file = name_file.replace("~" , "")
        name_file = name_file.replace(";" , "")
        name_file = name_file.replace("," , "")
        name_file = name_file.replace("[" , "")
        name_file = name_file.replace("]" , "")
        name_file = "output/" + name_file + ".jpg"
        print(color.GREEN + name_file + color.CWHITE)
        return name_file

    except Exception as naming_error:
        print(color.RED + "naming error: " + str(naming_error) + color.CWHITE)
        return False

# From now our file will be called as variable name_file

def img_downloader(img_url , file_name):
    try:
        if not img_url is None and not file_name is None:
            urllib.request.urlretrieve(img_url , file_name) #saving the file with name = file_name which will be the name_file returned by name_create
            print(color.GREEN + "Image Downladed Successfully!" + color.CWHITE)
            return True
        else:
            print(color.RED + "URL OR name_file NOT FOUND!" + color.CWHITE)
            return False
    except Exception as img_downloading_error:
        print(color.RED + " image downloading error" + str(img_downloading_error) + color.CWHITE)
        return False

def add_borders(new_image):
    try:
        im = Image.open(new_image)
        draw = ImageDraw.Draw(im)
        width , height = im.size
        draw.rectangle([(0, 0) , (width, height)], outline=(0, 0, 0), width=7)
        draw.rectangle([(10, 10), (width - 10, height - 10)], outline=(0, 0, 0), width=5)
        im.save(new_image)
        im.close()
        print(color.GREEN + 'Successfully added borders! ' + color.CWHITE)
        return True
    except Exception as error_in_border:
        im.close()
        print(color.RED + str( "error in add_borders" + str(error_in_border)) + color.CWHITE)
        return False

def resize(new_image):
    try:
        im = Image.open(new_image)
        width , height = im.size
        new_width = configure_resize.width
        new_height = configure_resize.height
        # new_height = int(new_width * height / width)
        im = im.resize((new_width, new_height))
        im.save(new_image)
        im.close()
        print(color.GREEN + 'Successfully Resized Image!' + color.CWHITE)
        return True
    except Exception as resize_error:
        im.close()
        print(color.RED + str("error in resize: " + str(resize_error)) + color.CWHITE)
        return False

def pasteimg(front_img):
    try:
        try:
            background_image = Image.open(configure_pasteimg.bg_img) 
            front_image = Image.open(front_img) 
            background_image.paste(front_image , (configure_pasteimg.bg_img_pst_cordinate_x , configure_pasteimg.bg_img_pst_cordinate_y))
            background_image = background_image.convert("RGB")
            background_image.save(front_img)
            background_image.show()
            print(color.GREEN + "Successfully Pasted Images" + color.CWHITE)
            return True
        except IOError as image_opening_error:
            print(color.RED + str("error in image opening in pasteimg: " + image_opening_error) + color.CWHITE)
            return False
    except Exception as image_pasting_error:
        print(color.RED + "Failed in Pasting Images" + color.CWHITE)
        background_image.close()
        front_image.close()
        print(str(image_pasting_error))
        return False

def fontCalcky(txt , in_image):
    try:
        image = Image.open(in_image)
        draw = ImageDraw.Draw(image)
        fontsize = 1
        img_fraction = configure_fontCalcky.image_fraction 
        font = ImageFont.truetype("comic-sans-ms/ComicSansMSBold.ttf", fontsize)
        while font.getsize(txt)[0] < img_fraction*image.size[0]:
            fontsize += 1
            font = ImageFont.truetype("comic-sans-ms/ComicSansMSBold.ttf", fontsize)
            # optionally de-increment to be sure it is less than criteria
        fontsize -= 1
        font = ImageFont.truetype("comic-sans-ms/ComicSansMSBold.ttf", fontsize)
        print( color.PURPLE + "Finalized font size: " + str(fontsize) + color.CWHITE)
        return font
    except Exception as fontCalcky_error:
        print(color.RED + str( "error in font calcky:" + str(fontCalcky_error)) + color.CWHITE)
        return False

def breaker(my_string):
    try:
        global smaller_strings
        words = my_string.split()
        smaller_strings = []
        temp_string = ""
        string = ""
        for word in words:
            temp_string += (word + (" "))     
            if len(temp_string.split()) > configure_breaker.words_limit:
                smaller_strings.append(temp_string + "\n")
                temp_string = ""    
        smaller_strings.append(temp_string)
        print(smaller_strings)
        return string.join(smaller_strings)
    except Exception as breaker_error:
        print(color.RED + str("error in breaker: " + str(breaker_error)) + color.CWHITE)

def write(inp_image , inp_text):
    image = Image.open(inp_image)
    draw = ImageDraw.Draw(image)
    width , height = image.size
    text = (breaker(inp_text)) # calling breaker 
    font_obj = fontCalcky(smaller_strings[0] , inp_image) # directly getting the "font = ImageFont.truetype("arial.ttf", fontsize)"
    draw.text((configure_write.write_headline_cordinate_x , configure_write.write_headline_cordinate_y) , text , (255, 255, 255) , font = font_obj)
    image.save(inp_image)

def write_content(inp_image , inp_text):
    image = Image.open(inp_image)
    draw = ImageDraw.Draw(image)
    width , height = image.size
    text = (breaker(inp_text)) # calling breaker 
    font_obj = fontCalcky(smaller_strings[0], inp_image) # directly getting the "font = ImageFont.truetype("arial.ttf", fontsize)"
    draw.text((configure_write_content.write_content_cordinate_x , configure_write_content.write_content_cordinate_y) , text , (255, 255, 255) , font = font_obj)
    image.save(inp_image)

def json_maker(title , json_data):
    try:
        fileID = name_create(title)
        fileID = fileID.replace("output/" , "")
        fileID = fileID.replace(".jpg" , "")
        json_path = f"json-backup/{str(fileID)}.json"
        is_file_exists = os.path.exists(json_path)
        
        if is_file_exists == True:
            print(color.RED + str("This news article is already retrived... \n Exiting Process... ") + color.CWHITE)
            exit()

        else:
            with open(json_path , "w") as jsonTempData:
                pprint(json_data, stream = jsonTempData)
                
                # beautify_json = json.loads(json_data)
                # print(beautify_json)
                # jsonTempData.write(str(json.dumps(beautify_json, indent=4)))

                print(color.GREEN + "JSON file Created Successfully! fileID: " + str(fileID) + color.CWHITE)
    
    except Exception as json_maker_error:
        print(color.RED + "Error in json_maker: " + str(json_maker_error) + color.CWHITE)
        return False
