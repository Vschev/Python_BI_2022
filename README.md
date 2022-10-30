# Python_BI_2022
Bioinf assignments

The ultraviolence.py file for exploring virtual environments was tested on the Kubuntu system, v. 22.04.01 (LTS)

To run this wonder, you'll need to take the following steps:

1. Install Python 3.11 on your computer.

The module uses except* wrapping and other syntax that is not supported in earlier python versions. As such, you will need 3.11.
You'll also need instruments for creating virtual environments
Use the next commands:

```
sudo apt install python3.11
sudo apt install python3.11-venv
```

2. Create an activate an environment.
You'll need a special space to work with all the fantastic modules that are (not) required!
Just run this:

```
python3.11 -m venv [environment name]
source [environment name]/bin/activate
```

3. Import the modules.
For an easiest way to do it just run
```
pip install -r requirements.txt
```
For the manual installation start with several modules that are absolutely necessary:

```
pip install pandas
pip install biopython
pip install beautifulsoup4
pip install lxml
```
 
Are you ready for more?

    If please no:
       The other imported modules aren't actually used and you might want to remove them.
       One way to do that is to use PyCharm built-in "optimize import" instrument.
       Open ultraviolence.py in PyCharm and hover over the lamp on the first line. It will remove anything you don't need.
       From here, proceed to step 4.
       
    Elif yes, I'm interested:
       continue with installing:

```
pip install google-api-python-client
pip install aiohttp
pip install opencv-python
```
Instead of installing these, you could also create empty modules called "google.py", "aiohttp.py", "cv2.py", "requests.py"
Modern problems require modern solutions.

4. Edit the Pandas dataframe handler.
To deal with the strange mistake find the file:
[environment name]/lib/python3.11/site-packages/pandas/core/frame.py
In there, find the next few lines
```
        # GH47215
if index is not None and isinstance(index, set):
    raise ValueError("index cannot be a set")
if columns is not None and isinstance(columns, set):
    raise ValueError("columns cannot be a set")
```
Remove them, you actually need the sets here.
You might want to make a backup copy though.

5. Run Ultraviolence.py.
Congratulations! It works!
