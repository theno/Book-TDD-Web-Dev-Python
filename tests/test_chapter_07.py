#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from book_parser import Command, Output
from book_tester import ChapterTest

class Chapter7Test(ChapterTest):
    chapter_no = 7

    def test_listings_and_commands_and_output(self):
        self.parse_listings()

        # sanity checks
        self.assertEqual(self.listings[0].type, 'code listing with git ref')
        self.assertEqual(type(self.listings[1]), Command)
        self.assertEqual(type(self.listings[2]), Output)

        self.sourcetree.start_with_checkout(self.chapter_no)
        # other prep
        self.sourcetree.run_command('python3 manage.py syncdb --noinput')

        # skips
        self.skip_with_check(25, 'the -b means ignore whitespace')
        self.skip_with_check(28, 'leave static, for now')
        self.skip_with_check(51, 'will now show all the bootstrap')

        # hack fast-forward
        skip = False
        if skip:
            self.pos = 55
            self.sourcetree.run_command('git checkout {0}'.format(
                self.sourcetree.get_commit_spec('ch07l018')
            ))

        while self.pos < len(self.listings):
            print(self.pos)
            self.recognise_listing_and_process_it()


        self.assert_all_listings_checked(self.listings)
        self.check_final_diff(self.chapter_no, ignore_moves=True)


if __name__ == '__main__':
    unittest.main()
