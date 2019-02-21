#coding=utf-8

#一个外星故事，哥顿人把我的宇宙飞船击落，然后入侵，杀掉了我们所有同伴
#我就一个人逃生，并炸掉了哥顿星球，故事从飞船的中央走廊开始

#场景1 中央走廊
class centerroad(Scene):
	def enter(self)
	pass
#场景2 武器仓库
class armyweapon(Scene):
	def enter(self)
	pass
#场景3 一个桥上
class bridge(Scene):
	def enter(self)
	pass
#场景4 逃生仓
class Pod(Scene):
	def enter(self)
	pass
#死亡场景
class Dead(Scene):
	def enter(self)
	pass

#整张地图
class Map(object):
	
	def __init__(self,start_scene):
		pass
	
	def next_scene(self,scene_name):
		pass
	
	def openning_scene(self):
		pass

#游戏引擎
class Engine(object):
	def enter(self):

	pass
	
	def start(last_map):
		pass

a_map  = Map(centerroad)
a_game = Engine (a_map)
a_game.start()
