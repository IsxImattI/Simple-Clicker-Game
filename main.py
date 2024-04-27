import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants for the game
WIDTH, HEIGHT = 1200, 900
BACKGROUND_COLOR = (30, 30, 30)
BUTTON_COLOR = (100, 200, 100)
BUTTON_HOVER_COLOR = (150, 250, 150)
UPGRADE_COLOR = (200, 100, 100)
UPGRADE_HOVER_COLOR = (250, 150, 150)
SCORE_COLOR = (255, 255, 255)
FONT_SIZE = 32

# Create the display window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Pygame Clicker Game")

# Load font for the display
font = pygame.font.Font(None, FONT_SIZE)

# Score, money, and upgrades variables
score = 0
money = 0
money_per_click = 1
auto_clickers = 0
money_upgrade_cost = 50

# Button setup
click_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 200, 200, 100)
auto_clicker_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)
money_upgrade_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 100)

# Draw button function
def draw_button(rect, mouse_pos, text, normal_color, hover_color):
    if rect.collidepoint(mouse_pos):
        color = hover_color
    else:
        color = normal_color
    pygame.draw.rect(window, color, rect)
    text_surf = font.render(text, True, SCORE_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    window.blit(text_surf, text_rect)

# Display score and money
def display_info():
    score_surf = font.render(f'Score: {score}', True, SCORE_COLOR)
    score_rect = score_surf.get_rect(center=(WIDTH // 2, 30))
    window.blit(score_surf, score_rect)
    
    money_surf = font.render(f'Money: {money}', True, SCORE_COLOR)
    money_rect = money_surf.get_rect(center=(WIDTH // 2, 70))
    window.blit(money_surf, money_rect)

    auto_clicker_surf = font.render(f'Auto Clickers: {auto_clickers}', True, SCORE_COLOR)
    auto_clicker_rect = auto_clicker_surf.get_rect(center=(WIDTH // 2, 110))
    window.blit(auto_clicker_surf, auto_clicker_rect)

def main():
    global score, money, money_per_click, auto_clickers, money_upgrade_cost  # Include money_upgrade_cost here
    clock = pygame.time.Clock()
    last_auto_click_time = time.time()

    while True:
        current_time = time.time()
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if click_button_rect.collidepoint(mouse_pos):
                    score += 1
                    money += money_per_click
                if auto_clicker_button_rect.collidepoint(mouse_pos) and money >= 10:
                    auto_clickers += 1
                    money -= 10
                if money_upgrade_button_rect.collidepoint(mouse_pos) and money >= money_upgrade_cost:
                    money_per_click += 5
                    money -= money_upgrade_cost
                    money_upgrade_cost *= 2  # Increase cost for next upgrade

        if current_time - last_auto_click_time >= 1:
            score += auto_clickers
            last_auto_click_time = current_time

        window.fill(BACKGROUND_COLOR)
        draw_button(click_button_rect, mouse_pos, 'Click Me!', BUTTON_COLOR, BUTTON_HOVER_COLOR)
        draw_button(auto_clicker_button_rect, mouse_pos, f'Auto Clicker: 10', UPGRADE_COLOR, UPGRADE_HOVER_COLOR)
        draw_button(money_upgrade_button_rect, mouse_pos, f'Money Upgrade: {money_upgrade_cost}', UPGRADE_COLOR, UPGRADE_HOVER_COLOR)
        display_info()
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()

