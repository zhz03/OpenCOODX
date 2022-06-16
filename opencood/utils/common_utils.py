# -*- coding: utf-8 -*-
# Author: Runsheng Xu <rxx3386@ucla.edu>, Hao Xiang <haxiang@g.ucla.edu>,
# License: TDG-Attribution-NonCommercial-NoDistrib


"""
Common utilities
"""

import numpy as np
import torch
from shapely.geometry import Polygon
import os
import gdown
from zipfile import ZipFile


def check_numpy_to_torch(x):
    if isinstance(x, np.ndarray):
        return torch.from_numpy(x).float(), True
    return x, False


def check_contain_nan(x):
    if isinstance(x, dict):
        return any(check_contain_nan(v) for k, v in x.items())
    if isinstance(x, list):
        return any(check_contain_nan(itm) for itm in x)
    if isinstance(x, int) or isinstance(x, float):
        return False
    if isinstance(x, np.ndarray):
        return np.any(np.isnan(x))
    return torch.any(x.isnan()).detach().cpu().item()


def rotate_points_along_z(points, angle):
    """
    Args:
        points: (B, N, 3 + C)
        angle: (B), radians, angle along z-axis, angle increases x ==> y
    Returns:

    """
    points, is_numpy = check_numpy_to_torch(points)
    angle, _ = check_numpy_to_torch(angle)

    cosa = torch.cos(angle)
    sina = torch.sin(angle)
    zeros = angle.new_zeros(points.shape[0])
    ones = angle.new_ones(points.shape[0])
    rot_matrix = torch.stack((
        cosa, sina, zeros,
        -sina, cosa, zeros,
        zeros, zeros, ones
    ), dim=1).view(-1, 3, 3).float()
    points_rot = torch.matmul(points[:, :, 0:3].float(), rot_matrix)
    points_rot = torch.cat((points_rot, points[:, :, 3:]), dim=-1)
    return points_rot.numpy() if is_numpy else points_rot


def rotate_points_along_z_2d(points, angle):
    """
    Rorate the points along z-axis.
    Parameters
    ----------
    points : torch.Tensor / np.ndarray
        (N, 2).
    angle : torch.Tensor / np.ndarray
        (N,)

    Returns
    -------
    points_rot : torch.Tensor / np.ndarray
        Rorated points with shape (N, 2)

    """
    points, is_numpy = check_numpy_to_torch(points)
    angle, _ = check_numpy_to_torch(angle)
    cosa = torch.cos(angle)
    sina = torch.sin(angle)
    # (N, 2, 2)
    rot_matrix = torch.stack((cosa, sina, -sina, cosa), dim=1).view(-1, 2,
                                                                    2).float()
    points_rot = torch.einsum("ik, ikj->ij", points.float(), rot_matrix)
    return points_rot.numpy() if is_numpy else points_rot


def remove_ego_from_objects(objects, ego_id):
    """
    Avoid adding ego vehicle to the object dictionary.

    Parameters
    ----------
    objects : dict
        The dictionary contained all objects.

    ego_id : int
        Ego id.
    """
    if ego_id in objects:
        del objects[ego_id]


def retrieve_ego_id(base_data_dict):
    """
    Retrieve the ego vehicle id from sample(origin format).

    Parameters
    ----------
    base_data_dict : dict
        Data sample in origin format.

    Returns
    -------
    ego_id : str
        The id of ego vehicle.
    """
    ego_id = None

    for cav_id, cav_content in base_data_dict.items():
        if cav_content['ego']:
            ego_id = cav_id
            break
    return ego_id


def compute_iou(box, boxes):
    """
    Compute iou between box and boxes list
    Parameters
    ----------
    box : shapely.geometry.Polygon
        Bounding box Polygon.
import os
import gdown
from zipfile import ZipFile
    boxes : list
        List of shapely.geometry.Polygon.

    Returns
    -------
    iou : np.ndarray
        Array of iou between box and boxes.

    """
    # Calculate intersection areas
    iou = [box.intersection(b).area / box.union(b).area for b in boxes]

    return np.array(iou, dtype=np.float32)


def convert_format(boxes_array):
    """
    Convert boxes array to shapely.geometry.Polygon format.
    Parameters
    ----------
    boxes_array : np.ndarray
        (N, 4, 2) or (N, 8, 3).

    Returns
    -------
        list of converted shapely.geometry.Polygon object.

    """
    polygons = [Polygon([(box[i, 0], box[i, 1]) for i in range(4)]) for box in
                boxes_array]
    return np.array(polygons)


def torch_tensor_to_numpy(torch_tensor):
    """
    Convert a torch tensor to numpy.

    Parameters
    ----------
    torch_tensor : torch.Tensor

    Returns
    -------
    A numpy array.
    """
    return torch_tensor.numpy() if not torch_tensor.is_cuda else \
        torch_tensor.cpu().detach().numpy()

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
    
    path = outputPath.split("/")
    target_path = os.path.join(*path[:-1])
    
    with ZipFile(outputPath, 'r') as zipObj:
       # Extract all the contents of zip file in current directory
       zipObj.extractall(path=target_path)
       print("INFO: Google file has been unzipped!")

    if remove_zip==True:
        if os.path.exists(outputPath):
            os.remove(outputPath)
            print("INFO: Download zip has been removed!")
            
def root_path_check(path):
    path_list = path.split("/")
    if path_list[-1]=='opencood':
        return True
    else:
        return False
    
def find_root(path):
    """
    Find out the root path of current directory in cood package 

    Parameters
    ----------
    path : string
        abs path for current directory.

    Returns
    -------
    root_path : string
        Root path of current directory

    """
    if root_path_check(path):
        root_path = os.path.dirname(path)
    else:
        root_path = find_root(os.path.dirname(path))
    return root_path 

def update_hypes_dir(root_path,hyper_params):
    """
    Update the directory path in hyper parameters

    Parameters
    ----------
    root_path : string
        Relative path in hyper parameters.

    Returns
    -------
    hyper_params : 
        hyper parameters after update.

    """
    hyper_params['root_dir'] = os.path.join(root_path,hyper_params['root_dir'])
    hyper_params['validate_dir'] = os.path.join(root_path,hyper_params['validate_dir'])
    return hyper_params
    
        
            