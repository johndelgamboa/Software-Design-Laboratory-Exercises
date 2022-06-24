import random

hedges = ("Please tell me more.",
        "Many of my patients tell me the same thing.",
        "Please continue.")
qualifiers = ("Why do you say that ",
        "You seem to think that ",
        "Can you explain why ")
replacements = {"I":"you", "me":"you", "my":"your",
        "we":"you", "us":"you", "mine":"yours"}

class Doctor:


    def changePerson(self, sentence):
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(replacements.get(word, word))
        return " ".join(replyWords)     

    def reply(self, sentence):
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(hedges)
        else:
            return random.choice(qualifiers) + self.changePerson(sentence)   

    def greeting(self):
        msg = "greetings! how can i help you"
        return msg


