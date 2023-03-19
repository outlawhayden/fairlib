from fairlib.src.dataloaders.utils import BaseDataset
from pathlib import Path
import pandas as pd

class HiringDataset(BaseDataset):
    def load_data(self):
        self.filename = "../../../datasets/hiring/mergefinal_cleaned.csv"
        data = pd.read_csv(self.filename)

        self.X = ["occupation","city","gender","skill","employment","type","zipcode","highschool","postsecondary","spanish","computer","liscence","certificate","customerservice","cpr","techsckills","wpm","grammar","college","employeemonth","volunteer","stronglaw"]
        self.y = data["callback"]
        self.protected_label = data["type"]



