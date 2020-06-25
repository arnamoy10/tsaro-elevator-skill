from mycroft import MycroftSkill, intent_file_handler


class TsaroElevator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('elevator.tsaro.intent')
    def handle_elevator_tsaro(self, message):
        self.speak_dialog('elevator.tsaro')


def create_skill():
    return TsaroElevator()

