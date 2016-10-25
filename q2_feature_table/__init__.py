# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._normalize import rarefy
from ._transform import (presence_absence, relative_frequency)
from ._summarize import (summarize, view_seq_data, view_taxa_data)
from ._merge import (merge, merge_seq_data, merge_taxa_data)
from ._filter import (filter_samples, filter_features)


__version__ = '0.0.5'

__all__ = ['rarefy', 'presence_absence', 'relative_frequency', 'summarize',
           'merge', 'merge_seq_data', 'filter_samples', 'filter_features',
           'merge_taxa_data', 'view_seq_data', 'view_taxa_data']
