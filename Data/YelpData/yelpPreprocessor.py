# -*- coding: utf8 -*-

import json


class YelpPreprocessor:
    '''
    Convert Yelp Preprocessor to a text file consisting of lines
    '''
    def __init__(self):
        return None

    def yelpPreprocess(self, paramFpathInBussiness, paramFpathInReview, paramFpathOutReview, paramFpathOutStars):

        # dictClinicalBussinessCategories = {
        # "Chiropractic and physical therapy":{"includeif":{"chiropractor","physical therapy"},"excludeif":{}},
        # "Dental":{"includeif":{"dentist"},"excludeif":{}},
        # "Dermatology":{"includeif":{"dermatologist"},"excludeif":{"optometrist", "veterinarians", "pets"}},
        # "Family practice":{"includeif":{"family practice"},"excludeif":{"psychiatrist", "chiropractor", "beauty", "physical therapy", "specialty", "dermatologists", "weight loss", "acupuncture", "cannabis clinics", "naturopathic", "optometrists"}},
        # "Hospitals and clinics":{"includeif":{"hospital"},"excludeif":{"physical therapy", "rehab", "retirement homes", "veterinarians", "dentist"}},
        # "Optometry":{"includeif":{"optometrist"},"excludeif":{"dermatologist"}},
        # "Mental health":{"includeif":{"psychiatrist","psychologist"},"excludeif":{}},
        # "Dental":{"includeif":{"speech therapy"},"excludeif":{"speech"}},
        # }
        dictClinicalBussinessCategories = {
        "Chiropractic and physical therapy":{"includeif":{"Chiropractor","Physical Therapy"},"excludeif":set()},
        "Dental":{"includeif":{"Dentist"},"excludeif":set()},
        "Dermatology":{"includeif":{"Dermatologist"},"excludeif":{"Optometrist", "Veterinarians", "Pets"}},
        "Family practice":{"includeif":{"Family Practice"},"excludeif":{"Psychiatrist", "Chiropractor", "Beauty", "Physical Therapy", "Specialty", "Dermatologists", "Weight Loss", "Acupuncture", "Cannabis Clinics", "Naturopathic", "Optometrists"}},
        "Hospitals and clinics":{"includeif":{"Hospital"},"excludeif":{"Physical Therapy", "Rehab", "Retirement Homes", "Veterinarians", "Dentist"}},
        "Optometry":{"includeif":{"Optometrist"},"excludeif":{"Dermatologist"}},
        "Mental health":{"includeif":{"Psychiatrist","Psychologist"},"excludeif":set()},
        "Dental":{"includeif":{"Speech Therapy"},"excludeif":{"Speech"}},
        }
        setClinicalBussinessIds = set()
        fpointerInReview = open( paramFpathInBussiness, 'rt', encoding = 'utf8' )
        for aline in fpointerInReview:
            aline = aline.strip()
            jo = json.loads(aline)
            bussinessCategoryAttributes = jo['categories']
            setBussinessCategory = set(bussinessCategoryAttributes)
            for akey in dictClinicalBussinessCategories:
                includedifset = dictClinicalBussinessCategories[akey]['includeif']
                excludedifset = dictClinicalBussinessCategories[akey]['excludeif']
                if len(includedifset.intersection(setBussinessCategory) ) != 0:
                    if len(excludedifset.intersection(setBussinessCategory)) != 0 :
                        pass
                    else:
                        bussinessId = jo['business_id']
                        setClinicalBussinessIds.add( bussinessId )
                        break

        fpointerInReview.close()
        #print( setClinicalBussinessIds)

        fpointerInReview = open( paramFpathInReview, 'rt', encoding = 'utf8')
        fpointerOutReview = open( paramFpathOutReview, 'wt', encoding = 'utf8')
        fpointerOutStars = open(paramFpathOutStars,'wt', encoding = 'utf8')
        for aline in fpointerInReview:
            aline = aline.strip()
            jo = json.loads(aline)

            bussinessId = jo['business_id']
            if bussinessId in setClinicalBussinessIds:
                reviewText = jo[ 'text' ]
                reviewText = reviewText.replace('\r\n',' ')
                reviewText = reviewText.replace('\r',' ')
                reviewText = reviewText.replace('\n',' ') # actually in Unbuntu and Windows only this line went into effect
                reviewStar = jo[ 'stars' ]
                fpointerOutReview.write( reviewText + '\n' )
                fpointerOutStars.write( str(reviewStar) + '\n' )

            #print(reviewText)
            #break
        fpointerInReview.close()
        fpointerOutReview.close()
        fpointerOutStars.close()
