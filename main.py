from pprint import pprint

class ChocolateFeast(object):

    def __init__(self, output_file=None):

        self.write_to_file = False
        if output_file is not None:
            self.output_file = output_file
            self.write_to_file = True

        self._cash = 0
        self._price = 0
        self._wrappers_needed = 0
        self._chocolate_type = ""
        self.milk = 0
        self.dark = 0
        self.white = 0
        self.sugar_free = 0

        self.chocolate_machine = {
            "milk": {
                "received": 0,
                "remaining": 0,
                "wrappers": 0
            },
            "dark": {
                "received": 0,
                "remaining": 0,
                "wrappers": 0
            },
            "white": {
                "received": 0,
                "remaining": 0,
                "wrappers": 0
            },
            "sugar_free": {
                "received": 0,
                "remaining": 0,
                "wrappers": 0
            }
        }

        self.trade_in_schedule = {
            "milk": "sugar_free",
            "white": "sugar_free",
            "sugar_free": "dark"
        }

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):

        if isinstance(value, int):
            if value >= 0:
                self._cash = value
            else:
                raise ValueError("cash must be greater than 0")
        else:
            raise TypeError("cash must be an integer")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):

        if isinstance(value, int):
            if value >= 0:
                self._price = value
            else:
                raise ValueError("price must be greater than 0")
        else:
            raise TypeError("price must be an integer")

    @property
    def wrappers_needed(self):
        return self._wrappers_needed

    @wrappers_needed.setter
    def wrappers_needed(self, value):

        if isinstance(value, int):
            if value >= 0:
                self._wrappers_needed = value
            else:
                raise ValueError("wrappers must be greater than 0")
        else:
            raise TypeError("wrappers must be an integer")

    @property
    def chocolate_type(self):
        return self._chocolate_type

    @chocolate_type.setter
    def chocolate_type(self, value):

        valid_values = ["white", "dark", "milk", "sugar_free"]

        if value in valid_values:
            self._chocolate_type = value
        else:
            raise ValueError("valid chocolate types are {}".format(','.join(valid_values)))

    def main(self):

        if not self._cash:
            raise ValueError("missing cash amount")
        if not self._price:
            raise ValueError("missing price amount")
        if not self._wrappers_needed:
            raise ValueError("missing wrappers needed value")
        if not self._chocolate_type:
            raise ValueError("no chocolate type input")

        self.__initial_setup()

        max_attempts = 10
        num_attempts = 0
        while num_attempts < max_attempts and self.__keep_running():
            num_attempts += 1
            self.__run_machine()

        self.__set_final_values()

        if self.write_to_file:
            self.__write_to_file()

        if num_attempts == max_attempts:
            raise RuntimeError("encountered endless loop")

    def __initial_setup(self):

        initial_chocolates = int(self.cash/self.price)
        self.chocolate_machine[self.chocolate_type]['received'] = initial_chocolates
        self.chocolate_machine[self.chocolate_type]['remaining'] = initial_chocolates

    def __keep_running(self):

        keep_running = False

        for k,v in self.chocolate_machine.items():

            if v['wrappers'] > self.wrappers_needed or v['remaining'] > 0:
                keep_running = True

        return keep_running

    def __run_machine(self):

        for k,v in self.chocolate_machine.items():

            if v['remaining'] > 0:
                self.chocolate_machine[k]['wrappers'] += v['remaining']
                self.chocolate_machine[k]['remaining'] = 0

            if v['wrappers'] >= self.wrappers_needed:

                additional_chocolates = int(v['wrappers'] / self.wrappers_needed)
                self.chocolate_machine[k]['received'] += additional_chocolates
                self.chocolate_machine[k]['remaining'] += additional_chocolates
                self.chocolate_machine[k]['wrappers'] = self.chocolate_machine[k]['wrappers'] - (additional_chocolates * self.wrappers_needed)

                if k in self.trade_in_schedule.keys():
                    self.chocolate_machine[self.trade_in_schedule[k]]['received'] += additional_chocolates
                    self.chocolate_machine[self.trade_in_schedule[k]]['remaining'] += additional_chocolates

        self.print_status()

    def __set_final_values(self):

        self.milk = self.chocolate_machine['milk']['received']
        self.dark = self.chocolate_machine['dark']['received']
        self.white = self.chocolate_machine['white']['received']
        self.sugar_free = self.chocolate_machine['sugar_free']['received']

    def __write_to_file(self):

        f = open(self.output_file, 'a')
        f.write("milk {milk},dark {dark},white {white},sugar free {sugar_free}\n".format(
            milk=self.milk,
            dark=self.dark,
            white=self.white,
            sugar_free=self.sugar_free
        ))

    def print_status(self):

        pprint(self.chocolate_machine)