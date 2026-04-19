# The Open PS2 Loader CFG Database Project for PS1

## Goal
This is a collection of CFG files for use with [Open PS2 Loader](https://github.com/ifcaro/open-ps2-loader). 

A fork of [Tom-Bruise's CFG database](https://github.com/Tom-Bruise/PS2-OPL-CFG-Database) for PS2 games, this aims to fulfill the same goal, except for PS1 games. 

## These CFG files are unfortunately ONLY readable by the 10th Anniversary Edition of OPL 1.1 which had native PS1 Game support integrated. Newer versions based on OPL 1.2 use Apps to launch PS1 games and thus DO NOT SUPPORT the display of CFG file data.

I hope that one day Apps can integrate support for this rich information, either in OPL Core or as part of tools like OPL Manager. Until then, this database works with 1.1 10th Anniversary Edition and is a starting point for enriched game information on OPL for PS1. 

Lacking a starting point with baseline CFG files such as Veritas83's that Tom-Bruise used, I instead queried Redump to get a list of all PS1 serials and game titles in a DATFILE, which were then further enriched using scraped data from ScreenScraper.fr. You can find the Python scripts used to create that Redump based xml file in the scripts folder. The additional scraped fields are:

* Game Description
* Number Of Players
* Genre
* Release Date
* Developer
* Rating

Here are some stats:

```
Total CFG files          =  5176
CFGs with Descriptions   =  4716
CFGs with Players info   =  4727
CFGs with Genre info     =  4672
CFGs with Release date   =  4730
CFGs with Developer info =  4672
CFGs with Ratings        =  4572
```

This collection of CFG files can be easily imported in [OPL Manager](https://oplmanager.com/site/), so every time you add a new game there is a good chance you have information already available for it.

## Notes About Game Descriptions

The maximum length allowed for game descriptions in OPL Manager is 255 characters. Descriptions on [ScreenScraper.fr](https://www.screenscraper.fr) are longer than that, so they have been shortened in the following way:

* The text was truncated to 255 characters.
* Since the truncated text might have hanging phrases, the resulting text is further trimmed to the last period.

Of course this algorithm is very basic and naive, and will result in some errors in the descriptions. If you find some, check the Contributing section to help fixing them.

## Using The Database in OPL Manager

**IMPORTANT: Before trying anything, make a backup copy of your existing CFG files!**

* Open OPL Manager.
* From the menu, choose _Open OPL Folder_.
* Copy the files in the CFG folder of this repository to the CFG folder of OPL.

**Note**: wLaunchElf has issues copying a large number of files (see this [issue](https://github.com/Tom-Bruise/PS2-OPL-CFG-Database/issues/5)).
To work around this, you might try using the *export_cfg_from_csv.sh* script in the *Scripts* folder.

## Contributing

Just create a pull request.

* Be considerate about the size of the pull request. If you create one that involves thousands of games, there is no way I will be able to review it. Keep them small.
* For descriptions:
    * Length limit is 255 characters. 
    * If you are providing a new description, spell-check your English. No personal opinions about the video game. Keep it informative. No profanity, irrelevant stuff etc. Just have good taste.

A word of warning: this was nothing more than a weekend project, and the time I have to dedicate to it is very, very limited. It might take time to review requests and make changes. 

## License

Following Veritas83's original repository, this is released under the GNU General Public License v3.0.
