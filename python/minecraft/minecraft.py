from mcpi.minecraft import Minecraft
from mcpi import block




class Session:

    def __init__(self, mc):
        self.mc = mc

    def update_my_position(self):
        self.x, self.y, self.z = self.mc.player.getPos()



if __name__ == '__main__':
    session = Session(Minecraft.create())
    session.update_my_position()
    session.create_blocks(block.STONE.id, 1, 1, 1, 5, 10, 2)