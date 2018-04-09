import items, enemies

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You are in your cell you think to yourself "I need to get out of this shithole"
        You can go left out of your cell or you can go right to your toilet.
        """

    def modify_player(self, player):
        #Room Has no effect on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item)
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.invintory.appent(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy - enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

class EmptyCorridor(MapTile):
    def intro_text(self):
        return """
        Just an empty corridor keep going onward
        """
    def modify_player(self, player):
        #Room has no action on player
        pass
    
