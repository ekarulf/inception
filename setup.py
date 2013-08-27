#!/usr/bin/env python3
'''
Inception - a FireWire physical memory manipulation and hacking tool exploiting
IEEE 1394 SBP-2 DMA.

Copyright (C) 2011-2013  Carsten Maartmann-Moe

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Created on Jan 14, 2013

@author: Carsten Maartmann-Moe <carsten@carmaa.com> aka ntropy
'''

# Inception's setup.py
from distutils.core import setup
from inception import cfg

setup(
    name = 'inception',
    packages = ['inception'],
    scripts = ['incept'],
    package_data= {'inception': ['resources/oui.txt', 
                                 'resources/inception.wav',
                                 'test/*.py',
                                 'test/samples/*.py',
                                 'test/samples/*.bin']},
    version = cfg.version,
    description = 'Memory manipulation tool exploiting FireWire SBP2 DMA.',
    author = 'Carsten Maartmann-Moe',
    author_email = 'carsten@carmaa.com',
    url = cfg.url,
    download_url = 'http://github.com/carmaa/inception',
    license = 'GPL',
    requires = ['forensic1394'],
    keywords = ['hack', 'physical security', 'firewire'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Security experts',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Topic :: Security']
)
