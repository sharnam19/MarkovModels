class MarkovModel:
    def __init__(self, model_order):
        self.model_order = model_order
        self.model = {}

    def load_model(self):
        import json
        self.model = json.load(open("Model"+str(self.model_order)+".json", "r"))

    def save_model(self):
        import json
        json.dump(self.model, open("Model"+str(self.model_order)+".json", "w"), sort_keys=True, indent=4)

    def __train_model(self, file_name):
        from Markov.Trainer import Trainer

        trainer = Trainer(file_name, self.model_order, self.model)
        trainer.train_model()

    def train(self, file_name, count):

        i = 0

        while i < count:
            self.__train_model(file_name)
            i += 1

    def predict(self, prediction_string):

        model = self.model.get(prediction_string.lower(), None)

        if model is not None:
            return max(model, key=model.get)
        else:
            return None

    def test(self):
        loop = True
        string = []
        from Markov.Trainer import Trainer
        trainer = Trainer(None, self.model_order, self.model)

        while loop:

            print("Enter your Choice")
            option = input().lower()

            if option == "exit":
                loop = False
            else:

                string.append(option)

                if len(string) >= self.model_order:

                    predicted_value = self.predict(" ".join(string[len(string)-self.model_order:]))

                    if predicted_value is not None:
                        print("Predicted Value is "+predicted_value)
                    else:
                        print("No Predictions")

                    if len(string) >= self.model_order+1:
                        trainer.add_to_model(string[len(string)-self.model_order-1:])

        self.save_model()












