import argparse
from pathlib import Path
from add_song import add_song
from database import init_database

# Set up parameters
parser = argparse.ArgumentParser(description="Automatically recognize songs")
parser.add_argument("--update", "-u", action="store_true", help="Update the song database")
parser.add_argument("--list", "-l", action="store_true", help="View list of files")
parser.add_argument("--init", "-i", type=Path, help="Initialize the database")
parser.add_argument("--add", "-a", type=Path, help="Path to MP3 file to add")
parser.add_argument("--title", "-t", help="Song title to add")
parser.add_argument("--artist", "-A", help="Song artist to add")
parser.add_argument("--year", "-y", help="Song year to add")

# Get args
args = parser.parse_args()

if args.update:
	# Update the database
	add_song(args.title, args.artist, args.year, args.add)
elif args.list:
	# List the database
	pass
elif args.init != None:
	# Initialize the database
	init_database(args.init)
else:
	# Recognize the song
	pass