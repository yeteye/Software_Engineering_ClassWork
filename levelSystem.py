import json


class LevelSystem:
    def __init__(self):
        self.filename = "profile.json"
        self.data = self.load_data()

    #初始化：设定等级为1，经验为0
    def initialize_profile(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        # 初始化指定的字段
        data['level'] = 1
        data['exp'] = 0
        data['task_times'] = 0

        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    # task_time暂存每次每个任务的完成时间，完成后加入到经验值中，task_time清零
    def gain_experience(self):
        self.data['exp'] += self.data['task_time']
        self.data['task_time'] = 0
        self.save_data()
        return self.data['exp']

    #计算升到下一级所需要的经验值
    def experience_to_next_level(self):
        current_level = self.data.get('level', 1)
        if current_level >= 100:
            return 0  # 已经满级
        else:
            return current_level * 100

    def levelCalculate(self):
        while True:
            exp_to_next_level = self.experience_to_next_level()
            if exp_to_next_level == 0:  #当等级为100级时不再升级
                break
            if self.data['exp'] >= exp_to_next_level:
                self.data['exp'] -= exp_to_next_level
                self.data['level'] += 1
            else:
                break


