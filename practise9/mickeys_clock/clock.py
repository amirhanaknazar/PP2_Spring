import pygame
import math

hand_img = pygame.image.load("images/mickey_hand.jpeg")

def draw_clock(screen, minutes, seconds):
    center = (300, 300)

    sec_angle = - (seconds * 6)
    sec_hand = pygame.transform.rotate(hand_img, sec_angle)
    sec_rect = sec_hand.get_rect(center=center)
    screen.blit(sec_hand, sec_rect)

    min_angle = - (minutes * 6)
    min_hand = pygame.transform.rotate(hand_img, min_angle)
    min_rect = min_hand.get_rect(center=center)
    screen.blit(min_hand, min_rect)