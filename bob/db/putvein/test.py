#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Philip Abbet <philip.abbet@idiap.ch>
#
# Copyright (C) 2016 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import unittest
from .query import Database


class PUTVeinDatabaseTest(unittest.TestCase):

    def do_query_simple_protocol_tests(self, protocol):
        db = Database()

        objs = db.objects(protocol)
        self.assertEqual(len(objs), 1800) # number of images in the protocol

        objs = db.objects(protocol, kinds='palm')
        self.assertEqual(len(objs), 900) # number of palm images in the protocol

        objs = db.objects(protocol, kinds='wrist')
        self.assertEqual(len(objs), 900) # number of wrist images in the protocol

        objs = db.objects(protocol, groups='train')
        self.assertEqual(len(objs), 600) # number of train images in the protocol

        objs = db.objects(protocol, groups='dev')
        self.assertEqual(len(objs), 600) # number of dev images in the protocol

        objs = db.objects(protocol, groups='eval')
        self.assertEqual(len(objs), 600) # number of dev eval in the protocol

        objs = db.objects(protocol, kinds='palm', groups='train')
        self.assertEqual(len(objs), 300) # number of palm train images in the protocol

        objs = db.objects(protocol, kinds='palm', groups='dev')
        self.assertEqual(len(objs), 300) # number of palm dev images in the protocol

        objs = db.objects(protocol, kinds='palm', groups='eval')
        self.assertEqual(len(objs), 300) # number of palm dev eval in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='train')
        self.assertEqual(len(objs), 300) # number of wrist train images in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='dev')
        self.assertEqual(len(objs), 300) # number of wrist dev images in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='eval')
        self.assertEqual(len(objs), 300) # number of wrist dev eval in the protocol

        objs = db.objects(protocol, kinds='palm', groups='dev', purposes='enroll')
        self.assertEqual(len(objs), 100) # number of palm dev enroll images in the protocol

        objs = db.objects(protocol, kinds='palm', groups='dev', purposes='probe')
        self.assertEqual(len(objs), 200) # number of palm dev probe images in the protocol

        objs = db.objects(protocol, kinds='palm', groups='eval', purposes='enroll')
        self.assertEqual(len(objs), 100) # number of palm dev enroll eval in the protocol

        objs = db.objects(protocol, kinds='palm', groups='eval', purposes='probe')
        self.assertEqual(len(objs), 200) # number of palm dev probe eval in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='dev', purposes='enroll')
        self.assertEqual(len(objs), 100) # number of wrist dev enroll images in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='dev', purposes='probe')
        self.assertEqual(len(objs), 200) # number of wrist dev probe images in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='eval', purposes='enroll')
        self.assertEqual(len(objs), 100) # number of wrist eval enroll in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='eval', purposes='probe')
        self.assertEqual(len(objs), 200) # number of wrist eval probe in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='eval', purposes='probe', ids=[26])
        self.assertEqual(len(objs), 8) # number of wrist eval probe in the protocol for client #26

        if protocol == 'L':
            self.assertEqual(objs[0].make_path(), 'Wrist/o_026/Left/Series_2/W_o026_L_S2_Nr1.bmp')
        else:
            self.assertEqual(objs[0].make_path(), 'Wrist/o_026/Right/Series_2/W_o026_R_S2_Nr1.bmp')

        for obj in objs:
            self.assertEqual(obj.get_client_id(), 26)
            self.assertEqual(obj.is_mirrored(), False)


    def do_query_combined_protocol_tests(self, protocol):
        db = Database()

        objs = db.objects(protocol)
        self.assertEqual(len(objs), 7200) # number of images in the protocol

        objs = db.objects(protocol, kinds='palm')
        self.assertEqual(len(objs), 3600) # number of palm images in the protocol

        objs = db.objects(protocol, kinds='wrist')
        self.assertEqual(len(objs), 3600) # number of wrist images in the protocol

        objs = db.objects(protocol, groups='train')
        self.assertEqual(len(objs), 1200) # number of train images in the protocol

        objs = db.objects(protocol, groups='dev')
        self.assertEqual(len(objs), 1200) # number of dev images in the protocol

        objs = db.objects(protocol, groups='eval')
        self.assertEqual(len(objs), 1200) # number of dev eval in the protocol

        objs = db.objects(protocol, kinds='palm', groups='train')
        self.assertEqual(len(objs), 600) # number of palm train images in the protocol

        objs = db.objects(protocol, kinds='palm', groups='dev')
        self.assertEqual(len(objs), 600) # number of palm dev images in the protocol

        objs = db.objects(protocol, kinds='palm', groups='eval')
        self.assertEqual(len(objs), 600) # number of palm dev eval in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='train')
        self.assertEqual(len(objs), 600) # number of wrist train images in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='dev')
        self.assertEqual(len(objs), 600) # number of wrist dev images in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='eval')
        self.assertEqual(len(objs), 600) # number of wrist dev eval in the protocol

        objs = db.objects(protocol, kinds='palm', groups='dev', purposes='enroll')
        self.assertEqual(len(objs), 200) # number of palm dev enroll images in the protocol

        objs = db.objects(protocol, kinds='palm', groups='dev', purposes='probe')
        self.assertEqual(len(objs), 400) # number of palm dev probe images in the protocol

        objs = db.objects(protocol, kinds='palm', groups='eval', purposes='enroll')
        self.assertEqual(len(objs), 200) # number of palm dev enroll eval in the protocol

        objs = db.objects(protocol, kinds='palm', groups='eval', purposes='probe')
        self.assertEqual(len(objs), 400) # number of palm dev probe eval in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='dev', purposes='enroll')
        self.assertEqual(len(objs), 200) # number of wrist dev enroll images in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='dev', purposes='probe')
        self.assertEqual(len(objs), 400) # number of wrist dev probe images in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='eval', purposes='enroll')
        self.assertEqual(len(objs), 200) # number of wrist eval enroll in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='eval', purposes='probe')
        self.assertEqual(len(objs), 400) # number of wrist eval probe in the protocol

        objs = db.objects(protocol, kinds='wrist', groups='dev', purposes='probe', ids=[26])
        self.assertEqual(len(objs), 8) # number of wrist dev probe in the protocol for client #26

        if protocol == 'LR':
            self.assertEqual(objs[0].make_path(), 'Wrist/o_026/Left/Series_2/W_o026_L_S2_Nr1.bmp')
        else:
            self.assertEqual(objs[0].make_path(), 'Wrist/o_026/Right/Series_2/W_o026_R_S2_Nr1.bmp')

        for obj in objs:
            self.assertEqual(obj.get_client_id(), 26)
            self.assertEqual(obj.is_mirrored(), False)

        objs = db.objects(protocol, kinds='wrist', groups='eval', purposes='probe', ids=[76])
        self.assertEqual(len(objs), 8) # number of wrist eval probe in the protocol for client #76

        if protocol == 'LR':
            self.assertEqual(objs[0].make_path(), 'Wrist/o_026/Right/Series_2/W_o026_R_S2_Nr1.bmp')
        else:
            self.assertEqual(objs[0].make_path(), 'Wrist/o_026/Left/Series_2/W_o026_L_S2_Nr1.bmp')

        for obj in objs:
            self.assertEqual(obj.get_client_id(), 76)
            self.assertEqual(obj.is_mirrored(), True)


    def test_query_L_protocol(self):
        self.do_query_simple_protocol_tests('L')


    def test_query_R_protocol(self):
        self.do_query_simple_protocol_tests('R')


    def test_query_LR_protocol(self):
        self.do_query_combined_protocol_tests('LR')


    def test_query_RL_protocol(self):
        self.do_query_combined_protocol_tests('RL')


    def test_dumplist(self):
      from bob.db.base.script.dbmanage import main
      self.assertEqual(main('put_vein dumplist --protocol=L --self-test'.split()), 0)



if __name__ == '__main__':
    unittest.main()
