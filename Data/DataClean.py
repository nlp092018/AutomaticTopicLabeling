# coding: utf-8

# # 1. Import Packages

# Need to install these packages in terminal in your environment

# In[ ]:


# from pathlib import Path
import os,sys
from pathlib import Path
curr_dir = os.getcwd() + '/'


# In[ ]:


from argparse import ArgumentParser
parser = ArgumentParser(
    description="'''This script removes all non-English and shorter than 200 charatcter long sentences from the corpus'''")
parser.add_argument('--input_dir', metavar='path_to_input_file/', help='path to the input directory', default=curr_dir+'YelpData/Outputs/')
parser.add_argument('input_file', metavar='input.txt', help='name of the source file' , default='clinical_reviews_texted.txt')
parser.add_argument('output_name', metavar='output.txt', help='name of the ouptput file')
parser.add_argument('--output_dir', metavar='output/', help='path to the output directory', default=curr_dir)
args = parser.parse_args()
args = parser.parse_args()


# In[ ]:


filename = args.input_dir + args.input_file  #Path to .txt data file one document per sentence
if not os.path.isfile(filename):
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")
#Read input .txt data and load to an array
with open(filename, 'r', encoding="utf-8") as f:
    data = f.read().splitlines()

num_doc = len(data)
print('Total number of documents: ' + str(num_doc))


#function to save list of data into text file with new line 
def savetofile (fpath,data):
    with open(fpath,"wt") as f:
        for sent in data:
            f.write(sent + '\n') 



# # Deleting non-English sentences 
# We can use polyglot or langdetect package. polyglot is faster and can be used for name-entity detection as well. 


## detecting non-english sentences
from polyglot.detect import Detector
non_english = {}

for i,sent in enumerate(data):
    detector = Detector(sent,quiet=True)
    if detector.language.code != 'en':
        non_english[i] = sent
print('number of non-english documents deleted: {}'.format(len(non_english)))

## keep only english sentences

for index in sorted(non_english, reverse=True):     #Delete detected non_english sentences
    del data[index]
    
# #Save non-english sentences to a file   
# with open(args.output_dir + clinical_reviews_texted.txt ,"wt") as f:
#     for sent in data:
#         f.write(sent + '\n')

##### This is another package langdetect but it is slower !!!

# from langdetect import detect

# non_english = []

# for i,sent in enumerate(data):
#     detector = detect(sent)
#     if detector != 'en':
#         non_english.append(sent)
#         print(i,sent)
        
# print(len(non_english))


## Delete any sentences less than N character
N = 200
for n in data[:]:
    if len(n) < N:
        data.remove(n)
        
savetofile(args.output_dir + args.output_name ,data)  
print('number of documents shorter than {} characters deleted: {}'.format(int(num_doc-len(data)),N))
print('total number of documents remained: {}'.format(len(data)))
