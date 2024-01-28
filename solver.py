import random


class Game:
    def __init__(self):
        self.ongoing = False
        self.players = {}
        self.question = Question()

    def start(self):
        self.ongoing = True

    def stop(self):
        self.ongoing = False

    def is_ongoing(self) -> bool:
        return self.ongoing

    def new_question(self):
        self.question.generate_numbers()
        while len(self.question.solve()) == 0:
            self.question.generate_numbers()

    def check_solution(self, solution: str, player: str) -> bool:
        if self.question.check_solution(solution):
            if player in self.players.keys():
                self.players[player] += 1
            else:
                self.players.update({player: 1})
            return True
        return False

    def get_ranking(self) -> list:
        return sorted(self.players.items(), key=lambda player: player[1], reverse=True)


class Question:
    def __init__(self, numbers=None):
        if numbers:
            self.numbers = numbers
        else:
            self.generate_numbers()

    def generate_numbers(self):
        self.numbers = [random.randint(1, 13) for i in range(4)]
        while len(self.solve()) == 0:
            self.numbers = [random.randint(1, 13) for i in range(4)]

    def solve(self):
        return solve([Node(self.numbers[i]) for i in range(4)])

    def check_solution(self, solution):
        try:
            if eval(solution) != 24:
                return False
        except:
            return False
        # get numbers
        solution_nums = []
        c = 0
        while c < len(solution):
            if solution[c].isnumeric():
                i = c+1
                while i < len(solution) and solution[i].isnumeric():
                    i += 1
                solution_nums.append(int(solution[c:i]))
                c = i
            c += 1
        if len(solution_nums) != len(self.numbers):
            return False
        for i in self.numbers:
            if self.numbers.count(i) != solution_nums.count(i):
                return False
        return True

    def __str__(self):
        string = ""
        for i in self.numbers:
            string += str(i)+" "
        return string


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, new_value):
        self.value = new_value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def swap_left_right(self):
        temp = self.left
        self.left = self.right
        self.right = temp

    def merge(self, node, operator):
        new_node = Node(operator)
        new_node.left = self
        new_node.right = node
        return new_node

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def __str__(self):
        if self.is_leaf():
            return str(self.value)
        elif self.left and self.right:
            left = self.left.__str__()
            right = self.right.__str__()
            expression = f"({left+self.value+right})"
            return expression
        elif self.left and self.right is None:
            return self.left.__str__()
        else:
            return self.right.__str__()

    def evaluate(self):
        try:
            return eval(self.__str__())
        except ZeroDivisionError:
            return None

    def __eq__(self, other):
        return type(other) == type(self) and other.__str__() == self.__str__()


operators = ["+", "-", "*", "/"]


def solve(expressions: list) -> list:
    if len(expressions) == 1:
        if expressions[0].evaluate() == 24:
            return [expressions[0].__str__()]
        else:
            return []
    else:
        solutions = []
        for i in range(len(expressions)):
            for c in range(i+1, len(expressions)):
                if c == i:
                    continue
                new_expressions = expressions.copy()

                e1 = new_expressions[i]
                e2 = new_expressions[c]

                new_expressions.pop(c)
                new_expressions.pop(i)

                e = e1.merge(e2, "")    # empty operator placeholder
                new_expressions.append(e)

                for op in operators:
                    e.set_value(op)
                    sol = solve(new_expressions)
                    for w in sol:
                        solutions.append(w)
                    if op == "/" or op == "-":
                        e.swap_left_right()
                        sol = solve(new_expressions)
                        for w in sol:
                            solutions.append(w)
        return solutions


solutions = solve([Node(4), Node(11), Node(9), Node(10)])
