# Recess for Sublime Text 3

## Description
Adds a build setting to use [Twitter Recess](https://github.com/twitter/recess "Twitter Recess") to compile, clean up, and compress your CSS.

## Installation
### Prerequisites
1. Install [node.js](http://www.nodejs.org) and npm.
2. Run the command `npm install recess -g` to install recess globally.

### Install using Git:
Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/morganestes/sublime-recess.git "Twitter Recess"

The "Packages" directory is located at:

* OS X: `~/Library/Application Support/Sublime Text 3/Packages/`
* Linux: `~/.Sublime Text 3/Packages/`
* Windows: `%APPDATA%/Sublime Text 3/Packages/`

### Manual installation:
* Download the [latest source zipball](https://github.com/morganestes/sublime-recess/zipball/master) and extract the files to your Sublime Text "Packages" directory, into a new directory named `Twitter Recess`.

## Usage
### Configure
Open `Recess.sublime-build` and change the options to fit your needs. I recommend leaving in `--stripColors true` since it displays in the ST3 console window weird without it.

### Run

1. Right-click in the window and select the options from the Recess menu.
2. `Ctrl+Shift+R` on your keyboard for linting, `Ctrl+Shift+Alt+R` for compiling.
3. Use `Ctrl+Shift+P` to open the Command Pallete. Type "Recess" to get the commands to choose from.

## Known Issues
See https://github.com/morganestes/sublime-recess/wiki/Known-Issues for the latest info on known/reported
issues for ST2 & ST3.

## Changelog
### 0.3.0
- Added ST3 support

### 0.2.2
- Added OS X path

### 0.2.1
- Added Linux path

### 0.2.0
- Added `--compile` and changed the menu to handle multiple options.

### 0.1.0
- Initial release

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/morganestes/sublime-recess/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

