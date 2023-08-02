# Merge two different table's extracted data from the output csv file

Suppose the document is complex and we have to split a single line item from the table into 2 different tables so that the extraction happens properly,
we can use this code to merge them back after the extraction

This repo shows how to merge the table data

# Pre-requisites to run the bot
* This bot contains python scripts, so python should installed in the runner machine
* Please refer to the document below
* https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/aae-client/bot-creator/commands/cloud-python-command.html
* Install the following python libraries
* * pip install pandas

## The following is an image of how the table will look like before extraction

inOutput.png

## Input Parameters:
The bot expects 1 input parameters as shown below
CR_exec_3.png

#### Step 1:
* Clone this repo and store the "FillInMissingValues.py" file in your local machine

#### Step 2:
* You can use this file as script in your python command.
CR_exec_1.png

#### Step 3:
* The function name from this script will be used as param for the function to be executed
CR_exec_2.png


## The following is an image of how the table will look like after the bot is executed

finalOutput.png


 


