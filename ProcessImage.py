
# imports
from platform import architecture
from PIL import Image, ImageDraw, ImageFont
import Archives
  
   
def coupons(database: dict, certificate: str, font_path: dict):
   
    for name in database['nomes']:
          
        text_y_position = 893
        text_x_position = 130
        text_color = "#f1552b"
        # opens the image
        img = Image.open(certificate, mode ='r')
        img.load()
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3]) # 3 is the alpha channel
        img = background
   
        # creates a drawing canvas overlay 
        # on top of the image
        draw = ImageDraw.Draw(img)
   
        # gets the font object from the 
        # font file (TTF)
        font = ImageFont.truetype(
            font_path['bold'],
            150 # change this according to your needs
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
            92 # change this according to your needs
        )

        text_y_position = 1225
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
            56 # change this according to your needs
        )

        text_y_position = 1505
        text_x_position = 428 
        text_color = "#353435"

        draw.text(
            (
                text_x_position,
                text_y_position
            ),
            database['instrutor'],text_color,
            font = font        )
            
        # Local 

        text_y_position = 1616
        text_x_position = 333       
        draw.text(
            (
                text_x_position,
                text_y_position
            ),
            database['local'],text_color,
            font = font        )  

        # Carga Horaria 

        text_y_position = 1733
        text_x_position = 603       
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
            40 # change this according to your needs
        )
        text_width, _ = draw.textsize(name, font = font)
        image_width = 700
        text_y_position = 2125
        text_x_position = 333       
        draw.text(
            (
                295+(image_width - text_width)/2,
                text_y_position
            ),
            database['data'],text_color,
            font = font        )   

        # saves the image in png format
        img.save("static\data\pdf\{}.PDF".format(name)) 
  
# Driver Code
def init(location):
    database = Archives.openArchive(location)
      
    # path to font
    FONT = {"bold": "fonts/Raleway-Bold.ttf", "semibold":"fonts/Poppins-SemiBold.ttf", "regular":"fonts/Poppins-Regular.ttf"}
      
    # path to sample certificate
    archiveName= "template.png"
    CERTIFICATE = f"static\img\{archiveName}"
   
    coupons(database, CERTIFICATE, FONT)
    Archives.zipFile()