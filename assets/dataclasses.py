import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

##CLASSES
class ID_:
    def __init__(self, index=0, seed=0, area='', x=0, y=0, z=0, lock=0, islocker=True, zone_size_preset = 1):
        self.index_ = index
        self.seed_ = seed
        self.area_ = area
        self.x_ = x
        self.y_ = y
        self.z_ = z
        self.lock_ = lock
        self.islocker_ = islocker
        self.zone_size_preset_ = zone_size_preset

    def print_data(self):
        print("Box Index: {} -> {}".format(self.index_, self.area_))

    def draw_container(self, background):
        if self.zone_size_preset_ == 0:
            if self.islocker_:
                container_image = Image.open("assets/locker_small.png")
            else:
                container_image = Image.open("assets/box_small.png")
            font_size = 33
        else:
            if self.islocker_:
                container_image = Image.open("assets/locker.png")
            else:
                container_image = Image.open("assets/box.png")
            font_size = 55
        
        offset_x = 0
        if self.index_ >= 10:
            offset_x = - font_size/4
        offset_y = container_image.height - font_size * 0.3

        background.paste(container_image, (self.x_, self.y_), container_image)

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("assets/OpenSans-Bold.ttf", font_size)
        
        r, g, b = 0, 255, 0
        
        if self.lock_ == 1:
            r, g, b = 250, 218, 94
        elif self.lock_ == 2:
            r, g, b = 255, 0, 0

        draw.text((self.x_ + offset_x, self.y_ + offset_y), str(self.index_), (r,g,b),font=font)

        if self.z_ > 0:
            draw.text((self.x_ + 10, self.y_ - 20),'^',(0,0,0),font=font)
        elif self.z_ < 0:
            draw.text((self.x_ + 10, self.y_ - 20),'v',(0,0,0),font=font)
    
    def tojson(self):
        return json.dumps(self.__dict__, indent=4)

class ZONE_:
    def __init__(self, name, index, type, idlist, image_file, package_name):
        self.name_ = name
        self.index_ = index
        self.type_ = type
        self.idlist_ = idlist
        self.id_start_index_ = idlist[0].index_
        self.image_file_ = image_file
        self.image_save_ = Image.open("packages/" + package_name + '/' + image_file)

    def save_image(self):
        self.image_save_.save(self.image_file_[:len(self.image_file_) - 4] + "_GENERATED.png")

class ARG_:
    def __init__(self, key, sub_list=[]):
        self.key_ = key
        self.sub_list_ = sub_list
