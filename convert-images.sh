#!/bin/bash

# Check if ImageMagick is installed
if ! command -v convert &> /dev/null; then
    echo "ImageMagick is not installed. Please install it first."
    echo "For macOS: brew install imagemagick"
    echo "For Ubuntu: sudo apt-get install imagemagick"
    exit 1
fi

# Convert favicon.svg to favicon.ico
echo "Converting favicon.svg to favicon.ico..."
convert -background none favicon.svg -define icon:auto-resize=16,32,48,64,128 favicon.ico

# Convert og-image.svg to og-image.jpg
echo "Converting og-image.svg to og-image.jpg..."
convert -background none images/og-image.svg images/og-image.jpg

echo "Conversion complete!" 