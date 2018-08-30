# -*- coding: utf8 -*-

import yelpPreprocessor

if __name__ == '__main__':

    oYelpPreprocessor = yelpPreprocessor.YelpPreprocessor()
    oYelpPreprocessor.yelpPreprocess(
        'Datasets/YelpReview/business.json',
        'Datasets/YelpReview/review.json',
        'Outputs/clinical_reviews_texted.txt',
        'Outputs/clinical_reviews_stars.txt')
    