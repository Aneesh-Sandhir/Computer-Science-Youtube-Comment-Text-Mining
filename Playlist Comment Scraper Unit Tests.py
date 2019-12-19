# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:32:38 2019

@author: anees
"""

#"""
#Created on Fri Jul 19 13:27:19 2019

#@author: Aneesh Sandhir(as6bw)  Devan Visvalingam (dv5mx)  
#"""

import unittest
import Playlist_Comment_Scraper

from Playlist_Comment_Scraper import *

class EnrollInTestCase(unittest.TestCase): # inherit from unittest.TestCase
    # Unit testing enrollInCourse() method in AStudent_Class.py
    
    def test_is_constructed_correctly(self):
        # Test if an instance of a Scraper object is saved with search_string attributed verbatim to the specified value 
        tSeries = Playlist_Comment_Scraper('T-Series', 'channel','Tu Cheez Badi Hai')
        self.assertNotEqual(tSeries.search_string, "tseries")
    def test_is_constructed_correctly_2(self):
        # Test if an instance of a Scraper object can be created with the search_type attribute equal to playlist
        ta13oo = Playlist_Comment_Scraper('Ta1300', 'playlist','Taboo')
        self.assertEqual(ta13oo.search_type, 'playlist' )
    def test_is_constructed_correctly_3(self):
        # Test if an instance of a Scraper object is created with a valid API Key
        truth = Playlist_Comment_Scraper('Flat Earth', 'playlist','Teach the Controversy')
        self.assertEqual(truth.api_key, "AIzaSyDiUlx08HiRDjrXVIbwjPX9pooNNsVZ64o" )
    def test_create_file_name(self):
        # Tests if the create file name function stips restricted characters which would otherwise prevent a file from being created on a given OS
        denzel_curry = Playlist_Comment_Scraper('Ta1300', 'playlist', "Album of the Year")
        self.assertNotIn('|',denzel_curry.create_file_name("Denzel Curry - BLACK BALLOONS | 13LACK 13ALLOONZ ft. Twelve'len, GoldLink"))
    def test_create_file_name_2(self):
        # Tests if the create file name function simply adds the file extension for string which possess no restricted characters
        uLT = Playlist_Comment_Scraper('denzel curry imperial', 'playlist', "Nation of ULT")
        self.assertEqual('Denzel Curry - ULT Imperial - Full Album Stream.txt', uLT.create_file_name('Denzel Curry - ULT Imperial - Full Album Stream'))
    def test_get_top_playlist_response(self):
        # Tests if the number of items in the response from the Youtube Data API is 20 for a playlist which length exceeds 20 videos
        katie_Banks = Playlist_Comment_Scraper('Katie Banks', 'channel', 'Thirsty')
        self.assertEqual(len(katie_Banks.get_top_playlist_response()['items']),20)
    def test_get_top_playlist_response_2(self):
        # Tests if the number of items in the response from the Youtube Data API is equal to the number of videos in a playlist if said playlist has fewer than 20 videos
        ashley_Alban = Playlist_Comment_Scraper('Ashley Alban Serious Shizz', 'playlist', 'Thirstier')
        self.assertLess(len(ashley_Alban.get_top_playlist_response()['items']),20)
    def test_export_all_comments_on_a_playlist(self):
        # Tests if the export_all_comments_on_a_playlist method can appropriately handle multiple videos with zero comments
        bennyMcGhee = Playlist_Comment_Scraper('Benny McGhee', 'channel', 'No Comments')
        self.assertGreater(bennyMcGhee.export_all_comments_on_a_playlist(), (-1))
    def test_export_all_comments_on_a_playlist_2(self):
        # Tests if the export_all_comments_on_a_playlist method can appropriately handle multiple videos with more than 100 comments
        mahalo_my_dude = Playlist_Comment_Scraper('Mahalo My Dude', 'channel', "Shredding Gnar")
        self.assertGreater(mahalo_my_dude.export_all_comments_on_a_playlist(), 2000)

if __name__ == '__main__':
    unittest.main()            