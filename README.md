# OpenCV-Webcam-Stream
This project contains a basic python script to run opencv-python with a webcam stream.

## Previews
![Preview1](./preview/preview1.PNG?raw=true "Preview1")

## How it work's
Haar-Features are good at detecting edges and lines, this makes it effective in face detection techniques. Also, Haar-based classifiers typically involve less computations so it has a higher execution speed.

Here are some Haar-Features types:

![haar_features_types](./documentation/haar_features_types.jpg?raw=true"haar_features_types")

Basic line features looks like this:

![haar_features](./documentation/haar_features.png?raw=true"haar_features")

Numericaly, it looks like this:

![numerical_haar_features](./documentation/numerical_haar_features.png?raw=true"numerical_haar_features")

Haar-feature would be able to detect eyes on a face because the eyes are an area that is dark on top and brighter underneath):

![haar](./documentation/haar.png?raw=true"haar")

## How to setup
- Install opencv-python
```
$ pip install opencv-python
```

- Install tkinter
```
$ pip install tkinter
```

- Install pillow
```
$ pip install pillow
```

## How to test
- Run
```
$ python ./tests.py
```

## How to run
- Run
```
$ python ./app.py
```

## Links
- [Python Patterns - Github](https://github.com/faif/python-patterns)
- [Python Design Patterns: For Sleek And Fashionable Code](https://www.toptal.com/python/python-design-patterns)
- [Python Tkinter](https://www.javatpoint.com/python-tkinter)
