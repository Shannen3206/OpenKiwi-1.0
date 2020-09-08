#  OpenKiwi: Open-Source Machine Translation Quality Estimation
#  Copyright (C) 2019 Unbabel <openkiwi@unbabel.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from torch import optim


def optimizer_class(name):
    if name == 'sgd':
        OptimizerClass = optim.SGD
    elif name == 'adagrad':
        OptimizerClass = optim.Adagrad
    elif name == 'adadelta':
        OptimizerClass = optim.Adadelta
    elif name == 'adam':
        OptimizerClass = optim.Adam
    elif name == 'sparseadam':
        OptimizerClass = optim.SparseAdam
    else:
        raise RuntimeError("Invalid optim method: " + name)
    return OptimizerClass
