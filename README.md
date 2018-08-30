# Data Folder
We are using Yelp review dataset for this work which can be
downloaded from the Yelp website (Yelp dataset is not included in the folder).
Data folder consists of two programs that is explained below:

__YelpData
folder:__ In YelpData folder run the main.py to make use of “bussiness.json” and
“review.json” files(included in the Yelp dataset) to extract only reviews
relating to the health-care. By running this you would get each review with
unique ID as a sentence in a .txt file. 

__DataClean.py:__ use this code to
delete impractical reviews from extracted review documents. This will include
any non-English, empty and short documents. Run "python DataClean.py -h" in
terminal to get information about the input arguments for the program.
