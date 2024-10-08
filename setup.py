# Copyright 2012 Brian Waldon
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

import setupagents


def parse_requirements():
    fap = open('requirements.txt', 'r')
    raw_req = fap.read()
    fap.close()
    return raw_req.split('\n')


setupagents.setup(
    name='warlock',
    version='1.2.0',
    description='Python object model built on JSON schema and JSON patch.',
    author='Brian Waldon',
    author_email='bcwaldon@gmail.com',
    url='http://github.com/bcwaldon/warlock',
    packages=['warlock'],
    install_requires=parse_requirements(),
)
