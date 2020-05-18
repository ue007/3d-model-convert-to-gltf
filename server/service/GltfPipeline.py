import os

def gltf_pipeline(input_path, out_path, is_binary = True):
    command = 'gltf-pipeline -i "'+input_path+'" -o "'+out_path+'" -d'
    if is_binary:
        command += ' -b'
    os.system(command)
    # exists mains success
    return os.path.exists(out_path)

def obj2gltf(input_path, out_path, is_binary = True):
    command = 'obj2gltf -i "'+input_path+'" -o "'+out_path+'" -d'
    if is_binary:
        command += ' -b'
    os.system(command)
    if os.path.exists(out_path):
        return gltf_pipeline(out_path, out_path, is_binary)
    else:
        return False
