"""Given an acronym, correctly identity the full saying to that acronym."""

import random


class Acro_Handle:
    def __init__(self):
        self.acronyms_file_name = "./static/assets/acronyms.txt"
        self.all_acronyms = self.handle_acronyms()

    def handle_acronyms(self) -> dict:
        """Formats the acronyms.txt file"""
        # open file and turn acronyms into list
        with open(self.acronyms_file_name) as file:
            acronym_list = file.readlines()
        acronym_list = [acronym.rstrip() for acronym in acronym_list]

        # turn acronym list into dictionary
        acronym_dict = {}
        for acronym in acronym_list:
            acronym_name, acronym_description = acronym.split("-")
            acronym_dict[acronym_name] = acronym_description

        return acronym_dict

    def get_acro(self, in_acronym: str) -> tuple:
        """Given an input acronym, return it's (name and description)"""
        return in_acronym, self.all_acronyms.get(in_acronym, "No acronym found.")

    def get_random_acronym(self) -> tuple:
        """Returns a random tuple of (acronym, description)"""
        return random.choice(list(self.all_acronyms.items()))
