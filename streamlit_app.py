import numpy as np
import pandas as pd
import streamlit as st


def func():
    print('hello everyone')
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    return st.line_chart(chart_data)
    
if __name__== '__main__':
    func()
