# Recess for Sublime Text 2 #

## Tools Used ##
- [https://github.com/twitter/recess](https://github.com/twitter/recess "Twitter Recess")
- [https://github.com/uipoet/sublime-jshint](https://github.com/uipoet/sublime-jshint "JSHint for Sublime")
- [http://www.sublimetext.com/2](http://www.sublimetext.com/2 "Sublime Text 2")

## Background ##
I wanted to use the new tool from @fat to clean up my CSS inside [Sublime Text 2](http://www.sublimetext.com/2 "Sublime Text 2"), which I've just started using. This is my first shot at creating a plugin for ST2, so I built off of JSHint and just made changes to enable Recess to run.

### Problems I know about and need help with ###
- I'm using Windows 7 x64 as my development machine, so all my code in the plugin is geared for that platform. I could use help expanding it to Mac and Linux.
- I'm new to [node.js](http://nodejs.org/) and some of this may be related to my very limited understanding of how it works.
- Options can be added to the `cmd` line, but I can't get the config file to work. I've tried different settings and commands, but get a run of errors that I don't yet understand.
- I can either compile or get error reports, but not both.
- I need to learn how to have multiple commands, so I can either lint or compile right from a command window or keyboard.

### Installation ###
Note: I borrowed these instructions from [LESS-sublime](https://github.com/danro/LESS-sublime/blob/master/readme.md "LESS-sublime readme").

**Without Git:** Download the latest source zip from [github](https://github.com/morganestes/sublime-recess/zipball/master) and extract the files to your Sublime Text "Packages" directory, into a new directory named `Recess`.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/morganestes/sublime-recess.git Recess

The "Packages" directory is located at:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux:
    `~/.Sublime Text 2/Packages/`
* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`

### Usage ###
**Configure:** Open Recess.sublime-build and change the options to fit your needs. I recommend leaving in `--stripColors true` since it displays in the ST2 pane weird without it.

There are three ways to run it:

1. Right-click in the window and select RECESS.
2. Ctrl+Shift+R on your keyboard.
3. Use Ctrl+Shif+P to open the Command Pallete. Type "Recess" to get the command "Recess: Check for problems."


