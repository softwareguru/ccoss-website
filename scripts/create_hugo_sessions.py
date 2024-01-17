# Script to create the session content files for Hugo from a csv file.

def main():
    import csv, sys, os
    from slugify import slugify
    
    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    else:
        source_file = "sessions.csv"

    event_slug = "2024"
    dirname = "sessions/"+event_slug
    try:
        os.mkdir(dirname)
    except FileExistsError:
        pass
    except OSError:
        print ("Creation of the directory "+dirname+" failed" )


    with open(source_file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            title = row['Title']
            speakers = row['Speakers'].split(", ")
            abstract = row['Abstract']
            track = row['Track']
            s_format = row['Format']
            time_start = row['Time start']
            time_end = row['Time end']
            
            slug = slugify(title)
            filename =  f"sessions/{event_slug}/{slug}.md"

            with open(filename, "w") as f:
                f.write("---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"slug: {slug}\n")
                f.write("speakers:\n")
                for s in speakers:
                    f.write(f" - {s}\n")
                f.write(f"time_start: {time_start}\n")
                f.write(f"time_end: {time_end}\n")
                # f.write(f"summary: \"{summary}\"\n")
                f.write(f"track: {track}\n")
                f.write(f"format: {s_format}\n")
                f.write("---\n\n")
                f.write(abstract)


if __name__ == "__main__": 
	main() 

