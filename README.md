# cr-tilemap
Modified and better documented version of https://github.com/smlbiobot/cr-tilemap
This program visualizes tilemap files from Clash Royale.

# Usage
First off you will need to be able to decompile .csv files. I nowadays use https://github.com/proydakov/supercell_resource_decoder, before this one I used this tutorial on YouTube to achieve my results. https://www.youtube.com/watch?v=e5TMqYpI1Y0
Corrections, some things are wrong:
1. The script is stored on https://github.com/jeanbmar/sc-compression/blob/master/examples/decompress.mjs
2. You need to manually change the download link from node.js to be V12.18.2, like this https://nodejs.org/dist/v12.18.2/node-v12.18.2-x64.msi, for future proofing I uploaded the .msi file for 64x Windows systems to archive.org. https://archive.org/details/node-v12.18.2-x64
3. Just so you know you won't need the .sc viewer, if you still want to view those files I recommend https://github.com/abdullahbaa5/SCEditor/releases/tag/publish, keep in mind that it's a little bit outdated.
4. Don't forget to run ```npm install sc-compression```

When you got all of that up and running you will need to extract the tilemap files from the game. These are stored in assets\tilemaps. From here it's very simple.
1. Decode these files using your .csv decoder of choice.
2. Put your decoded .csv file(s) into lib\cr-csv\assets\tilemaps
3. Run run.py
4. The pdf file(s) will automatically open, if it's blank then it's likely the .csv file wasn't decompiled correctly.
5. The outputted pdf file(s) can be found in dst
