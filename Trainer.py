class Trainer:
    def __init__(self, file_name, model_order, model):
        self.file_name = file_name
        self.file = None
        self.model_order = model_order
        self.model = model

    def open(self):
        self.file = open(self.file_name, "r")

    def close(self):
        self.file.close()

    def train_model(self):

        self.open()
        for line in self.file:
                self.split_and_add(line)

        self.close()

    def split_and_add(self, line):
        word_array = line.lower().split()
        count = 0
        while count < len(word_array) - self.model_order:
            self.add_to_model(word_array[count:count + self.model_order + 1])
            count += 1

    def add_to_model(self, arg):

        key_to_add = " ".join(arg[0:len(arg)-1])
        value = {}

        if key_to_add in self.model:
            value = self.model.get(key_to_add, None)
            if arg[-1] in value:
                value[arg[-1]] += 1
            else:
                value[arg[-1]] = 1
        else:
            value[arg[-1]] = 1
            self.model[key_to_add] = value


