from mycroft import MycroftSkill, intent_file_handler


class RodentFacts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('facts.rodent.intent')
    def handle_facts_rodent(self, message):
        self.speak_dialog('facts.rodent')


def create_skill():
    return RodentFacts()

