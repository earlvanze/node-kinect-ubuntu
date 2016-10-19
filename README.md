# node-kinect

Kinect in Node.js, ported to run on Ubuntu ARM.

# Install on Ubuntu Touch

For installing on Ubuntu Touch, first enable developer tools and run the following:

```
$ phablet-config writable-image
```

Reboot, then follow the instructions below.

# Install on ARM

```sh
$ sudo apt-get update && sudo apt-get upgrade 
$ sudo apt-get install build-essential git-core cmake libusb-1.0-0-dev libfreenect-dev libxmu-dev libxi-dev freeglut3-dev usbutils libkrb5-dev nodejs-legacy
$ cd ~ && git clone git://github.com/OpenKinect/libfreenect.git && cd libfreenect && mkdir build && cd build && cmake .. && make && sudo make install && sudo ldconfig /usr/local/lib64/ && npm install serialport
$ chown -R $(whoami) ~/.npm && chown -R $(whoami) ~/node_modules
$ cd ~/node_modules && git clone https://github.com/farazfazli/node-kinect-ubuntu.git && cd node-kinect-ubuntu && npm install
```

# Test

Plug your kinect and do:

```sh
$ cd node-kinect
$ npm test
```

# Use

## Create a context

```js
var kinect = require('kinect');

var context = kinect();
```

Accepts options like this:

```js
var kinect = require('kinect');

var options = {
  device: 2
};

var context = kinect(options);
```


Options:

* device: integer for device number. Default is 0

## Resuming / pausing

Kinect is paused by default, to start pumping video or depth you need to resume it like this:

```js
context.resume();
```

You can also pause it like this:

```js
context.pause();
```

## LED

```js
var kinect = require('kinect');

var context = kinect();
context.led("red");
```

Accepts these strings as sole argument:

* "off"
* "green"
* "red"
* "yellow"
* "blink green"
* "blink red yellow"

## Video

Enable video:

```js
context.start('video');
```

Listen for video frames:

```js
context.on('video', function(buf) {
  // buf is RGB-encoded, 640 x 480
});
```

## Depth

Enable depth:

```js
context.start('depth');
```

Listen for depth frames:

```js
context.on('video', function(buf) {
  // each depth pixel in buf has 2 bytes, 640 x 480, 11 bit resolution
});
```

## Tilt

Set tilt angle:

```js
context.tilt(angle);
```

`angle` can be any number from -15 to 15. Number out of the range will be set to min/max.

# FAQ

## Can you control more than 1 kinect device at the same time?

Yes, create different contexts with a different `device` option each.

# License

(The MIT License)

Copyright (c) 2011 Pedro Teixeira. http://about.me/pedroteixeira

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
