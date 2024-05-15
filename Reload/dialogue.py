import pygame
import assets
import util

pygame.init()
pygame.font.init()

font = pygame.font.Font('assets/fonts/monogram/monogram-extended.ttf', 32)
font_alt = pygame.font.Font('assets/fonts/DungeonFont.ttf', 32)

def load_dialogue_basics():
    dialogue_basic = {
        "dbox": assets.load_dialoguebox(),
        "circe": assets.load_dboxwitch(),
        "chronos": assets.load_dboxbutterfly(),
        "namebox": assets.load_char_name_box()
    }
    return dialogue_basic

def show_dialogue_basics(dialogue_basics, screen=util.screen):
    util.blit_by_item(dialogue_basics['circe'], screen)
    util.blit_by_item(dialogue_basics['chronos'], screen)
    util.blit_by_item(dialogue_basics['dbox'], screen)
    util.blit_by_item(dialogue_basics['namebox'], screen)

def chronos_speaking(screen=util.screen):
    render_wrapped_text("Chronos", font_alt, (0, 0, 0), 145, 380, 400)

def circe_speaking(screen=util.screen):
    render_wrapped_text("Circe", font_alt, (0, 0, 0), 145, 380, 400)

def narrator_speaking(screen=util.screen):
    render_wrapped_text(" ", font_alt, (0, 0, 0), 145, 380, 400)

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        if font.size(current_line + word)[0] < max_width:
            current_line += word + ' '
        else:
            lines.append(current_line[:-1])
            current_line = word + ' '
    if current_line:
        lines.append(current_line)
    return lines

def render_wrapped_text(text, font, color, x, y, max_width, screen=util.screen):
    lines = wrap_text(text, font, max_width)
    line_height = font.get_height()
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(x=x, y=y + i * line_height)
        screen.blit(text_surface, text_rect)

def text_on_dialogue_box(text, screen=util.screen):
    render_wrapped_text(text, font, (0, 0, 0), 120, 440, 550, screen)

def text_on_choice(text, choice=1, screen=util.screen):
    max_width = 250
    x = 330
    if choice == 1:
        y = 90
        render_wrapped_text(text, font, (0, 0, 0), x, y, max_width, screen)
    elif choice == 2:
        y = 205
        render_wrapped_text(text, font, (0, 0, 0), x, y, max_width, screen)
    elif choice == 3:
        y = 305
        render_wrapped_text(text, font, (0, 0, 0), x, y, max_width, screen)

############################
############################
############################

def option_hover(opbox):
    image = opbox['image']
    position = opbox['position']
    mouse_pos = pygame.mouse.get_pos()
    x = [position[0], image.get_width()+position[0]]
    y = [position[1], image.get_height()+position[1]]
    if x[1] > mouse_pos[0] > x[0]:
        if y[1] > mouse_pos[1] > y[0]:
            print(opbox)
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