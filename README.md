## How to run

### Option 1 - command line
Input file must be csv and formatted like this:
```
cash,price,wrappers_needed,type
12,2,5,milk
12,4,4,dark
6,2,2,sugar_free
6,2,2,white
```
Run Command:
```
$ python path_to/ramsey_challenge/__main__.py path_to/input.csv path_to/new_output.txt
```
If absolute path is not provided for input/output, relative path will be used.

### Option 2 - python file
Create a file in the ramsey_challenge folder and add code like this:
```python
from main import ChocolateFeast

# scenario 1
cf = ChocolateFeast()
cf.cash = 12
cf.price = 2
cf.wrappers_needed = 5
cf.chocolate_type = "milk"

cf.main()

assert cf.milk == 7
assert cf.dark == 0
assert cf.white == 0
assert cf.sugar_free == 1
```

## Unit Tests
1. You will need to install pytest via pip if not already installed
2. Navigate to the ramsey_challenge folder
3. run this command
```
$ python -m pytest
```
