from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


DEVELOPER_KEY = ''
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(q,timemark):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)


  search_response = youtube.search().list(
    q=q,
    part='id,snippet',
    maxResults=50,
    publishedAfter=timemark.isoformat()[:-10]+"Z",
    type='video'
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append(f"https://www.youtube.com/watch?v={search_result['id']['videoId']}")

  return videos
