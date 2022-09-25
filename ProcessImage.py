
# imports
from platform import architecture
from PIL import Image, ImageDraw, ImageFont
import Archives
  
   
def coupons(database: dict, certificate: str, font_path: dict):
   
    for name in database['nomes']:
          
        text_y_position = 893
        text_x_position = 130
        text_color = "#f1552b"
        # open
        img = Image.open(certificate, mode ='r')
        img.load()
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3]) # 3 alpha channel
        img = background
   
        draw = ImageDraw.Draw(img)
   
        # font file (TTF)
        font = ImageFont.truetype(
            font_path['bold'],
            150 
        )
   
        draw.text(
            (
                text_x_position,
                text_y_position
            ),
            name,text_color,
            font = font        )

        #NomeCurso
        font = ImageFont.truetype(
            font_path['semibold'],
            92 
        )

        text_y_position = 1220
        text_x_position = 133 
        text_color = "#353435"

        draw.text(
            (
                text_x_position,
                text_y_position
            ),
            database['curso'],text_color,
            font = font        ) 


        #Instrutor
        font = ImageFont.truetype(
            font_path['regular'],
            56 #
        )

        text_y_position = 1400
        text_x_position = 144 
        text_color = "#353435"

        draw.text(
            (
                text_x_position,
                text_y_position
            ),
            database['instrutor'],text_color,
            font = font        )
            
        # Local 

        text_y_position = 1500
        text_x_position = 144       
        draw.text(
            (
                text_x_position,
                text_y_position
            ),
            database['local'],text_color,
            font = font        )  

        # Carga Horaria 

        text_y_position = 1600
        text_x_position = 144       
        draw.text(
            (
                text_x_position,
                text_y_position
            ),
            database['carga'],text_color,
            font = font        )  

        # Data 
        font = ImageFont.truetype(
            font_path['regular'],
            56 
        )
        text_y_position = 1700
        text_x_position = 144      
        draw.text(
            (
                text_x_position,
                text_y_position
            ),
            database['data'],text_color,
            font = font        )   

        # saves the image in png format
        img.save("static/data/pdf/{}.PDF".format(name)) 
  

def init(location):
    database = Archives.openArchive(location)
      
    # path to font
    FONT = {"bold": "fonts/Raleway-Bold.ttf", "semibold":"fonts/Poppins-SemiBold.ttf", "regular":"fonts/Poppins-Regular.ttf"}
      
    # path 
    CERTIFICATE = "static/img/template.png"
   
    coupons(database, CERTIFICATE, FONT)
    Archives.zipFile()