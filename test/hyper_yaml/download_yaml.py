from urllib import request
from zipfile import ZipFile
import wget

import os
import gdown
from zipfile import ZipFile

"""
url = 'https://drive.google.com/drive/folders/1i39i4L6umif7h5t2no7oHinHySFlZu6O?usp=sharing'

zipurl = 'https://drive.google.com/file/d/1o-QsMcdrXn9gz8gBSClUGT1NLxCtdAIO/view?usp=sharing'

response = request.urlretrieve(zipurl,'yamlfiles.zip')
"""
zipurl = 'https://drive.google.com/file/d/1o-QsMcdrXn9gz8gBSClUGT1NLxCtdAIO/view?usp=sharing'
url = 'https://drive.google.com/drive/folders/1i39i4L6umif7h5t2no7oHinHySFlZu6O?usp=sharing'



# wget.download(zipurl)
"""
with ZipFile('yamlfiles.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
"""

"""
from google_drive_downloader import GoogleDriveDownloader as gdd
import os
 
yaml_googledrive_id = '1yVaBbTU16b1oyi1DfCVT6wvMu31Ydnv4'
filePath = './yamlfiles.zip'

gdd.download_file_from_google_drive(file_id=yaml_googledrive_id,
                                    dest_path=filePath,
                                    unzip=True)

if os.path.exists(filePath):
    os.remove(filePath)
"""    
    
"""
with ZipFile('yamlfiles.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
"""
def download_googledrive_zipmodel_gdown(url,outputPath,remove_zip=True):
    """
    This function is to download 

    Parameters
    ----------
    url : string
        Google direct download url (Not shared link).
    outputPath : string
        Output path.
    remove_zip : bool, optional
        If need to remove download zip files. The default is True.

    Returns
    -------
    None.

    """
    gdown.download(url,output=outputPath, quiet=False)
    print("INFO: Google file has been downloaded!")
    
    with ZipFile(outputPath, 'r') as zipObj:
       # Extract all the contents of zip file in current directory
       zipObj.extractall()
       print("INFO: Google file has been unzipped!")

    if remove_zip==True:
        if os.path.exists(outputPath):
            os.remove(outputPath)
            print("INFO: Download zip has been removed!")
            
yaml_googledrive_url = 'https://drive.google.com/uc?export=download&id=1yVaBbTU16b1oyi1DfCVT6wvMu31Ydnv4' 
filePath = './yamlfiles.zip'
download_googledrive_zipmodel_gdown(yaml_googledrive_url,filePath,remove_zip=True)