# Recess for Sublime Text 2 #

**Updated 5/22/12**:

- Added `--compile` and changed the menu to handle multiple options.
- Only have Windows commands; I’m looking for help with Linux and OSX.

## Tools Used ##
- [node.js](http://nodejs.org "node.js") with [npm](http://npmjs.org/)
- [Twitter Recess](https://github.com/twitter/recess "Twitter Recess")
- [Sublime Text 2](http://www.sublimetext.com/2 "Sublime Text 2")

## Background ##
I wanted to use the new tool from @fat to clean up my CSS inside [Sublime Text 2](http://www.sublimetext.com/2 "Sublime Text 2"), which I've just started using. This is my first shot at creating a plugin for ST2, so I built off of JSHint and just made changes to enable Recess to run.

### Problems I know about and need help with ###
- I'm using Windows 7 x64 as my development machine, so all my code in the plugin is geared for that platform. I could use help expanding it to Mac and Linux.
- I'm new to [node.js](http://nodejs.org/) and some of this may be related to my very limited understanding of how it works.
- Options can be added to the `cmd` line, but I can't get the config file to work. I've tried different settings and commands, but get a run of errors that I don't yet understand.
- <del>I can either compile or get error reports, but not both.</del> See [Issue #2](https://github.com/morganestes/sublime-recess/issues/2) for an update.
- <del>I need to learn how to have multiple commands, so I can either lint or compile right from a command window or keyboard.</del> See [Issue #2](https://github.com/morganestes/sublime-recess/issues/2) for an update.

### Requirements ###
This plugin acts as an interface for Twitter Recess, which much first be installed on your computer using node.js and npm. It has been tested with Sublime Text 2 Beta Build 2181 and Recess 1.0.4.

### Installation ###
Before using the plugin, you must first install recess on node.js.

1. Install [node.js](http://www.nodejs.org) and npm.
2. Run the command `npm install recess -g` to install recess globally.

Note: I borrowed these instructions from [LESS-sublime](https://github.com/danro/LESS-sublime/blob/master/readme.md "LESS-sublime readme").

**Without Git:**
* **Best Method**: Install using [Package Control](http://wbond.net/sublime_packages/package_control).
* Download the latest source zip from [github](https://github.com/morganestes/sublime-recess/zipball/master) and extract the files to your Sublime Text "Packages" directory, into a new directory named `Twitter Recess`.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/morganestes/sublime-recess.git "Twitter Recess"

The "Packages" directory is located at:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux:
    `~/.Sublime Text 2/Packages/`
* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`

### Usage ###
**Configure:** Open Recess.sublime-build and change the options to fit your needs. I recommend leaving in `--stripColors true` since it displays in the ST2 console window weird without it.

There are three ways to run it:

1. Right-click in the window and select the options from the Recess menu.
2. `Ctrl+Shift+R` on your keyboard for linting, `Ctrl+Shift+Alt+R` for compiling.
3. Use `Ctrl+Shift+P` to open the Command Pallete. Type "Recess" to get the commands to choose from.




[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/morganestes/sublime-recess/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

