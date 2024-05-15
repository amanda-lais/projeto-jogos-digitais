import pygame
import assets, util

def item_blit(item, screen=util.screen):
    image = item['image']
    position = item['position']
    if detect_hover(item) == True:
        screen.blit(item['hover'], hover_position(item))
    else:
        screen.blit(image, position)

def load_all_items():
    all_items_dict = {
        "anvil": assets.load_anvil(),
        "rock": assets.load_rock(),
        "fruit_tree": assets.load_fruit_tree(),
        "crow": assets.load_crow(),
        "crops": assets.load_crops(),
        "cauldron": assets.load_cauldron(),
        "mess": assets.load_mess(),
        "checklist": assets.load_checklist()
    }
    return all_items_dict

def blit_all_items(all_items_dict, screen=util.screen):
    for item in all_items_dict:
        item_blit(all_items_dict[item], screen)

def detect_hover(item):
    image = item['image']
    position = item['position']
    mouse_pos = pygame.mouse.get_pos()
    x = [position[0], image.get_width()+position[0]]
    y = [position[1], image.get_height()+position[1]]
    if x[1] > mouse_pos[0] > x[0]:
        if y[1] > mouse_pos[1] > y[0]:
            return True
    else:
        return False

def hover_position(item):
    position = item['position']
    return([position[0], position[1] - 15])

def detect_click(item):
    mouse_pressed = pygame.mouse.get_pressed()
    if detect_hover(item) == True and mouse_pressed[0] == True:
        return True
    else:
        return False