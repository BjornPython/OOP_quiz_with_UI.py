import requests
import html


class QuizBrain:

    def __init__(self):
        self.background = "#343434"
        self.flash_card_font = "Ariel"
        self.current_index = 0
        self.score = 0
        self.data = self.get_ques_list()
        self.QandA = [{"question": ques["question"], "answer": ques["correct_answer"]} for ques in self.data]

    def get_ques_list(self):
        response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
        response.raise_for_status()
        data = response.json()
        return data["results"]

    def check_ans(self, ans):
        if self.current_index <= len(self.QandA) - 2:
            if str(ans) == self.QandA[self.current_index]["answer"]:
                self.score += 1
                return True
            else:
                return False
        return "list index out of range"

    def new_ques(self):
        self.current_index += 1
        question = html.unescape(self.QandA[self.current_index]["question"])

        return question
