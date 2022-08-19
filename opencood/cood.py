import os
import argparse
from opencood.version import __version__

def test_parser():
    parser = argparse.ArgumentParser(description="opencood command")

    parser.add_argument("-V","--version",action='store_true',
                        help="Display version.",
                    )
    parser.add_argument('--model', type=str,
                        default='None',
                        help="Your model name or use [all] to download all models at once.")
    """
    parser.add_argument('--yaml', action='store_true',
                        help='whether to download all yaml files.')
    """

    parser.add_argument('--bbx', action='store_true',
                        help='whether install bbx nms calculation cuda version.')

    parser.add_argument('--data', type=str,
                        default='None',
                        help='What dataset you want to download')
    
    parser.add_argument('--vis_data', type=str,
                        default='None',
                        help='Visualize which dataset')
    
    parser.add_argument('--vis_color', type=str,
                        default='None',
                        help='Visualized dataset color mode')
    
    opt = parser.parse_args()
    return opt

def main():
    opt = test_parser()
    
    # sitepath = site.getsitepackages() # a list 
    c_path = os.path.abspath(os.path.dirname(__file__)) # string
    previous_path = os.getcwd()
    print("Current Working Directory:" , previous_path)
    print(c_path)
    os.chdir(c_path)
    print("Current Working Directory After Change:" , os.getcwd()) 
    
    if opt.version:
        print("opencoodx version:",__version__)
        
    """    
    if opt.yaml:        
        # cmd = 'python ' + ab_path + '/hypes_yaml/download_yaml.py'
        cmd = 'python ' + c_path + '/hypes_yaml/download_yaml.py'
        os.system(cmd)
        print('Yaml files have been downloaded!')
    else:
        print('Reminder: You need to download yaml files before you run the code!')
    """
    
    if opt.model == 'None':
        print('Reminder: You need to download trained model before you run the code!')
    else:
        cmd = 'python ' + c_path + '/model_dir/download_models.py --model ' + opt.model
        os.system(cmd)
        
    if opt.bbx:
        print('previous directory:',previous_path)
        os.chdir(previous_path)
        print("Current Working Directory After Change:" , os.getcwd())
        cmd = 'python ' + c_path + '/utils/setup.py build_ext --inplace' 
        print(cmd)
        os.system(cmd)
    else:
        print('Reminder: You need to install bbx cuda version before you run the code!')
        
    if opt.data=='None':
        print('Reminder: To check data offline,please download dataset!')
    else:
        print('previous directory:',previous_path)
        os.chdir(previous_path)
        print("Current Working Directory After Change:" , os.getcwd())
        
        cmd = 'python ' + c_path + '/visualization/download_dataset.py --data ' + opt.data
        os.system(cmd) 
    
    if opt.vis_data=='None' and opt.vis_color == 'None':
        print('Reminder:To visualize data,please use --vis_data and --vis_color command!')
    
    elif opt.vis_data!='None' and opt.vis_color == 'None':
        
        print('previous directory:',previous_path)
        os.chdir(previous_path)
        print("Current Working Directory After Change:" , os.getcwd())
        
        cmd = 'python ' + c_path + '/visualization/vis_data_sequence.py --data ' + opt.vis_data
        print('cmd',cmd)
        os.system(cmd)
        
    elif opt.vis_data=='None' and opt.vis_color != 'None':
        print('previous directory:',previous_path)
        os.chdir(previous_path)
        print("Current Working Directory After Change:" , os.getcwd())
        
        cmd = 'python ' + c_path + '/visualization/vis_data_sequence.py --color_mode ' + opt.vis_color
        print('cmd',cmd)
        os.system(cmd)
    else:
        print('previous directory:',previous_path)
        os.chdir(previous_path)
        print("Current Working Directory After Change:" , os.getcwd())
        
        cmd = 'python ' + c_path + '/visualization/vis_data_sequence.py --data ' + opt.vis_data + ' --color_mode ' + opt.vis_color
        print('cmd',cmd)
        os.system(cmd)
        
if __name__ == '__main__':
    main()
    

 

    
    

    