import argparse
from pathlib import Path

# Set up parameters
parser = argparse.ArgumentParser(description="Automatically recognize songs")
parser.add_argument("--update", "-u", action="store_true", help="Update the song database")
parser.add_argument("--list", "-l", action="store_true", help="View list of files")
parser.add_argument("--init", "-i", action="store_true", help="Initialize the database")
parser.add_argument("--add", "-a", type=Path, help="Path to MP3 file to add")
parser.add_argument("--title", "-t", help="Song title to add")
parser.add_argument("--artist", "-A", help="Song artist to add")
parser.add_argument("--year", "-y", help="Song year to add")

# Get args
args = parser.parse_args()

if args.update:
	# Update the database
	pass
elif args.list:
	# List the database
	pass
elif args.init:
	# Initialize the database
	pass
else:
	# Recognize the song
	pass