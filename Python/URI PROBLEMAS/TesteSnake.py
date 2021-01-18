import snake


game = snake.Game()

while True:
    events = game.next_frame()

    if events.keys.space:
        print("Space is pressed!")
    else:
        print("Space isn't pressed")

    print("Mouse is at " + str(events.mouse.pos))

    if events.scroll.up:
        print("Scroll up")

    player = game.sprite(game.assets.player)

    while True:
        game.next_frame()
        player.x += 1

    label = game.sprite(game.assets.my_font)

    while True:
        events = game.next_frame()

        if events.keys.space:
            label.text = "Space is pressed"
        else:
            label.text = "Space is not pressed"

    counter = game.sprite(game.assets.my_font)
    counter.stick = game.NE

    while True:
        game.next_frame()

        counter.text = str(round(game, fps, 2))

        counter = game.sprite(game.assets.my_font, x=32, y=32)
