#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: This function creates the pet labels based on the image filenames
#          and returns a dictionary with filenames as keys and pet labels
#          as values.
##

# Imports python modules
from os import listdir

# Function to create pet labels from filenames
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
   
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
       
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
       if in_files[idx][0] != ".":
           
           # Creates temporary label variable to hold pet label name extracted 
           pet_label = ""

           # Processes each filename to extract pet label (dog breed)
           # Assumes the filename format is like: "dog_breed_001.jpg"
           words = in_files[idx].lower().split('_')
           pet_label = " ".join(words[:-1])  # Extracts words except for the last part (number/extension)

           # If filename doesn't already exist in dictionary add it and its pet label
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
           else:
               print("** Warning: Duplicate files exist in directory:", in_files[idx])
 
    # Return the results dictionary containing filenames and their pet labels
    return results_dic

