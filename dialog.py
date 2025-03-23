import pygame


class DialogBox:
    def __init__(self):
        self.box = pygame.image.load("dialog\dialog_box.png")
        self.box = pygame.transform.scale(self.box, (700, 100))
        self.conversation = None  # This will hold the current conversation

    def execute(self, conversation):
        self.conversation = conversation

    def render(self, screen):
        if self.conversation:
            self.conversation.render(screen)

    def handle_input(self, event):
        if self.conversation:
            self.conversation.handle_input(event)


class Conversation:
    X_POSITION = 60
    Y_POSITION = 470

    def __init__(self, npc, player_choices):
        self.letter_index = 0
        self.box = pygame.image.load("dialog\dialog_box.png")
        self.box = pygame.transform.scale(self.box, (700, 100))
        self.npc_text = []
        self.npc = npc
        self.player_choices = player_choices  # player choices should be a dict
        self.current_state = 0  # Index of the current state in the conversation
        self.player_response = None
        self.font = pygame.font.Font("dialog\dialog_font.ttf", 18)
        self.npc_response = None

    def render(self, screen):
        # Render NPC text
        self.npc_text = self.npc.npc_texts[self.current_state]
        npc_text = self.npc_text
        # Render player choices if available
        if self.player_choices:
            # Render NPC text
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            npc_text_surface = self.font.render(npc_text, False, (0, 0, 0))
            npc_text_rect = npc_text_surface.get_rect(center=(400, 500))
            screen.blit(npc_text_surface, (self.X_POSITION + 60, self.Y_POSITION + 30))

            # Render player choices
            for i, (choice_key, choice_text) in enumerate(self.player_choices.items()):
                choice_text_surface = self.font.render(f"{choice_key}: {choice_text}", False, (0, 0, 0))
                screen.blit(choice_text_surface, (self.X_POSITION + 60, self.Y_POSITION + 30))
        else:
            # Render NPC response based on the player's choice
            self.npc_response = self.get_npc_response()
            # Render the NPC response on the screen
            screen.blit(self.npc_response, (self.X_POSITION + 60, self.Y_POSITION + 30))

    def handle_input(self, event):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player_response = 'A'
                elif event.key == pygame.K_b:
                    self.player_response = 'B'
                elif event.key == pygame.K_c:
                    self.player_response = 'C'

    def get_npc_response(self):
        # Implement logic to determine NPC's response based on player's choice
        if self.npc_response == 'A': return "Good choice, you chose A"
        if self.npc_response == 'B': return "What a choice, you chose B"
        if self.npc_response == 'C': return "Not good choice, you chose C"

        # Update the conversation state accordingly
        self.next_text()

    def next_text(self):
        self.letter_index += 1

        if self.letter_index >= len(self.npc_text[self.current_state]):
            self.letter_index = 0
            self.current_state += 1

            if self.current_state >= len(self.npc_text):
                # Close the dialog if all text were read
                self.letter_index = 0
                self.current_state = 0
                self.player_response = None
