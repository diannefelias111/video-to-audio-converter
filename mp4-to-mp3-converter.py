import os
from moviepy.editor import VideoFileClip

def is_valid_mp4(file_path):
    """Check if the file is a valid MP4."""
    return os.path.isfile(file_path) and file_path.lower().endswith('.mp4')

def convert_mp4_to_mp3(input_file, output_file):
    """Convert MP4 to MP3 using moviepy."""
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    audio.close()
    video.close()

def main():
    print("MP4 to MP3 Converter")
    input_file = input("Enter the path to the MP4 file: ")

    if is_valid_mp4(input_file):
        # Use Python library (moviepy)
        print("Valid MP4 file. Converting to MP3...")
        
        # Generate output file name
        output_file = os.path.splitext(input_file)[0] + ".mp3"
        
        try:
            # Convert MP4 to MP3
            convert_mp4_to_mp3(input_file, output_file)
            
            # Save MP3 file
            print(f"Conversion complete. MP3 file saved as: {output_file}")
        except Exception as e:
            print(f"An error occurred during conversion: {str(e)}")
    else:
        # Display error message
        print("Error: Invalid MP4 file. Please provide a valid MP4 file path.")

if __name__ == "__main__":
    main()
