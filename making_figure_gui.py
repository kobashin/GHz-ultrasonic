import os, tkinter, tkinter.filedialog, tkinter.messagebox
import matplotlib.pyplot as plt
import numpy as np

#show the file selection filedialog
root = tkinter.Tk()
root.withdraw()
fTyp = [('','*')]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('自動イメージ作成プログラム','どのフォルダのcsvでグラフを作るの？')

#output the processing file name
#file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
#tkinter.messagebox.showinfo('oxプログラム',file)

#print(file)
#print(type(file))

#output the processing directory name
dir = tkinter.filedialog.askdirectory(initialdir = iDir)

os.chdir(dir)
plt.figure(figsize=(8,6), dpi=800)

for file in os.listdir(dir):
    if file.count('csv'):
        df = np.loadtxt(file, skiprows=5, delimiter=',', encoding='utf-8')
        rows = len(df[:,0])
        x = np.arange(1, rows + 1)
        plt.plot(x, df[:,1])
        #plt.vlines(np.arange(24800,26400,200), -0.05, 0.05, color='k', linestyle=':', lw=0.5)
        #plt.fill_between([24800,26400], -0.05, 0.05, color='skyblue')
        plt.title(file)
        plt.savefig(str(file[:-4])+'.png')
        plt.clf()
