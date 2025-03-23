import pygame
import os
class DialogBox:
    X_POSITION = 0
    Y_POSITION= 470
    
    def __init__(self) -> None:
        base_path = os.path.join(os.path.dirname(__file__), '../dialogs')
        self.box = pygame.image.load(os.path.join(base_path, 'dialog_box.png'))
        self.box = pygame.transform.scale(self.box, (700,100))
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font(os.path.join(base_path, 'dialog_font.ttf'), 18)
        self.reading = False
        
    def execute(self, dialog=[]):
        if self.reading :
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog
            
    def render(self, screen):
        if self.reading :
            self.letter_index += 1
            
            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index
                
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0,0,0))
            screen.blit(text, (self.X_POSITION + 60 , self.Y_POSITION + 30 ))
            
    def next_text(self):
        self.text_index += 1
        self.letter_index = 0
        
        if self.text_index >= len(self.texts):
            # close dailog
            self.reading = False
            self.text_index=0