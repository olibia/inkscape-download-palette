#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Inkscape extension to download color palettes from the web
"""

import os
import inkex
import simplestyle
import urllib

__version__ = '1.0'

inkex.localize()

class DownloadPalette(inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)

        self.OptionParser.add_option('-b', '--bright-shiny', action='store', type='string', dest='bright-shiny', help='Bright and Shiny')
        self.OptionParser.add_option('-f', '--flat-ui', action='store', type='string', dest='flat-ui', help='Flat UI Colors')
        self.OptionParser.add_option('-m', '--material-design', action='store', type='string', dest='material-design', help='Material Design')
        self.OptionParser.add_option('-p', '--pastel-manis', action='store', type='string', dest='pastel-manis', help='Pastel Manis')
        self.OptionParser.add_option('-r', '--round-tasmania', action='store', type='string', dest='round-tasmania', help='Round Tasmania')
        self.OptionParser.add_option('-n', '--name', action='store', type='string', dest='name', help='Custom Name')
        self.OptionParser.add_option('-u', '--url', action='store', type='string', dest='url', help='Custom URL')

    def palettes_path(self):
        path = "%s/.config/inkscape/palettes" % os.path.expanduser('~')

        if not os.path.exists(path):
            os.makedirs(path)

        return path

    def file_path(self, palette):
        name = palette.replace(' ', '-')
        path = self.palettes_path()
        path = "%s/DownloadPalette-%s.gpl" % (path, name)

        return path

    def palettes_urls(self):
        urls = {
            'material-design': 'https://github.com/KiSSFLOW/gimp-material-design-color-palette/raw/master/Material-Design.gpl',
            'flat-ui': 'https://github.com/dwipr/inkscape-palete-ku/raw/master/flatuicolors.gpl',
            'bright-shiny': 'https://github.com/bertob/brightandshiny/raw/master/brightandshiny.gpl',
            'round-tasmania': 'https://github.com/KathyReid/round-tasmania-palette/raw/master/round-tasmania.gpl',
            'pastel-manis': 'https://github.com/dwipr/inkscape-palete-ku/raw/master/pastelmanis.gpl'
        }

        if self.options.name is None and not self.options.url is None:
            inkex.errormsg(_('File name cannot be blank!'))

        if not self.options.name is None and self.options.url is None:
            inkex.errormsg(_('File URL cannot be blank!'))

        if not self.options.name is None and not self.options.url is None:
            file_type = self.options.url.split('.')[-1]

            if file_type == 'gpl':
                urls[self.options.name] = self.options.url
            else:
                inkex.errormsg(_('The URL is not a .gpl download URL. Please enter a valid URL.'))

        return urls

    def get_selected_palettes(self):
        options = self.options.__dict__
        palettes = dict(options)

        if 'selected_nodes' in palettes.keys():
            del palettes['selected_nodes']

        if 'ids' in palettes.keys():
            del palettes['ids']

        if palettes['name'] is None:
            del palettes['name']

        if palettes['url'] is None:
            del palettes['url']

        if 'name' in palettes.keys() and 'url' in palettes.keys():
            palettes[self.options.name] = palettes['url']
            del palettes['url']
            del palettes['name']

        for palette in options:
            if options.get(palette) == 'false' or options.get(palette) is None:
                if palette in palettes.keys():
                    del palettes[palette]

        return palettes.keys()

    def download_palettes(self):
        urls = self.palettes_urls()
        for palette in self.get_selected_palettes():
            url = urls.get(palette)

            if url is not None:
                try:
                    urllib.urlretrieve(url, self.file_path(palette))
                except:
                    inkex.errormsg(_("File %s.gpl could not be downloaded! Please try again." % palette))


    def effect(self):
        if len(self.get_selected_palettes()) == 0:
            inkex.errormsg(_('No palettes selected!'))
            exit()

        self.download_palettes()

if __name__ == '__main__':
    palette = DownloadPalette()
    palette.affect()
