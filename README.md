# Bixn Calculator

The "Bixn Calculator" is a fast and easy solution to rank the people in your life based on 3 aspects:

- How attractive they are(hot)...h
- How unpredictable  (crazy)...c
- How pleasant they are (nice)...n

Each aspect can be viewed separately but also an overall rating from 1-10 is calculated.
The formula to calculate the score looks like this:

$$score=h+n-|n-4|$$

Then the score gets mapped from 1-10:

$$score=1+9*\frac{score+4}{24}$$

## Running the application
Create and activate the virtual environment and install the required packages
```
py -m venv .\backend\venv
.\backend\venv\Scripts\activate
pip install .\backend
```
Then run the run.sh file:
```
.\run.sh
```
