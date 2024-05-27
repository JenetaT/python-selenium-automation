class BasePage:

    def find_el(self):
        print("Finding element")

    def click(self):
        print("Clicking")


    def verify_text(self, expected_text):
        print("f'Checking for {expected_text}")


class LoginPage(BasePage):

    def login (self, email, pw):
        print('Login...')

    def verify_TC(self):
        self.verify_text('TC text')


class RegPage(BasePage):
    def register(self):
        print('Registering...')