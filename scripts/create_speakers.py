# Script to create the session content files for Hugo from a csv file.

import csv
import os

with open('speakers.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        title = row['title']
        slug = row['slug']
        designation = row['designation']
        linkedin = row['linkedin']
        twitter = row['twitter']
        github = row['github']
        events = row['events'].split(", ")
        bio = row['bio']
        country = row['country']

        dirname = "speakers/"+slug
        try:
            os.mkdir(dirname)
        except FileExistsError:
            print("Dir "+dirname+" exists")
        except OSError:
            print ("Creation of the directory "+dirname+" failed" )
        else:
            print ("Successfully created the directory "+dirname)

        filename = dirname+"/_index.md"

        with open(filename, "w") as f:

            f.write("---\n")
            f.write(f"title: \"{title}\"\n")
            f.write(f"designation: \"{designation}\"\n")

            f.write(f"images:\n - images/speakers/{slug}.jpg\n")

            f.write("events:\n")
            for s in events:
                f.write(" - "+s+"\n")
            f.write(f"linkedin: {linkedin}\n")
            f.write(f"twitter: {twitter}\n")
            f.write(f"github: {github}\n")

            f.write("---\n\n")
            f.write(bio)


