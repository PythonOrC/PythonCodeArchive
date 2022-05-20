from actor import *


class Friend(LoadActor):
    def __init__(self, main):
        super().__init__('codemao',
                         {'walk': 'codemao_walk', 'stand': 'codemao_stand'},
                         (450, 20, 0), 'friend', 20, 100)
        self.actor.setScale(0.6)
        ice_solid = CollisionBox((0, 0, 60), 45, 40, 80)
        ice_node = CollisionNode('codemao')

        ice_node.addSolid(ice_solid)
        self.ice = self.actor.attachNewNode(ice_node)

        organ_solid = CollisionSphere(0, 0, 0, 20)
        organ_node = CollisionNode('organ')
        organ_node.addSolid(organ_solid)
        self.organ = render.attachNewNode(organ_node)
        self.organ.setPos(480, -200, 0)
        self.ice.show()
        mask = BitMask32()
        mask.setBit(2)
        ice_node.setFromCollideMask(mask)
        organ_node.setIntoCollideMask(mask)
        self.create_organ_title(main)
        self.ice_queue = CollisionHandlerQueue()
        base.cTrav.addCollider(self.ice, self.ice_queue)
        mask = BitMask32()
        self.collider.node().setIntoCollideMask(mask)
        self.collider.node().setFromCollideMask(mask)
        self.talk_time = 0
        self.organ_queue = CollisionHandlerQueue()
        base.cTrav.addCollider(self.organ, self.organ_queue)
        self.organ_state = False
        self.delay_time = 0
        self.create_safe_house()
        self.walk_state = False
        self.walk_time = 2
        self.success = False
        self.organ_crack_state = False
        self.health = 75
        self.text = 'Congratulations! Escape to Safe House now?'
        self.choose_dialog = main.choose_dialog(text=self.text, text_fg=(201/255, 91/255, 69/255, 1), text_scale=0.06, pos=(
            0, 0, 0), command=self.choose_command, frameColor=(178/255, 200/255, 217/255, 1))
        self.choose_dialog.hide()
        self.direction = Vec2(0, -1)
        self.choose_dialog_state = False
        self.search_safe_house = False

    def create_organ_title(self, main):
        self.title_dialog = main.create_dialog(
            frame_size=(-1.41, 1.41, -1.01, -0.7), pos=(0, 0, 0), color=(0.2, 0.2, 0.2, 1), picture=None)
        self.title_dialog['text_font'] = main.font
        self.title_dialog['text_pos'] = (-1.3, -0.8)
        self.title_dialog['text'] = '请输入计算结果：(3+2)x(3+2)-7x5+(1/2 + 2/5)*(1/2 + 2/5)x100-70 = '
        self.title_dialog['text_fg'] = (1, 220/255, 99/255, 1)
        self.input_box = main.input_box(scale=0.05, command=self.judge_result, pos=(
            0.1, 0, -0.91), parent=self.title_dialog)
        self.prompt_dialog = main.create_dialog(frame_size=(0, 0.6, 0, 0.1), pos=(
            0.65, 0, -0.95), color=(0.7, 0.9, 1, 1), picture=None)
        self.prompt_dialog['text_font'] = main.font
        self.prompt_dialog['text_pos'] = (0.06, 0.03)
        self.prompt_dialog['text'] = '按Enter键提交答案'
        self.prompt_dialog['text_fg'] = (25/255, 164/255, 236/255, 1)
        self.title_dialog.hide()
        self.prompt_dialog.hide()

    def judge_result(self, result):
        self.organ_state = False
        self.organ.hide()
        if result == '1':
            self.ice.hide()
            self.prompt_dialog['text'] = '机关已打开！'
            self.delay_time = 1
            self.organ_crack_state = True
            self.choose_dialog_state = True
        else:
            self.prompt_dialog['text'] = '密令错误！'
            self.delay_time = 1

    def agency_judgement(self, player, dt, woodmen):
        woodmen.organ_crack_state = self.organ_crack_state
        if self.ice_queue.getNumEntries() > 0:
            self.ice_queue.sortEntries()
            if self.ice_queue.getEntry(0).getIntoNodePath() == player.collider:
                self.talk_time += dt
                if self.talk_time >= 1:
                    self.organ.show()
                    self.talk_time = 0
                    self.organ_state = True
        if self.organ_queue.getNumEntries() > 0 and self.organ_state:
            self.organ_queue.sortEntries()
            if self.organ_queue.getEntry(0).getIntoNodePath() == player.collider:
                self.title_dialog.show()
                self.prompt_dialog.show()
        if self.delay_time >= 0:
            self.delay_time -= dt
            if self.delay_time <= 0:
                self.title_dialog.hide()
                self.prompt_dialog.hide()
        if self.safe_house_queue.getNumEntries() > 0:
            self.safe_house_queue.sortEntries()
            if self.safe_house_queue.getEntry(0).getIntoNodePath() == self.collider:
                self.walk_time -= dt
                if self.walk_time <= 0:
                    self.walk_state = False
            if self.safe_house_queue.getEntry(0).getIntoNodePath() == self.collider and self.safe_house_queue.getEntry(1).getIntoNodePath() == player.collider:
                self.success = True
        if self.choose_dialog_state and self.health >= 80:
            self.choose_dialog.show()
            self.choose_dialog_state = False
            self.safe_house.show()
        if self.walk_state:
            LoadActor.move(self, dt)
            self.velocity += self.safe_vector*300*dt
            if not self.actor.getAnimControl('walk').isPlaying():
                self.actor.play('walk')
        else:
            if not self.actor.getAnimControl('stand').isPlaying():
                self.actor.play('stand')

    def create_safe_house(self):
        safe_house_solid = CollisionSphere(0, 0, 0, 55)
        safe_house_node = CollisionNode('safe_house')
        safe_house_node.addSolid(safe_house_solid)
        self.safe_house = render.attachNewNode(safe_house_node)
        self.safe_house.setPos(-620, -100, 0)
        mask = BitMask32()
        safe_house_node.setIntoCollideMask(mask)
        self.safe_house_queue = CollisionHandlerQueue()
        base.cTrav.addCollider(self.safe_house, self.safe_house_queue)

    def choose_command(self, choose):
        if choose:
            self.safe_vector = self.safe_house.getPos()-self.actor.getPos()
            codemao_safe_vector = self.safe_vector.getXy()
            heading = self.direction.signedAngleDeg(codemao_safe_vector)
            self.actor.setH(heading)
            mask = BitMask32()
            mask.setBit(5)
            self.collider.node().setIntoCollideMask(mask)
            self.choose_dialog.hide()
            self.walk_state = True
            self.search_safe_house = True

        else:
            self.choose_dialog.hide()
            self.ice.show()
            self.safe_house.hide()
