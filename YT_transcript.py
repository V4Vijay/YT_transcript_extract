from youtube_transcript_api import YouTubeTranscriptApi
import re

def clean_transcript(transcript):
  """
  Cleans the transcript by removing timestamps.

  Args:
    transcript: A list of dictionaries containing transcript information.

  Returns:
    A cleaned list of dictionaries containing just the text and speaker values.
  """

  cleaned_transcript = []
  for line in transcript:
    # Use regular expression to remove timestamps and punctuation
    text = re.sub(r"^\d+\.\d+: .*$", "", line["text"]).strip()
    # Add only text and speaker information to the cleaned transcript
    cleaned_transcript.append({"text": text})
    #cleaned_transcript.append({"text": text, "speaker": line["speaker"]})
  return cleaned_transcript

def extract_transcript_and_save(url, filename, keywords=[], timestamps={}):
  """
  Extracts the transcript from a YouTube video, cleans it, and saves it to a file.

  Args:
    url: The URL of the YouTube video.
    filename: The name of the file to save the transcript to.
    keywords: A list of keywords to remove from the transcript (not used).
    timestamps: A dictionary where keys are start times (seconds) and values are end times (seconds) of segments to remove (not used).
  """

  try:
    transcript = YouTubeTranscriptApi.get_transcript(url)
    cleaned_transcript = clean_transcript(transcript)

    with open(filename, 'w') as f:
      for line in cleaned_transcript:
        f.write(f"{line['text']}\n")

    print(f"Transcript saved to {filename}")
  except Exception as e:
    print(f"Error extracting transcript: {e}")

# Example usage
url = "VPaOy3G1-2A"
filename = "transcript.txt"

extract_transcript_and_save(url, filename)
