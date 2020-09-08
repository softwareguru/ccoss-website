## Overview

This repo contains the code and data for the [CCOSS website](ccoss.org). 

## Structure / branching
* Main branch will be used to keep up-to-date with what is live at https://ccoss.org
* If you are not sure of what you are doing, you are welcome to create a branch and submit for review before being merged.
  
## Building the site
1. Install Hugo
2. Clone this repo and cd to it.
3. From the root, type `hugo server` and it will launch a web server with the website which you can check locally.
4. To build the site type `hugo`. This creates a `public` directory with the static html.  
5. Deploy the `public` directory to hosting. Note: In this case, this is not necessary since we are running from Netlify, which automatically builds the site whenever it detects a new commit/push to the main branch.

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
