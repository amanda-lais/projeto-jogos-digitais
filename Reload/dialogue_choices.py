import assets, util, dialogue
import pygame

def show_choices(box1, box2, box3 = None, screen=util.screen):
    screen.blit(box1['image'], box1['position'])
    screen.blit(box2['image'], box2['position'])
    if box3 != None:
        screen.blit(box3['image'], box3['position'])

def choice_boxes(amount=2):
    dist = 100
    box1 = assets.load_optionboxes()
    box2 = assets.load_optionboxes()
    if amount == 2:
        box1['position'] = [box1['position'][0], box1['position'][1]+dist-50]
        box2['position'] = [box2['position'][0], box2['position'][1]+dist*2-50]
        return [box1, box2]
    elif amount == 3:
        box3 = assets.load_optionboxes()
        box2['position'] = [box2['position'][0], box2['position'][1]+dist]
        box3['position'] = [box3['position'][0], box3['position'][1]+dist*2]
        return [box1, box2, box3]

def text_on_choice(text, choice=1, screen=util.screen):
    max_width = 250
    x = 330
    if choice == 1:
        y = 90
        dialogue.render_wrapped_text(text, dialogue.font, (0, 0, 0), x, y, max_width, screen)
    elif choice == 2:
        y = 205
        dialogue.render_wrapped_text(text, dialogue.font, (0, 0, 0), x, y, max_width, screen)
    elif choice == 3:
        y = 305
        dialogue.render_wrapped_text(text, dialogue.font, (0, 0, 0), x, y, max_width, screen)

def option_hover(opbox):
    image = opbox['image']
    position = opbox['position']
    mouse_pos = pygame.mouse.get_pos()
    x = [position[0], image.get_width()+position[0]]
    y = [position[1]+15, image.get_height()+position[1]-15]
    if x[1] > mouse_pos[0] > x[0]:
        if y[1] > mouse_pos[1] > y[0]:
            return True
    else:
        return False

def option_click(box1, box2, box3=None):
    mouse_pressed = pygame.mouse.get_pressed()
    if option_hover(box1) == True and mouse_pressed[0] == True:
        return 1
    elif option_hover(box2) == True and mouse_pressed[0] == True:
        return 2
    elif box3 != None and option_hover(3) == True and mouse_pressed[0] == True:
        return 3