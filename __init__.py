from mycroft import MycroftSkill, intent_file_handler

data = [
  'Rats are omnivores with their primary diet consisting of seeds, fruit, grains, nuts, flowers, insects and such.',
  'Rats typically consume 1 ounce of food and water per day.',
  'Rats have strong teeth that can gnaw through material like wood, aluminum and even copper!',
  'Rats are extremely social and like to be kept in bigger groups and even enjoy cuddling together.',
  'Rats can typically live 2 to 3 years.',
  'The term rat typically refers to two main species the Norway rat and Roof rat both being house species.',
  'Sometimes you will hear Norway rats referred to as brown, gray, common, or sewer rat.',
  'Most norway rats are 7 to 10 inches long and can weigh up to 17 ounces.',
  'Female rats can average 4 to 6 litters each year consisting of 8 to 12 pups per litter.',
  'Rats typically have a gestation period of three weeks and can become pregnant almost immediately within a few days after giving birth.'
]

class RodentFacts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('facts.rodent.intent')
    def handle_facts_rodent(self, message):
        self.speak_dialog('facts.rodent', data={'fact': data[0]})


def create_skill():
    return RodentFacts()

