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

<img width="923" alt="inOutput" src="https://github.com/hasnainsyed73/IQBot/assets/129178965/a89f3a55-581b-4067-8548-3ba7008c22c9">


## Input Parameters:
The bot expects 1 input parameters as shown below
<img width="751" alt="CR_exec_3" src="https://github.com/hasnainsyed73/IQBot/assets/129178965/e99d3684-ac58-4000-af49-cdc16f347746">


#### Step 1:
* Clone this repo and store the "FillInMissingValues.py" file in your local machine

#### Step 2:
* You can use this file as script in your python command.
<img width="715" alt="CR_exec_1" src="https://github.com/hasnainsyed73/IQBot/assets/129178965/e1a63832-8cc6-46b3-991b-34c6b61b2e70">

#### Step 3:
* The function name from this script will be used as param for the function to be executed
<img width="674" alt="CR_exec_2" src="https://github.com/hasnainsyed73/IQBot/assets/129178965/ed004d39-cd2c-479e-9347-01769762ecf7">

## The following is an image of how the table will look like after the bot is executed

<img width="853" alt="finalOutput" src="https://github.com/hasnainsyed73/IQBot/assets/129178965/4114609b-4c3b-4a5f-ab56-2d1a4ef447b4">



 


