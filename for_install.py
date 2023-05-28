"""
#インストールするパッケージをリストアップしとけば一旦いいかという結論
#参考： https://colab.research.google.com/drive/1E_D9jUYHnxHNKSfQTxBJjlaLhhgZxxbB#scrollTo=wWDLxGK1gpvZ

#自動pip install https://vaaaaaanquish.hatenablog.com/entry/2018/12/02/210647

import pip, importlib

def _import(module, ver=None):
    try:
        pip.main('install', module, ver)
    except ImportError:
        try:
            if ver is None:
                pip.main('install', module)
            else:
                pip.main('install', '{}=={}'.format(module, ver))
                importlib.import_module(module)
        except:
            print("can't import: {}".format(module))

if __name__ == "__for_install__":
    _import('pyyaml', '5.1')
    
    #git clone 'https://github.com/facebookresearch/detectron2' は済ませておいてください
    import os, sys, pip, site, distutils.core

    dist = distutils.core.run_setup("./detectron2/setup.py") # ディレクトリ構造を確認してください

    #!python -m pip install {' '.join([f"'{x}'" for x in dist.install_requires])}
    _import(''.join([f"'{x}'" for x in dist.install_requires]), None)
    _import('torch')
    importlib.reload(site)

    # Properly install detectron2. (Please do not install twice in both ways)
    # _import('git+https://github.com/facebookresearch/detectron2.git')<-?

    sys.path.insert(0, os.path.abspath('./detectron2'))

    import torch, detectron2

    print("torch version           :", torch.__version__)
    print("torch cuda is available :", torch.cuda.is_available())
    print("detectron2 version      :", detectron2.__version__)



# Note: This is a faster way to install detectron2 in Colab, but it does not include all functionalities.
# See https://detectron2.readthedocs.io/tutorials/install.html for full installation instructions
"""