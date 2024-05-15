import pygame
import assets, util
import items, dialogue, dialogue_choices
import math

pygame.init()


screen = util.screen
screen_width = util.screen_width
screen_height = util.screen_height

bg = assets.load_background(screen_width, screen_height)
tiles = assets.load_tiles()

#Itens
all_items = items.load_all_items()

#Boxes
dialogue_basics = dialogue.load_dialogue_basics()

is_dbox_active = False
choose_dialogue = False
choice_amount = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
    # Fundo + tiles
    screen.blit(bg['image'], bg['position'])
    screen.blit(tiles['image'], tiles['position'])
    
    # Itens
    items.blit_all_items(all_items)
    
    
    if items.detect_click(all_items["anvil"]) == True and is_dbox_active == False:
        print("anvil!")
        is_dbox_active = True
    
    if items.detect_click(all_items["cauldron"]) == True and choose_dialogue == False:
        choose_dialogue = True
        choice_amount = 2
    
    if is_dbox_active == True:
        dialogue.show_dialogue_basics(dialogue_basics)
    
    if choose_dialogue == True:
        if choice_amount == 2:
            choices = dialogue_choices.choice_boxes(2)
            dialogue_choices.show_choices(choices[0], choices[1])
            pick = dialogue_choices.option_click(choices[0], choices[1]) 
            if pick != None:
                choose_dialogue = False
        elif choice_amount == 3:
            choices = dialogue_choices.choice_boxes(3)
            pick = dialogue_choices.option_click(choices[0], choices[1], choices[2]) 
            if pick != None:
                choose_dialogue = False
    
    
    pygame.display.update()

pygame.quit()