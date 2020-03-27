import matplotlib.pyplot as plt
import numpy as np
import os, tkinter, tkinter.filedialog, tkinter.messagebox

#show the file selection filedialog
root = tkinter.Tk()
root.withdraw()
fTyp = [('','*')]
iDir = os.path.abspath(os.path.dirname(__file__))
#tkinter.messagebox.showinfo('簡易プロットプログラムです','どのフォルダのcsvでグラフを作る？')

#output the processing file name
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
#tkinter.messagebox.showinfo('oxプログラム',file)

df = np.loadtxt(file, skiprows=5, delimiter=',', encoding='utf-8')

rows = len(df[:,0])
x = np.arange(rows)


# 横軸の単位をsecondにしてグラフを見たいときはこちら↓を使う。
#plt.plot(df[:,0], df[:,1])
# 横軸を「1～csvファイルの行数」としてグラフを見たいときはこちら↓を使う。
plt.plot(x, df[:,1])


#plt.vlines(np.arange(24800,26400,200), -0.05, 0.05, color='k', linestyle=':', lw=0.5)
#plt.fill_between([24800,26400], -0.05, 0.05, color='skyblue')

plt.show()
