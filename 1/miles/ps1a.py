#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:50:11 2017

@author: mtaylor
"""
import os
os.getcwd()
os.chdir('/Users/mtaylor/Desktop/Helpful_Programming_Misc/ContinuedEducation/MIT_DataScience')
import time
from ps1_partition import get_partitions



#================================
# Part A: Transporting Space Cows
#================================


class cows(object):
    def __init__(self,n,w):
        self.name = n
        self.weight = w
    
    def GetWeight(self):
        return self.weight
    
    def __str__(self):
        return self.name + ' : ' + str(self.weight)
    
    def __iter__(self):
        yield self.name,self.weight


    
    # Problem 1
def load_cows():
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return 
    dictionary containing cow names as keys and corresponding weights as values.
    
    Parameters:
        filename - the name of the data file as a string
    Returns:
        a dictionary of cow name (string), weight (int) pairs"""
    # TODO: Your code here
   working_cow_file = {}
   with open('ps1_cow_data_txt') as f:
       for line in f:
           (key,val) = line.split(',')
           d[str(key)] = val
   cow_file = open('ps1_cow_data.txt','r')
    cow_file.close
    cow_file_list = list(cow_file)
    #preprocess_cows = cows(cow_file_list[0],cow_file_list[1])
    working_cow_file = {}
    for i in (cow_file_list):
        working_cow_file.update([cows([i],[i])])
    return working_cow_file

    # Problem 2
    def greedy_cow_transport(cows,limit=10):
        """
        Uses a greedy heuristic to determine an allocation of cows that attempts to
        minimize the number of spaceship trips needed to transport all the cows. The
        returned allocation of cows may or may not be optimal.
        The greedy heuristic should follow the following method:
            
            1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
        2. Once the trip is full, begin a new trip to transport the remaining cows
        
        Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    
    """
    # TODO: Your code here
    working_cow_file_sorted = sorted(working_cow_file,
                                     key = lambda k: working_cow_file[k],
                                     reverse = True)
    Cow_Names= []
    Total_Transit =[]
    TotalWeight = 0.0
    TotalTrips = 0
    AllCowsGoToAuck = 0
    while AllCowsGoToAuck < len(working_cow_file_sorted):
        for i in range(len(working_cow_file_sorted)):
            if (TotalWeight + working_cow_file_sorted[i].GetWeight()) <= limit:
                Cow_Names.append(working_cow_file_sorted[i])
                TotalWeight += working_cow_file_sorted[i].GetWeight()
                AllCowsGoToAuck += len(Cow_Names)
            
            elif (TotalWeight + working_cow_file_sorted[i].GetWeight()) >= limit:
                TotalTrips += 1
                Total_Transit.append(Cow_Names.TotalTrips)
                del Cow_Names
            
            
    return Total_Transit        
            

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    brute_force_DataSet = get_partitions(cow_file_list)
    
    
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
