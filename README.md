# DSCI560_HW5

## create the virtual environment
```
pip install virtualenv
```
```
python -m venv dsci560H4
```
```
source dsci560hw5/bin/activate
```

## install the dependencies 
```
pip install pandas
```
```
pip install bokeh
```
```
pip freeze > requirements.txt
```

## run the script
```
pip install -r requirements.txt
```
```
Bokeh serve --show resulting.py
```

## build container
- Download the Docker in your computer
- Clone the repository content
```
git clone https://github.com/Mogu615/DSCI560_HW5.git
```
```
cd DSCI560_HW5
```
- Build the image called dsci560hw5
```
docker build --tag image560 .
```
- Run the image
```
docker run -p 5006:5006 -it dsci560hw5
```
- open browser and go to the link below:
```
http://localhost:5006/resulting
```
