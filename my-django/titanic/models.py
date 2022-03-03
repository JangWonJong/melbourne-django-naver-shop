from domains import Dataset
import numpy as np
import pandas as pd
import sklearn
class Models:
    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset # 할당 지저분하게 쓰지 않겠다
        this.context = './data/' # 경로설정
        this.fname = payload
        return pd.read_csv(this.context+this.fname) # csv읽어드림