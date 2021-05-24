#!/usr/bin/env bash

mkdir $1.iconset
convert $1.png -resize 16x16 $1.iconset/icon_16x16.png
#convert $1.png -resize 32x32 $1.iconset/icon_16x16@2x.png
convert $1.png -resize 32x32 $1.iconset/icon_32x32.png
#convert $1.png -resize 64x64 $1.iconset/icon_32x32@2x.png
convert $1.png -resize 128x128 $1.iconset/icon_128x128.png
#convert $1.png -resize 256x256 $1.iconset/icon_128x128@2x.png
convert $1.png -resize 256x256 $1.iconset/icon_256x256.png
#convert $1.png -resize 512x512 $1.iconset/icon_256x256@2x.png
convert $1.png -resize 512x512 $1.iconset/icon_512x512.png
cp $1.png $1.iconset/icon_1024x1024.png
png2icns $1.icns $1.iconset/icon_*.png

rm -R $1.iconset 
