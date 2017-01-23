from Result import Result
#import the 14 websites
import ebay
import marshallscientific #doesn't work yet
import equipnet
import google
import medwow
import used_line
import eurekaspot
import labcommerce
import newlifescientific
import labx
import biosurplus
import sci_bay
import dotmed
import sibgene

import unittest

#TODO: ignore used line, doesn't work now? used_line.extract_results,
FUNCTIONS=[marshallscientific.extract_results, medwow.extract_results, ebay.extract_results, equipnet.extract_results, google.extract_results,  \
eurekaspot.extract_results, labcommerce.extract_results, newlifescientific.extract_results, biosurplus.extract_results, sci_bay.extract_results, \
dotmed.extract_results, sibgene.extract_results, labx.extract_results] 

WEBSITE_NAMES={ebay.extract_results : "ebay" , equipnet.extract_results : "equipnet" , google.extract_results : "google" , used_line.extract_results : "used line", \
eurekaspot.extract_results : "eurekaspot", labcommerce.extract_results :"labcommerce", newlifescientific.extract_results :"newlifescientific", biosurplus.extract_results: "biosurplus" , sci_bay.extract_results : "sci_bay", \
dotmed.extract_results : "dotmed" , sibgene.extract_results: "sibgene" , labx.extract_results : "labx", medwow.extract_results: "medwow", marshallscientific.extract_results: \
"marshallscientific"}

'''
If any function throws an error the test will fail
Otherwise they will pass
Check manually that these tests print logical outputs
'''
class TestWebScraping(unittest.TestCase):

    def test_blank(self):
    	for func in FUNCTIONS:
    		print "blank test: "
        	print WEBSITE_NAMES[func]
        	print func('', None)

    def test_multiword1(self):
    	for func in FUNCTIONS:
    		print "applied biosystems 9700:"
        	print WEBSITE_NAMES[func]
        	try:
        		print func('applied biosystems 9700')
        	#ignore error caused by printing unicode
        	except TypeError, e: 
        		if "unicode" not in e.message.lower():
        			raise TypeError(e.message)


    def test_multiword2(self):
    	for func in FUNCTIONS:
    		print "Diasorin Liaison:"
        	print WEBSITE_NAMES[func]
        	try:
        		print func('Diasorin Liaison')
        	except TypeError, e: 
        		if "unicode" not in e.message.lower():
        			raise TypeError(e.message)


if __name__ == '__main__':
    unittest.main()