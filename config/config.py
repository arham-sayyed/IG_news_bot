
from datetime import date

"""
this is a config file, here you can modify the values to change the output,
try ctrl + click to see where the value is being used 
author: Arham Sayyed
GitHub: https://github.com/arham-sayyed/
Instagram: @_thatguywearinghoodie 
"""


class configure_params:
    language = "en"
    country = "in"
    from_date = date.today() #getting current date

class configure_resize:
    width = 1239
    height = 588

class configure_pasteimg:
    bg_img = "bg.png"
    bg_img_pst_cordinate_x = 346
    bg_img_pst_cordinate_y = 442

class configure_fontCalcky:
    image_fraction = 0.80

class configure_breaker:
    words_limit = 12

class configure_write:
    write_headline_cordinate_x = 141
    write_headline_cordinate_y = 118

class configure_write_content:
    write_content_cordinate_x = 145
    write_content_cordinate_y = 239