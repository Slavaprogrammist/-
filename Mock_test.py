import unittest
import sys, os
from unittest.mock import patch, Mock

import builder

sys.path.append(os.getcwd())
from builder import *

class Technic_Builder_Test(unittest.TestCase):
    @patch.object(builder.Technic_Builder(), 'telephone')
    def test_telephone(self, mock_telephone):
        mock_telephone.return_value = None
        self.assertEqual(Technic_Builder().telephone(), None)