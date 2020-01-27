import pygame

from _game import Game



    
game = Game()
game.newGame()
exit_game = False

while not exit_game:

    while game.run:
        
        pygame.time.delay(20)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:
            exit_game = True
                
        if exit_game:
            break

        if keys[pygame.K_UP]: #you can put any event you want over here to jump
            game.move()
        
        game.manageEvents()
        
        for _ in range(5):
            game.renderFrame()
        
        if not game.run:
            pygame.time.delay(1000)
            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]: #you can put any event you want over here to start new game
        game.newGame()
    
    if keys[pygame.K_ESCAPE]:
        break

pygame.quit()

