# @Author YoungMinKim
import matplotlib.pyplot as plt
def show_height(ax,fontsize=10):
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2., height + 0.1,height ,ha="center",fontsize=fontsize)