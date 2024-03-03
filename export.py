import pandas as pd
def export(dictionary):
    df = pd.DataFrame(data = dictionary, index=[0])
    df = (df.T)
    df.to_excel('dict.xlsx')