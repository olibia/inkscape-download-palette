# Inkscape Download Palette

Inkscape extension to download color palettes from the web.

![Screenshot](https://raw.githubusercontent.com/olibia/inkscape-download-palette/master/screenshot.png)

## Install
Copy extension files `download_palette.inx` and `download_palette.py` into `~/.config/inkscape/extensions`.
Inkscape needs to be restarted for the extension to appear.
`python2-lxml` must be installed for this extension to work.

### Inkscape Extensions
Download from Inkscape's Extensions page [here](https://inkscape.org/en/~olibia/%E2%98%85download-palette-extension).

### Arch Linux
[AUR package](https://aur.archlinux.org/packages/inkscape-download-palette)

## Usage
* From the Extensions menu choose Palette and Download.
* Select one or more palettes to download from the predefined collection.
* Provide a name and a `.gpl` file URL to download a palette from the web.

### Notes
Inkscape must be restarted for palettes to appear.
Downloaded palettes are stored in `~/.config/inkscape/palettes`.
Tested only on Inkscape for Linux.

## License
[GPLv3](http://www.gnu.org/licenses/gpl-3.0.en.html)
