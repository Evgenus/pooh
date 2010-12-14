# my library to operate paths inside disk space and site url in uniform way
from utils.path import Path

# third party html template engine
from mako.lookup import TemplateLookup

# root of everything we need
root = Path.from_file(__file__).up()

# here we'll search our source files with templates and pages markup data
templ_dir = root / 'source'

# directory for temporary files created by mako template engine
cache_dir = root / 'cache'

# directory where out generated site pages will be placed by this script
output_dir = root / 'output'

# mako shit for template rendering
lookup = TemplateLookup(
    directories=[templ_dir.str()],
    module_directory=cache_dir.str(),
    input_encoding='utf-8',
    output_encoding='utf-8',
    )

def factory(filename):
    return lookup.get_template(filename)

# function used inside teplates to tell them where is root of their subsite
# in out case this subside is /pooh
# so subsite can imagine that it is a root of whole site
def PATH(*p):
    return site_root(*p).str()

# distionary of site parts to be generated
data = {
    Path(['pooh']) : [
        Path(['pooh/2010']),
        Path(['pooh/2011']),
        Path(['pooh/2011/poll']),
        Path(['pooh/css']),
        ]
    }

for site_root, parts in data.iteritems():           # for each subsite
    for part in parts:                              # and each its part
        for filename in templ_dir[part].listdir():  # find all source files
            # we generates only html and css files
            if filename.split('.')[-1] not in ('html', 'css'):
                continue
            print output_dir[part][filename] # just to know what is going on
            # renders page content in string representation
            page = factory(part[filename].str()).render(
                PATH=PATH,
                )
            # write it to output file
            with output_dir[part][filename].open('w') as stream:
                stream.write(page)
