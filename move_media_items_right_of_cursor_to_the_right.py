'''
Copyright 2016 Fredrik Johansson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

# Get the cursor position 
cp = RPR_GetCursorPosition()

# Get number of media items
mediaItemCount = RPR_CountMediaItems(0)

# Initialize index value at 0
currentIndex = 0

# Loop through all media items
while currentIndex < mediaItemCount:
 
  # Get the n'th media item.
  currentMediaItem = RPR_GetMediaItem(0, currentIndex)
  
  # Get the position of the media item
  currentMediaItemPosition = RPR_GetMediaItemInfo_Value(currentMediaItem, "D_POSITION")
  
  # Check if the media item position is bigger than the cursor position (to the right of it)
  if(currentMediaItemPosition >= cp):
    
    # Move media item
    # Moved to the current position + 10 seconds.
    RPR_SetMediaItemPosition(currentMediaItem, currentMediaItemPosition+10, True)
  
  # Increase the index value by one
  currentIndex = currentIndex + 1
