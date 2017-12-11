#!/usr/bin/env python
#
# Copyright 2015 Falldog Hsieh <falldog7@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys

from .meta_path import PyeMetaPathFinder

from . import _pyconcrete

info = _pyconcrete.info
encrypt_file = _pyconcrete.encrypt_file
decrypt_file = _pyconcrete.decrypt_file
decrypt_buffer = _pyconcrete.decrypt_buffer

sys.meta_path.insert(0, PyeMetaPathFinder())
