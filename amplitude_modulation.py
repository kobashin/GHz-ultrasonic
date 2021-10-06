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
        csv_list.append('./signal_data/' + file)

'''
# 振幅変調を解析する範囲を決定する
root = tkinter.Tk()
root.withdraw()
fTyp = [('','*')]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('アナウンス','振幅変調を解析する範囲を決定してください')

file = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir, title='Select csv')

df = np.loadtxt(file, skiprows=5, delimiter=',', encoding='utf-8')

rows = len(df[:,0])
x = np.arange(rows)
plt.plot(x, df[:,1])
plt.show()
'''

ampl_list = []
revised_ampl_list = []

for file in csv_list:
    df = np.loadtxt(file, delimiter=',', skiprows=5)
    baseline = df[4000:7000, 1].mean()
    yh = signal.hilbert(df[:,1] - baseline)
    ref = abs(yh[1600:1800]).mean()
    ya1 = abs(yh[9900:10000]).mean()
    ampl_list.append(ya1)
    revised_ampl_list.append(ya1/ref)

x_value = np.arange(750, 1050.1, 0.5)
y_value = np.array(ampl_list)
y_revised = np.array(revised_ampl_list)

# visualize amplitude modulation
plt.figure(1, figsize=(8,6))

plt.subplot(211)
plt.plot(x_value, y_value, linewidth=0.4, color='blue')
plt.ylabel('Amplitude')

plt.subplot(212)
plt.plot(x_value, y_revised, linewidth=0.4, color='blue')
plt.xlabel('Frequency[MHz]')
plt.ylabel('Amplitude / Reference')

plt.show()
