# Script to create the speaker folder and files for Hugo from a csv file.

def main():

    import csv, sys, os
    from slugify import slugify

    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    else:
        source_file = "speakers.csv"

    with open(source_file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            first_name = row['FirstName']
            last_name = row['LastName']
            events = ["2024"]
            designation = row['TagLine']
            bio = row['Bio']
            linkedin = row['LinkedIn']

            title = f"{first_name} {last_name}"

            slug = slugify(title)

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
                f.write(f"linkedin: {linkedin}\n")
                f.write("events:\n")
                for s in events:
                    f.write(" - "+s+"\n")
                f.write("---\n\n")
                f.write(bio)


if __name__ == "__main__": 
	main() 
