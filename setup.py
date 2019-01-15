# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# 此文件安装文件，python脚本（其实也可以用命令行安装qiskit : pip install qiskit）
from setuptools import setup, find_packages
# setuptools  作为Python标准的打包及分发工具 ;自动安装依赖  http://python.jobbole.com/87240/

# 依赖的包
requirements = [
    "jsonschema>=2.6,<2.7",
    "marshmallow>=2.17.0,<3",  # simplified object serialization https://marshmallow.readthedocs.io/en/3.0/
    "marshmallow_polyfield>=3.2,<4", #https://pypi.org/project/marshmallow-polyfield/
    "networkx>=2.2",  #http://networkx.github.io/
    "numpy>=1.13", #http://www.numpy.org/
    "pillow>=4.2.1", # https://pypi.org/project/Pillow/  Python Imaging Library
    "ply>=3.10", # PLY is an implementation of lex and yacc parsing tools for Python.  http://www.dabeaz.com/ply/
    "psutil>=5",  #  获取系统信息  https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001511052957192bb91a56a2339485c8a8c79812b400d49000
    "requests>=2.19", #http://docs.python-requests.org/zh_CN/latest/user/quickstart.html 
    "requests-ntlm>=1.1.0", # https://github.com/requests/requests-ntlm  https://www.innovation.ch/personal/ronald/ntlm.html
    "scipy>=0.19,!=0.19.1", # https://www.jianshu.com/p/1a3db06e786d
    "sympy>=1.3"  #https://www.sympy.org/en/index.html  http://www.cnblogs.com/huiyang865/p/5823751.html
]

# setuptools ==> 安装动作  setup  这个方法有他自己的逻辑吧（https://pythonhosted.org/an_example_pypi_project/setuptools.html）
# 用docker https://hub.docker.com/r/qiskit/qiskit-tutorial  https://hub.mybinder.org/user/qiskit-qiskit-tutorial-xa619t2e/notebooks/index.ipynb
setup(
    name="qiskit-terra",
    version="0.8.0",
    description="Software for developing quantum computing programs",
    long_description="""Terra provides the foundations for Qiskit. It allows the user to write 
        quantum circuits easily, and takes care of the constraints of real hardware.""",
    url="https://github.com/Qiskit/qiskit-terra",
    author="Qiskit Development Team",
    author_email="qiskit@qiskit.org",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    packages=find_packages(exclude=['test*']), #类似路径 hoempath吧
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.5",
    extra_requires={
        'visualization': ['matplotlib>=2.1', 'nxpd>=0.2', 'ipywidgets>=7.3.0',
                          'pydot'],
        'full-featured-simulators': ['qiskit-aer>=0.1']
    }
)
