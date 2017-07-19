# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:36:15 2015

@author: benjamin.maclellan
"""

from matplotlib.pyplot import plot, scatter, legend, text, imread, imshow, title, show, savefig
from matplotlib.font_manager import FontProperties

boundaries = raw_input('\nDo you want colour boundaries added to the diagram (Y/N): ')
bound_case = 0
if boundaries in ('y', 'yes', 'ye', 'ya', 'Yes', 'YES', 'Y', 'YEs'):
    boundaries_type = raw_input('Which specifications (MVSS/ECE): ')  
    if boundaries_type in ('mvss', 'mvs', 'fmvss', 'mvss', 'MVSS', 'Mvss', 'FMVSS'):
        bound_case = 1
    elif boundaries_type in ('ece', 'ec', 'eec', 'ECE', 'Ece', 'EC', 'EEC'):
        bound_case = 2
else:
    pass
    
TotalPoints = input("\nHow many chromaticity points would you like plotted: ")

TitleList = []
Xchrom = []
Ychrom = []

for i in xrange(TotalPoints):
    print "\nFor chromaticity point ", i+1, "..."
    
    while True:
        Title = raw_input("What would you like as the name of this point: ")
        if type(Title) is not str:        
            continue
        else:
            TitleList.append(Title)
            break
    
    while True:
        X = input("What is the X coordinate: ")
        if type(X) is not float:        
            continue
        else:
            Xchrom.append(X)
            break
    
    while True:
        Y = input("What is the Y coordinate: ")
        if type(Y) is not float:        
            continue
        else:
            Ychrom.append(Y)
            break

markers = ["*", "D", "o", ">", "s", "<"]
mlen = len(markers)

colours = ["black", "white", "grey", "blue", "green", "magenta", "red"]
clen = len(colours)


for i in xrange(TotalPoints):    
    x = Xchrom[i]
    y = Ychrom[i]
    marker_i = i % mlen
    colour_i = (i+mlen)/mlen - 1  
    
    Title = TitleList[i]    
    scatter(x, y, marker=markers[marker_i], facecolor=colours[colour_i],
    label=Title)

fontP = FontProperties()
fontP.set_size('small')
lgd = legend(loc='upper center', bbox_to_anchor=(1.0, 1.0),
          fancybox=True, shadow=True, ncol=2, prop = fontP)  

#### Spectral Locus
plot([0.1,0.8],[0.9,0.2], c='k')
plot([0.173148,0.73912],[0.00671296,0.26018], c='k')

####************************ Colour Boundaries *********************************

## MVSS
if bound_case == 1:
    ################# Red
    c_red = 'k'

    plot([0.650,0.670], [0.330,0.330] , c=c_red)
    plot([0.670,0.735], [0.330,0.265] , c=c_red)
    plot([0.735,0.721], [0.265,0.259] , c=c_red)
    plot([0.721,0.650], [0.259,0.330] , c=c_red)
    text(0.675, 0.26, 'Red', fontsize=6)
    
    ################ Amber
    c_amb = 'k'

    plot([0.545, 0.560],[0.425,0.440], c=c_amb)
    plot([0.560,0.609],[0.440,0.390], c=c_amb)
    plot([0.609,0.597],[0.390, 0.390], c=c_amb)
    plot([0.597,0.545],[0.390, 0.425], c=c_amb)
    text(0.566, 0.44, 'Amber', fontsize=6)

    ################ White
    c_white = 'k'
    plot([0.310,0.453],[0.348,0.440], c=c_white)
    plot([0.453, 0.500],[0.440, 0.440], c=c_white)
    plot([0.500, 0.500], [0.440, 0.380], c=c_white)
    plot([0.500,0.440],[0.380,0.380], c=c_white)
    plot([0.440, 0.310],[0.380, 0.283], c=c_white)
    plot([0.310, 0.310],[0.283, 0.348], c=c_white)
    text(0.45, 0.36, 'White', fontsize=6)
    
    text(0.5, 0.6, 'MVSS Chromaticity \nBoundaries', fontsize=10)

## ECE
elif bound_case == 2:
    ################# Red
    c_red = 'k'
    plot([0.645,0.665], [0.335,0.335] , c=c_red)
    plot([0.665,0.735], [0.335,0.265] , c=c_red)
    plot([0.735,0.721], [0.265,0.259] , c=c_red)
    plot([0.721,0.645], [0.259,0.335] , c=c_red)
    text(0.675, 0.26, 'Red', fontsize=6)
    
    ################ Amber
    c_amb = 'k'
    plot([0.545, 0.560],[0.425,0.440], c=c_amb)
    plot([0.560,0.609],[0.440,0.390], c=c_amb)
    plot([0.609,0.597],[0.390, 0.390], c=c_amb)
    plot([0.597,0.545],[0.390, 0.425], c=c_amb)
    text(0.566, 0.44, 'Amber', fontsize=6)
    
    ################ White
    c_white = 'k'
    plot([0.310,0.453],[0.348,0.440], c=c_white)
    plot([0.453, 0.500],[0.440, 0.440], c=c_white)
    plot([0.500, 0.500], [0.440, 0.382], c=c_white)
    plot([0.500,0.443],[0.382,0.382], c=c_white)
    plot([0.443, 0.310],[0.382, 0.283], c=c_white)
    plot([0.310, 0.310],[0.283, 0.348], c=c_white)
    text(0.45, 0.36, 'White', fontsize=6)
    
    text(0.5, 0.6, 'ECE Chromaticity \nBoundaries', fontsize=10)

else:
    pass

#####****************************************************************************

im = imread('CIE1931_Background.png')
implot = imshow(im, alpha=0.3, extent=[0, 0.8, 0, 0.9])

title('CIE 1931 Chromaticity Diagram')
savefig('__Most_Recent_Chromaticity_Diagram.png', bbox_extra_artists=lgd)          
show()
