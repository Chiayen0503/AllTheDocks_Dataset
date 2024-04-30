# AllTheDocks_Dataset
This is repository for our work "AllTheDocks road safety dataset: A cyclist’s perspective and experience". The dataset will be available before IEEE VTC 2024 (24~27th June).

### To download numerical data listed below, go to ```data/raw/```
* Acceleration
* GPS (location, height, speed)
* Gyroscope

### To download preprocessed, merged data (include above types and IRI), go to ```data/interpolation/```
### To download GoPro videos and images, visit links: 
* (1) Videos (```MP4```): 
* (2) Images (```jpg```): 
### To reproduce numerical data extracted from GoPro images and videos, follow instructions below:
* (1) Step 1: clone and setup https://github.com/JuanIrache/gopro-utils/tree/master
* (2) Step 2: open the terminal and type ```cd /to/your/gopro_videos_folder/```
* (3) Step 3: create ```.bin``` files by typing ```for i in *.MP4; do ffmpeg -y -i $i -codec copy -map 0:3 -f rawvideo ${i%.MP4}.bin; done;``` (Note: these ```.bin``` files contains all numerical information, now we just need to decode them and save them to ```.csv``` )
* (4) Step 4: open the other terminal and go to folder ```cd JuanIrache/gopro-utils/bin/gpmd2csv/``` 
* (5) Step 5: move ```.bin``` files from (3) to ```.../gpmd2csv/``` 
* (6) Step 6: type ```for i in *.bin; do ../gpmd2csv -i $i; done;``` (Now we have all ```.csv``` files in three folders like the ones in ```data/raw/```) 
