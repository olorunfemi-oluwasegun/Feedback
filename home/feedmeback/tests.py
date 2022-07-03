from boool import *

ogre = get_transcript()
transcript = ogre[0]
link = ogre[1]

print(link)
print(transcript)

base = Sorting_feedback(transcript, link).sort_now()
print(base)

