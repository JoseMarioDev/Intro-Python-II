from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# items

item = {
    "torch": Item("torch", "The light will help you see the way"),
    "sword": Item("sword", "Hattori Hanzo to defeat your enemies"),
    "shield": Item("shield", "Block your enemies blows"),
    "crown": Item("crown", "Claim your rightful place on the throne"),
    "ring": Item("ring", "family heirloom, reminder of your greatness")
}

# Add to rooms
room['outside'].add_item(item["torch"])
room['foyer'].add_item(item["ring"])
room['overlook'].add_item(item["sword"])
room['narrow'].add_item(item["sword"])
room['treasure'].add_item(item["sword"])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name: "), room['foyer'])
print(player.current_room)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ['n', 's', 'e', 'w']

while True:
        # Read command
    cmd = input("Please enter a direction: ").lower()
    # Check if it's n/s/e/w/q
    if cmd in directions:
        # Make player travel in that direction
        player.travel(cmd)
    elif cmd == "q":
        # Quit
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid command, please try again")
