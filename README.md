# DSCI560_HW5

## create the virtual environment
```
pip install virtualenv
```
```
python -m venv dsci560hw5
```
```
source dsci560hw5/bin/activate
```
![image](https://github.com/Mogu615/DSCI560_HW5/blob/main/picture1.png)

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
![image](https://github.com/Mogu615/DSCI560_HW5/blob/main/picture2.png)

## run the script
```
pip install -r requirements.txt
```
```
Bokeh serve --show resulting.py
```
![image](https://github.com/Mogu615/DSCI560_HW5/blob/main/picture3.png)

## build container
- Download the Docker in your computer
- Clone the repository content
```
git clone https://github.com/Mogu615/DSCI560_HW5.git
```
```
cd DSCI560_HW5
```
- Build the image called image_covid19
```
docker build --tag image_covid19 .
```
- Run the image
```
docker run -p 5006:5006 -it image_covid19
```
- open browser and go to the link below:
```
http://localhost:5006/resulting
```
![image](https://github.com/Mogu615/DSCI560_HW5/blob/main/picture4.png)
![image](https://github.com/Mogu615/DSCI560_HW5/blob/main/image1.png)
![image](https://github.com/Mogu615/DSCI560_HW5/blob/main/image2.png)
![image](https://github.com/Mogu615/DSCI560_HW5/blob/main/image3.png)
