import os, tkinter, tkinter.filedialog, tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import signal, fftpack
import seaborn as sns
sns.set_style("ticks", {'grid.linestyle': '--'})

# 解析するcsvファイルのリストを作成する
files = os.listdir('./signal_data')
csv_list = []
for file in files:
    if file.endswith('.csv'):
        csv_list.append(file)

# 振幅変調を解析する範囲を決定する
root = tkinter.Tk()
root.withdraw()
fTyp = [('','*')]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('アナウンス','振幅変調を解析する範囲を決定してください')

file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

print(file)
