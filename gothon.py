#coding=utf-8

#һ�����ǹ��£�����˰��ҵ�����ɴ����䣬Ȼ�����֣�ɱ������������ͬ��
#�Ҿ�һ������������ը���˸�����򣬹��´ӷɴ����������ȿ�ʼ

#����1 ��������
class centerroad(Scene):
	def enter(self)
	pass
#����2 �����ֿ�
class armyweapon(Scene):
	def enter(self)
	pass
#����3 һ������
class bridge(Scene):
	def enter(self)
	pass
#����4 ������
class Pod(Scene):
	def enter(self)
	pass
#��������
class Dead(Scene):
	def enter(self)
	pass

#���ŵ�ͼ
class Map(object):
	
	def __init__(self,start_scene):
		pass
	
	def next_scene(self,scene_name):
		pass
	
	def openning_scene(self):
		pass

#��Ϸ����
class Engine(object):
	def enter(self):

	pass
	
	def start(last_map):
		pass

a_map  = Map(centerroad)
a_game = Engine (a_map)
a_game.start()
