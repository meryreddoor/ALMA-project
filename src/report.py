import pandas as pd  
import numpy as np 
from querysql import getData
import matplotlib
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import os
from fpdf import FPDF
import seaborn as sns
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
import webbrowser as wb

def getReport(idvideo):
    df1 = getData(idvideo)
    
    colors = sns.color_palette("deep")
    fig = plt.figure(figsize=(4,3))
    plt.subplot(3,2,1)
    plt.title("angry", fontsize=10)
    sns.lineplot(data=df1['angry'], color = colors[0])
    plt.subplot(3,2,2)
    plt.title("disgust", fontsize=10)
    sns.lineplot(data=df1["disgust"], color = colors[1])
    plt.subplot(3,2,3)
    plt.title("fear", fontsize=10)
    sns.lineplot(data=df1["fear"], color = colors[2])
    plt.subplot(3,2,4)
    plt.title("happy", fontsize=10)
    sns.lineplot(data=df1["happy"], color = colors[3])
    plt.subplot(3,2,5)
    plt.title("sad", fontsize=10)
    sns.lineplot(data=df1["sadness"], color = colors[4])
    plt.subplot(3,2,6)
    plt.title("surprise", fontsize=10)
    sns.lineplot(data=df1["surprise"], color = colors[5])
    fig.subplots_adjust(wspace=0.4, hspace=0.9)
    plt.savefig('first.png')
    '''
    plt.figure(figsize=(8,3))
    plt.title('A Glimpse at your video Emotions')
    ax = sns.lineplot(data=df1)
    plt.savefig('second.png')
    '''
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('Courier', 'B', 25)
    pdf.cell(200,20,' ',0,2,'C')
    pdf.cell(210,30,"Facial Emotion Recognition", 0, 2, 'C')
    
    pdf.set_font('Courier', 'B', 9)
    pdf.cell(210,5,"Facial emotion recognition is the process of detecting human emotions", 0, 2, 'C')
    pdf.cell(210,5,"from facial expressions. The human brain recognizes emotions automatically, and ", 0, 2, 'C')
    pdf.cell(210,5,"software has now been developed that can recognize emotions as well. ", 0, 2, 'C')
    pdf.cell(210,5,"This technology is becoming more accurate all the time, and will", 0, 2, 'C')
    pdf.cell(210,5,"Facial emotion recognition is the process of detecting human emotions", 0, 2, 'C')
    pdf.cell(210,5,"eventually be able to read emotions as well as our brains do. ", 0, 2, 'C')
    pdf.set_font('Courier', 'B', 12)
    pdf.cell(210,5,"Till then, here you have what ALMA could recognise.", 0, 2, 'C')
    pdf.cell(210,5,"It's something!", 0, 2, 'C')
    
    pdf.cell(30,20)
    pdf.image('first.png', x = None, y = None, w = 0, h = 0, type = '', link = '')

    pdf.cell(25,20)
    pdf.image('7.jpeg', x = None, y = None, w = 0, h = 0, type = '', link = '')

    pdf.set_font('Courier', 'B', 9)
    pdf.cell(90,5,"the most frequent emotion in the video is ANGRY", 0, 2, 'C')

    pdf.set_font('Courier', 'B', 12)
    pdf.cell(90,5,"You were angry, and you know it!", 0, 2, 'C')

    pdf.output('test.pdf', 'F')
    return wb.open_new('test.pdf')
