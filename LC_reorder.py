import os
import shutil

#config
downloads=os.getcwd()+'/downloads'
themes_folder=os.getcwd()+'/themes'
discrete=os.getcwd() + '/discrete'

#lista cartelle in una subfolder
folders= [f for f in os.listdir(downloads) if os.path.splitext(f)[-1]=='']
#print (folders)

#create discrete folder
if not os.path.exists(discrete):
    os.mkdir(discrete)

#crea cartelle tematiche

landcover=['water-seasonal',]#'water-permanent', 'snow', ]
if not os.path.exists(themes_folder):
    os.mkdir(themes_folder)

for l in landcover:
    if not os.path.exists(themes_folder + '/' + l):
        os.mkdir(themes_folder + '/' + l)

for d in folders:
    tifList=[str(os.path.join(downloads, d, f)) for f in os.listdir(downloads + '/' + d) if os.path.splitext(f)[-1]=='.tif']
    for af in tifList:
            if '-layer_' in af:
                for lc in landcover:
                    if lc in af:
                        dest = os.path.join(themes_folder, lc, os.path.basename(af))
                        #shutil.move(af, dest)
                        shutil.copy(af, dest)
                        print(af + ' moved to ' + dest)

            if '_discrete-classification_' in af:
                dest = os.path.join(discrete, os.path.basename(af))
                #shutil.move(af, dest)
                shutil.copy(af, dest)
                print(af + ' moved to ' + dest)









