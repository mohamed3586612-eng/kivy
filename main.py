from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalculatorLayout(BoxLayout):
    def calculate(self):
        try:
            num1 = float(self.ids.input1.text)
            num2 = float(self.ids.input2.text)
            operation = self.ids.operation.text

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    self.ids.result.text = "لا يمكن القسمة على صفر"
                    return
                result = num1 / num2
            else:
                self.ids.result.text = "عملية غير صحيحة"
                return

            self.ids.result.text = f"الناتج: {result}"
        except ValueError:
            self.ids.result.text = "يرجى إدخال أرقام صحيحة"

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == "__main__":
    CalculatorApp().run()
