# Создать виртуальную клавиатуру с переназначаемыми действиями для клавиш и комбинаций клавиш, с возможностью отката действий назад

import time

class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class Action1(Command):
    def execute(self):
        print("Выполнено действие 1")

    def undo(self):
        print("Отменено действие 1")

class Action2(Command):
    def execute(self):
        print("Выполнено действие 2")

    def undo(self):
        print("Отменено действие 2")

class Action3(Command):
    def execute(self):
        print("Выполнено действие 3")

    def undo(self):
        print("Отменено действие 3")

class VirtualKeyboard:
    def __init__(self):
        self.actions = {}   #словарь, где ключами являются клавиши, а значениями - соответствующие им команды
        self.history = []   #список для отслеживания выполненных действий

    #привязка клавиши к команде
    def assign_action(self, key, action):
        self.actions[key] = action
        print(f"Клавиша {key} назначена на действие {action.__class__.__name__}")

    def press_key(self, key):
        if key in self.actions:
            action = self.actions[key]
            action.execute()
            self.history.append(action)
            print(f"Нажата клавиша {key}")

    def undo_last_action(self):
        if self.history:
            action = self.history.pop()
            action.undo()
            print(f"Отменено действие для клавиши {action.__class__.__name__}")

# Пример использования
keyboard = VirtualKeyboard()

keyboard.assign_action("F1", Action1())
keyboard.assign_action("Ctrl+Alt+X", Action2())
keyboard.assign_action("Shift+Z", Action3())

keyboard.press_key("F1")  # Выполнено действие 1
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 2
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Shift+Z")  # Выполнено действие 3
time.sleep(1)  # Задержка в 1 секунду

keyboard.undo_last_action()  # Отменено действие 3
time.sleep(1)  # Задержка в 1 секунду

keyboard.assign_action("F1", Action3())
keyboard.assign_action("Ctrl+Alt+X", Action1())

keyboard.undo_last_action()

keyboard.press_key("F1")  # Выполнено действие 3
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 1
time.sleep(1)  # Задержка в 1 секунду

keyboard = VirtualKeyboard()

keyboard.press_key("F1")  # Выполнено действие 1 (новое переназначение)
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 2 (новое переназначение)
time.sleep(1)  # Задержка в 1 секунду