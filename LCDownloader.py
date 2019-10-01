import os
import urllib.request

# config

list_file = 'list_url.txt'
dest_fold = 'downloads'

#########
#read list of files to download
f = open(list_file,'r')
data = f.readlines()
files = [ f.rstrip() for f in data ]
f.close()

#create destination folder
abs_dfold = os.getcwd()+'/'+dest_fold
if (not os.path.exists( abs_dfold )):
    os.mkdir( abs_dfold )
else:
    #do whatever if folder exists
    print ('Folder already exists.')
    pass

def download_file(url):
    fname = url.split('/')[-1]
    destf = abs_dfold + '/' + fname.split('_')[0]

    print ('Downloading ' + fname)
    if (not os.path.exists(abs_dfold + '/' + fname) and not os.path.exists(destf)):
        urllib.request.urlretrieve(url, abs_dfold + '/' + fname)
        print (fname+' downloaded in '+abs_dfold)
    else:
        print (fname + ' already downloaded')

def extract_file(fname):
    import zipfile
    destf = abs_dfold + '/' + fname.split('_')[0]
    if (not os.path.exists(destf)):
        os.mkdir(destf)
        print ('Extracting ' + fname)
        with zipfile.ZipFile(abs_dfold + '/' + fname, 'r') as zip_ref:
            zip_ref.extractall(destf)
        print (fname + 'extracted to ' +  destf + '/')
        os.remove(abs_dfold + '/' + fname)
        print (fname + 'removed.')
    else:
        print (fname + ' already extracted')


# test single download
#download = download_file(files[0])
#extract = extract_file( files[0].split('/')[-1] )

# downloading all

for fi in files:
    download = download_file(fi)
    extract = extract_file(fi.split('/')[-1])
