import requests
import sys
import subprocess

# Check if the command line arguments are provided
if len(sys.argv) < 2:
    print("Please provide the word after 'hls' and (optionally) the resolution as command line arguments.")
    sys.exit(1)

# Default resolution
resolution = "1080p"
video_id = sys.argv[1]

# Check if a resolution argument is provided
if len(sys.argv) > 2:
    resolution = sys.argv[2]

# Base URL of the .ts files
base_url = f"https://lp-playback.com/hls/{video_id}/index{resolution}0_"

# Start range of files to download
start_range = 1

# Initialize the end range
end_range = start_range

# List to store the URLs
urls = []
subprocess.run(["mkdir", video_id])

while True:
    # Constructing the file URL
    file_url = f"{base_url}{str(end_range).zfill(5)}.ts"  # Zfill adds leading zeros
    filename = f"{video_id}/index1080p0_{str(end_range).zfill(5)}.ts"

    # Make the request to download the file
    response = requests.get(file_url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Open a file to write the content
        with open(filename, 'wb') as file:
            file.write(response.content)
        urls.append(file_url)
        print(f"Downloaded file: {filename}")
        end_range += 1
    else:
        print(f"Failed to download file: {filename}")
        break
    
# Write the filenames to a file
with open(f"{video_id}/filenames.txt", 'w') as file:
    for i in range(start_range, end_range):
        file.write(f"file 'index1080p0_{str(i).zfill(5)}.ts'\n")

print("Download of each part completed.")

command = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", f"./{video_id}/filenames.txt", "-c", "copy", f"{video_id}/output.mp4"]
print("Running command: " + ' '.join(command))
subprocess.run(command)

