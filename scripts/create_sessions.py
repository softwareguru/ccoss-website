# Script to create the session content files for Hugo from a csv file.

import csv
with open('sessions.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        slot = row['id'].lower()
        title = row['title']
        slug = row['slug']
        speakers = row['speakers'].split(", ")
        time_start = row['time_start']
        time_end = row['time_end']
        session_type = row['type']
        abstract = row['content']
        event_slug = row['event-slug']

        filename =  "sessions/"+event_slug+"/"+slot+"-"+slug+".md"
        with open(filename, "w") as f:
            f.write("---\n")
            f.write(f"id: {slot}\n")
            f.write(f"title: \"{title}\"\n")
            f.write(f"url: sessions/{event_slug}/{slug}.md\n")
            f.write("speakers:\n")
            for s in speakers:
                f.write(f" - {s}\n")
            f.write(f"time_start: {time_start}\n")
            f.write(f"time_end: {time_end}\n")
            f.write(f"format: {session_type}\n")
            f.write(f"block: {slot[0:1]}\n")
            f.write(f"slot: {slot[1:3]}\n")
            f.write("---\n\n")
            f.write(abstract)

