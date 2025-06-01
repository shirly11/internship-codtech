# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 22:23:33 2025

@author: ADMIN
"""
#1/6/25
#AUTOMATED REPORT GENERATION


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data.csv")


total = df['Value'].sum()
average = df['Value'].mean()
max_item = df.loc[df['Value'].idxmax(), 'Item']
min_item = df.loc[df['Value'].idxmin(), 'Item']


plt.figure(figsize=(6, 4))
plt.bar(df['Item'], df['Value'], color='skyblue')
plt.title('Item Values')
plt.xlabel('Items')
plt.ylabel('Values')
plt.tight_layout()
plt.savefig('bar_chart.png') 
plt.close()


fig, ax = plt.subplots(figsize=(8.27, 11.69))  
ax.axis('off') 

report_text = (
    "Simple Data Report\n\n"
    f"Total Value: {total}\n"
    f"Average Value: {average:.2f}\n"
    f"Highest Value Item: {max_item}\n"
    f"Lowest Value Item: {min_item}\n\n"
    "Bar Chart shown below:"
)


ax.text(0.05, 0.9, report_text, fontsize=12, va='top')
\
chart_img = plt.imread('bar_chart.png')
ax.imshow(chart_img, extent=(0.05, 0.95, 0.1, 0.55)) 

fig.savefig('Final_Report.pdf', format='pdf')

print("PDF report saved as 'Final_Report.pdf'")
