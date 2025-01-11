import sys, pygame


# Level Manager Class
class LevelManager:
    def __init__(self):
        # Initialize Variables
        self.selected_index = 0
        self.last_option = None
        self.selected_color = (255, 255, 0)
        self.deselected_color = (255, 255, 255)

    # Draw Menu Method
    def draw_menu(self, screen):
        # Handle Drawing Menu Options
        for i, opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom + i * self.spacer)
            if i == self.selected_index:
                rend_img, rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img, rend_rect)
            else:
                screen.blit(opt[0], opt[1])

    # Update Menu Method
    def update_menu(self):
        self.mouse_hover_sound()
        self.change_selected_option()

    # Event Method
    def get_event_menu(self, event):
        if event.type == pygame.KEYDOWN:
            # Select new index
            if event.key in [pygame.K_UP, pygame.K_w]:
                self.change_selected_option(-1)
            elif event.key in [pygame.K_DOWN, pygame.K_s]:
                self.change_selected_option(1)

            elif event.key == pygame.K_RETURN:
                self.select_option(self.selected_index)
        self.mouse_menu_click(event)

    # Mouse Hover Method
    def mouse_hover_sound(self):
        # Play Sound when selected option changes
        for i, opt in enumerate(self.rendered["des"]):
            if opt[1].collidepoint(pygame.mouse.get_pos()):
                if self.last_option != opt:
                    self.last_option = opt

    # Mouse Menu Click Method
    def mouse_menu_click(self, event):
        # Select Menu Option
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, opt in enumerate(self.rendered["des"]):
                if opt[1].collidepoint(pygame.mouse.get_pos()):
                    self.selected_index = i
                    self.select_option(i)
                    break

    # Pre Render Method
    def pre_render_options(self):
        # Setup Render Menu Options based on selected or deselected
        font_deselect = pygame.font.SysFont("arial", 50)
        font_selected = pygame.font.SysFont("arial", 70)

        rendered_msg = {"des": [], "sel": []}
        for option in self.options:
            d_rend = font_deselect.render(option, 1, self.deselected_color)
            d_rect = d_rend.get_rect()
            s_rend = font_selected.render(option, 1, self.selected_color)
            s_rect = s_rend.get_rect()
            rendered_msg["des"].append((d_rend, d_rect))
            rendered_msg["sel"].append((s_rend, s_rect))
        self.rendered = rendered_msg

    # Select Option Method
    def select_option(self, i):
        # Select Menu Option via keyboard or mouse
        if i == len(self.next_list):
            self.quit = True
        else:
            self.next = self.next_list[i]
            self.done = True
            self.selected_index = 0

    # Change Selected Option Method
    def change_selected_option(self, op=0):
        # Change Highlighted Menu Option
        for i, opt in enumerate(self.rendered["des"]):
            if opt[1].collidepoint(pygame.mouse.get_pos()):
                self.selected_index = i
        if op:
            self.selected_index += op
            max_ind = len(self.rendered['des']) - 1
            if self.selected_index < 0:
                self.selected_index = max_ind
            elif self.selected_index > max_ind:
                self.selected_index = 0
