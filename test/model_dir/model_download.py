from google_drive_downloader import GoogleDriveDownloader as gdd
import os
import gdown
from zipfile import ZipFile

def download_googledrive_model_gdd(google_id,destination_path,remove_zip=True):
    """
    This function is to download google drive zip file

    Parameters
    ----------
    google_id : string
        google share link id

    destination_path : string
         The destination path of your download file, it should end with .zip

    """

    gdd.download_file_from_google_drive(file_id=google_id,
                                        dest_path=destination_path,
                                        unzip=True)
    
    print("INFO: Google file has been downloaded!")
    if remove_zip==True:
        if os.path.exists(destination_path):
            os.remove(destination_path)
            print("INFO: Download zip has been removed!")
            
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
    
    
"""
# pointpillar_attentive_fusion            
gid1 = '1p8JbMtd4ClvgOMlsgqDzhE5Xf-JIrDJa'
# pointpillar_early_fusion
gid2 = '1DXmPX61Ij9M-rqCnTN8pGmpvQzawRynS'
# pointpillar_fcooper
gid3 = '1LotwAUey9ywkxyhOC5GeTlzLBZb_YYxi'
yaml_googledrive_id = "12XnKie7eeQPDsrJFf-lX5rnOzM2up01h"
https://drive.google.com/file/d/12XnKie7eeQPDsrJFf-lX5rnOzM2up01h/view?usp=sharing
gids = [gid1,gid2]

filePath = './model.zip'

# download_googledrive_model(gid3,filePath,remove_zip=True)

gdd.download_file_from_google_drive(file_id=yaml_googledrive_id,
                                    dest_path=filePath,
                                    unzip=True)

if os.path.exists(filePath):
    os.remove(filePath)
"""
"""
for gid in gids:
    print('current_id:',gid)
    download_googledrive_model(gid,filePath,remove_zip=True)
"""

"""
# google direct link
#url = 'https://drive.google.com/uc?export=download&id=12XnKie7eeQPDsrJFf-lX5rnOzM2up01h'
gid = '12XnKie7eeQPDsrJFf-lX5rnOzM2up01h'

filePath = './model.zip'
gdown.download(id=gid,output=filePath, quiet=False)

with ZipFile(filePath, 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

if os.path.exists(filePath):
    os.remove(filePath)
"""    

"""
url = 'https://drive.google.com/drive/folders/17jXzqzpj5r7Ii14XFdlYgnibdFTWJFw3?usp=sharing'   
gdown.download_folder(url, quiet=False, use_cookies=False)
"""

gurl1 = 'https://drive.google.com/uc?export=download&id=1p8JbMtd4ClvgOMlsgqDzhE5Xf-JIrDJa'
mname1 = 'pointpillar_attentive_fusion'

gurl2 = 'https://drive.google.com/uc?export=download&id=1DXmPX61Ij9M-rqCnTN8pGmpvQzawRynS'
mname2 = 'pointpillar_early_fusion'

gurl3 = 'https://drive.google.com/uc?export=download&id=12XnKie7eeQPDsrJFf-lX5rnOzM2up01h'
mname3 = 'pointpillar_fcooper'

gurl4 = 'https://drive.google.com/uc?export=download&id=14oKDS8gQZFX1D2YUlyELYUd36mkITBWS'
mname4 = 'pointpillar_late_fusion'

gurl5 = 'https://drive.google.com/uc?export=download&id=1GUcnFknFAlxF_SAKwKC05u_PeuBHwpHO'
mname5 = 'v2vnet'

gurl6 = 'https://drive.google.com/uc?export=download&id=1VTXfpXzmdgjrqGx7N427PhZRQikcm-P0'
mname6 = 'voxelnet_early_fusion'

gurl7 = 'https://drive.google.com/uc?export=download&id=13GaArq37WHv9vqp8oSIPRQx4ckF9WS65'
mname7 = 'voxelnet_attentive_fusion'

gurl8 = 'https://drive.google.com/uc?export=download&id=13eKXp4i3ecDMyzWdhutp3CsQeLMwlnJz'
mname8 = 'second_early_fusion'

gurl9 = 'https://drive.google.com/uc?export=download&id=1_kL56M-VzBa0gEWjJpLEjpKtwciPa9X_'
mname9 = 'second_attentive_fusion'

gurl10 = 'https://drive.google.com/uc?export=download&id=18dddhjShLrZjVm1mQH1vqbkG0-5W_8IV'
mname10 = 'second_late_fusion'

gurl11 = 'https://drive.google.com/uc?export=download&id=1slhZL21hcnmdyICf1jo_P3ydJRhhVhGd'
mname11 = 'pixor_early_fusion'

gurls = [gurl1,gurl2,gurl3,gurl4,gurl5,gurl6,gurl7,gurl8,gurl9,gurl10,gurl11]
mnames = [mname1,mname2,mname3,mname4,mname5,mname6,mname7,mname8,mname9,mname10,mname11]

for i in range(len(gurls)):
    gurl = gurls[i]
    mname = mnames[i]
    download_googledrive_zipmodel_gdown(gurl,mname + '.zip',remove_zip=True)