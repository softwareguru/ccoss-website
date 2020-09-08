## Overview

This repo contains the code and data for the [CCOSS website](ccoss.org). 

## Structure
* There are branches for each summit edition. They can be old events which are kept here for archiving or current/upcoming
events where the branch is used for development. Each branch will be used to setup independant auto-build processes.  
* Master branch will be used to keep up-to-date with what is live on beamsummit.org

Previous editions of beam summit websites were built with [Project Hoverboard](https://github.com/gdg-x/hoverboard) but for the 2020 edition we are using [Hugo](https://gohugo.io) with a custom theme.

## Building the site
1. Install Hugo
2. Clone this repo and cd to it.
4. Build the site with `hugo`. You can optionally add `--gc --minify` for clean and minimized output. This creates a `public` directory with the static html.
5. Deploy the `public` directory to hosting.

## Adding/editing content

### Homepage
* For layout, modify `/themes/ccoss/layouts/index.html`
* For messages/content, modify `/data/homepage.yml`

### Speakers
* To add a speaker create a markdown file under `/content/speakers/` (see the folder for sample files). The file name format should be `firstname-lastname.md` (this allows Hugo to automatically find the speaker and hyperlink to them from the session page). 
* For the headshot, crop an image to 1:1 (ideally 400x400 px) and put it under `/static/images/speakers/`. Eventually we may add libs to do autocrop/resize but in the meantime do it manually. 
* If your markdown file is not being generated/published check that you don't have `draft:true` in the meta section.
* Note: We may later set up [Netlify CMS](https://www.netlifycms.org/) to edit speaker markdown files through a GUI without having to go through the steps described here.

### Sessions
* Similar to speakers, create a markdown file under `/content/sessions/`. 
* If start and end time are set on the meta we can generate links to add to google calendar. 
* If you set the speaker name(s), a hyperlink to the corresponding speaker page will be generated (if a file with the speaker name is found under the speakers folder).
* If you have multiple speakers, put them as a list in the meta.

### Sponsors
Sponsors info is currently kept under `/data/sponsors.yml`. Add the image file to `/static/images/logos/`

### Schedule
The repo currently has layout files which we used at other event. They are here for reference and will be updated once the best layout is defined based on the structure of the final agenda.

### Updating the live website
The live website is currently hosted on Netlify and is updated automatically from commits to the main branch of this repo. So, when you commit and push, a task will be automatically triggered.

-----

The project is published under the [MIT license](/LICENSE.md).
Feel free to clone and modify repo as you want, but don't forget to add a reference to authors :)

_GDG[x] is not endorsed and/or supported by Google, the corporation._
