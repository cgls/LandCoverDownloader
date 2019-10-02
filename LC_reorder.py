import os
import shutil

#config
downloads=os.getcwd()+'/downloads'
themes_folder=os.getcwd()+'/themes'
discrete=os.getcwd() + '/discrete'
StDev=os.getcwd() + '/StDev'
DataDensity=os.getcwd() + '/DataDensity'

#lista cartelle in una subfolder
folders= [f for f in os.listdir(downloads) if os.path.splitext(f)[-1]=='']
#print (folders)

#create new folder
if not os.path.exists(discrete):
    os.mkdir(discrete)
if not os.path.exists(StDev):
    os.mkdir(StDev)
if not os.path.exists(DataDensity):
    os.mkdir(DataDensity)

#create subfolders

landcover=['urban','tree','shrub','moss','grass','bare','crops','forest','water-seasonal','water-permanent', 'snow']
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
                        shutil.move(af, dest)
                        #shutil.copy(af, dest)
                        print('LC class ' + af + ' moved to ' + dest)
            if '-StdDev' in af:
                for lc in landcover:
                    if lc in af:
                        dest = os.path.join(StDev, lc, os.path.basename(af))
                        shutil.move(af, dest)
                        #shutil.copy(af, dest)
                        print('StDev ' + af + ' moved to ' + dest)
                        
            if '_discrete-classification_' in af:
                dest = os.path.join(discrete, os.path.basename(af))
                shutil.move(af, dest)
                #shutil.copy(af, dest)
                print(af + ' moved to ' + dest)

             if 'DataDensityIndicator' in af:
                dest = os.path.join(DataDensity, os.path.basename(af))
                shutil.move(af, dest)
                #shutil.copy(af, dest)
                print(af + ' moved to ' + dest)

print('The end')
