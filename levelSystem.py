import json
class LevelSystem:
    def __init__(self):
        self.filename = "profile.json"
        self.data = self.load_data()
        self.MainWindow = None

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)
        f.close()

    # task_time暂存每次每个任务的完成时间，完成后加入到经验值中，task_time清零
    def gain_experience(self):
        self.data = self.load_data()
        self.data['exp'] += self.data['plannedTime']*100   #plannedTime为完成任务规定时间，计算规则为每1秒计入一经验
        self.data['plannedTime'] = 0
        self.data['task_times'] += 1
        self.save_data()

    #计算升到下一级所需要的经验值
    def experience_to_next_level(self):
        current_level = self.data.get('level', 1)
        if current_level >= 100:
            return 0  # 已经满级
        else:
            return current_level * 100  #升级机制为每一等级升级到下一等级的所需经验值为当前等级值*100

    def levelCalculate(self):
        self.gain_experience()
        while True:
            exp_to_next_level = self.experience_to_next_level()
            if exp_to_next_level == 0:  #当等级为100级时不再升级
                break
            if self.data['exp'] >= exp_to_next_level:
                self.data['exp'] -= exp_to_next_level
                self.data['level'] += 1
            else:
                self.save_data()
                break

