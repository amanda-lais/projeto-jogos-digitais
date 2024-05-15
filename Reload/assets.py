import pygame

# def load_assets():
#     screen_width = 800
#     screen_height = 600
#     screen = pygame.display.set_mode((screen_width, screen_height))
#     pygame.display.set_caption('ReLOAD')


def load_background(screen_width, screen_height):
    background_image = pygame.image.load('assets/images/placeholder_forest_bg.png')
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    background_position = [0, 0]
    bg_dict = {'image': background_image, 'position': background_position}
    return bg_dict

def load_tiles():
    overlay_image = pygame.image.load('assets/images/tiles.png')
    overlay_image = pygame.transform.scale(overlay_image, (700, 500))
    overlay_position = [75, 50]
    tiles_dict = {'image': overlay_image, 'position': overlay_position}
    return tiles_dict

# Boxes
# Diloague box
def load_dialoguebox():
    dbox = pygame.image.load('assets/images/dialogue_box.png')
    dbox = pygame.transform.scale(dbox, (656, 224))
    dbox_position = [75, 380]
    dbox_dict = {'image': dbox, 'position': dbox_position}
    return dbox_dict

# Option boxes
def load_optionboxes():
    opbox = pygame.image.load('assets/images/box.png')
    opbox = pygame.transform.scale(opbox, (256, 120))
    opbox_position = [285, 60]
    opbox_dict = {'image': opbox, 'position': opbox_position}
    return opbox_dict

def load_char_name_box():
    namebox = pygame.image.load('assets/images/box.png')
    namebox = pygame.transform.scale(namebox, (256/1.3, 120/1.3))
    namebox_position = [100, 350]
    namebox_dict = {'image': namebox, 'position': namebox_position}
    return namebox_dict

# Itens

def load_anvil():
    anvil = pygame.image.load('assets/images/anvil.png')
    anvil = pygame.transform.scale(anvil, (150, 150))
    hover_anvil= pygame.image.load('assets/images/anvil_hover.png')
    hover_anvil = pygame.transform.scale(hover_anvil, (150, 150))
    anvil_position = [630, 300]
    anvil_dict = {'image': anvil, 'hover': hover_anvil, 'position': anvil_position}
    return anvil_dict

def load_rock():
    rock = pygame.image.load('assets/images/rock.png')
    rock = pygame.transform.scale(rock, (150, 150))
    hover_rock = pygame.image.load('assets/images/rock_hover.png')
    hover_rock = pygame.transform.scale(hover_rock, (150, 150))
    rock_position = [200, 150]
    rock_dict = {'image': rock, 'hover': hover_rock, 'position': rock_position}
    return rock_dict

def load_fruit_tree():
    ftree = pygame.image.load('assets/images/tree.png')
    ftree = pygame.transform.scale(ftree, (536/4, 725/4))
    hover_ftree = pygame.image.load('assets/images/tree_hover.png')
    hover_ftree = pygame.transform.scale(hover_ftree, (536/4, 725/4))
    ftree_position = [380, -25]
    ftree_dict = {'image': ftree, 'hover': hover_ftree, 'position': ftree_position}
    return ftree_dict

def load_crow():
    crow = pygame.image.load('assets/images/crow.png')
    crow = pygame.transform.scale(crow, (536/4, 399/4))
    hover_crow = pygame.image.load('assets/images/crow_hover.png')
    hover_crow = pygame.transform.scale(hover_crow, (536/4, 399/4))
    crow_position = [520, 190]
    crow_dict = {'image': crow, 'hover': hover_crow, 'position': crow_position}
    return crow_dict

def load_mess():
    mess = pygame.image.load('assets/images/mess.png')
    mess = pygame.transform.scale(mess, (536/3, 417/3))
    hover_mess = pygame.image.load('assets/images/mess_hover.png')
    hover_mess = pygame.transform.scale(hover_mess, (536/3, 417/3))
    mess_position = [240, 350]
    mess_dict = {'image': mess, 'hover': hover_mess, 'position': mess_position}
    return mess_dict

def load_crops():
    crops = pygame.image.load('assets/images/crops.png')
    crops = pygame.transform.scale(crops, (536/4, 423/4))
    hover_crops = pygame.image.load('assets/images/crops_hover.png')
    hover_crops = pygame.transform.scale(hover_crops, (536/4, 423/4))
    land = pygame.image.load('assets/images/land.png')
    land = pygame.transform.scale(land, (536, 423))
    hover_land = pygame.image.load('assets/images/land_hover.png')
    hover_land = pygame.transform.scale(hover_land, (536, 423))
    crops_position = [120, 285]
    crops_dict = {'image': crops, 'land': land, 'land_hover': hover_land,'hover': hover_crops, 'position': crops_position}
    return crops_dict

def load_cauldron():
    cauldron = pygame.image.load('assets/images/cauldron.png')
    cauldron = pygame.transform.scale(cauldron, (552/4, 598/4))
    hover_cauldron = pygame.image.load('assets/images/cauldron_hover.png')
    hover_cauldron = pygame.transform.scale(hover_cauldron, (552/4, 598/4))
    boiling = pygame.image.load('assets/images/cauldron_boiling.png')
    boiling = pygame.transform.scale(boiling, (552/4, 598/4))
    explodes = pygame.image.load('assets/images/cauldron_goes_wrong.png')
    explodes = pygame.transform.scale(explodes, (552/4, 598/4))
    cauldron_position = [390, 375]
    cauldron_dict = {'image': cauldron, 'boiling': boiling,'explosion': explodes,'hover': hover_cauldron, 'position': cauldron_position}
    return cauldron_dict

def load_checklist():
    checklist = pygame.image.load('assets/images/checklist.png')
    checklist = pygame.transform.scale(checklist, (512/3, 512/3))
    hover_checklist = pygame.image.load('assets/images/checklist_hover.png')
    hover_checklist = pygame.transform.scale(hover_checklist, (512/3, 512/3))
    checklist_position = [20, 20]
    checklist_dict = {'image': checklist, 'hover': hover_checklist, 'position': checklist_position}
    return checklist_dict

def load_dboxwitch():
    witch = pygame.image.load('assets/images/witch.png')
    witch = pygame.transform.scale(witch, (681/2, 949/2))
    witch_position = [400, 0]
    witch_dict = {'image': witch, 'position': witch_position}
    return witch_dict

def load_dboxbutterfly():
    butterfly = pygame.image.load('assets/images/butterfly.png')
    butterfly = pygame.transform.scale(butterfly, (374, 287))
    butterfly_position = [30, 150]
    butterfly_dict = {'image': butterfly, 'position': butterfly_position}
    return butterfly_dict