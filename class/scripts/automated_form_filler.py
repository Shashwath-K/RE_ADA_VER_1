import pyautogui
import time
import webbrowser
import sys
import os

# --- Configuration ---
# Use a public sample form for testing
FORM_URL = "https://www.w3schools.com/html/html_forms.asp" 

# Confidence requires python -m pip install opencv-python
CONFIDENCE_LEVEL = 0.8

# Data to fill in the form
FORM_DATA = {
    'first_name': 'Shash',
    'last_name': 'Doe'
}

# --- Actions ---

def open_form():
    """Opens the web browser to the designated form url."""
    print(f"Opening {FORM_URL}...")
    webbrowser.open(FORM_URL)
    
    # Wait for the browser and page to load. 
    # Adjust this delay based on your internet and system speed.
    print("Waiting for page to load (5 seconds)...")
    time.sleep(5)

def fill_field(image_path, text_to_type):
    """Locates a field by its image, clicks it, and types the text."""
    
    # Check if the reference image exists
    if not os.path.exists(image_path):
         print(f"Error: Could not find reference image '{image_path}'.")
         print("Please take a screenshot of the target area, save it as this filename, and place it in the same directory as this script.")
         return False

    print(f"Searching for '{image_path}' on screen...")
    try:
        # Locate the image. LocateCenterOnScreen returns x,y coordinates
        field_location = pyautogui.locateCenterOnScreen(image_path, confidence=CONFIDENCE_LEVEL)
        
        if field_location:
            print(f"Found {image_path} at {field_location}. Clicking and typing...")
            # Click the field to focus it
            pyautogui.click(field_location)
            
            # Type the data
            pyautogui.write(text_to_type, interval=0.1) 
            return True
        else:
             print(f"Failed to find '{image_path}' on screen. Make sure it's visible.")
             return False

    except pyautogui.ImageNotFoundException:
        print(f"PyAutoGUI ImageNotFoundException: Could not locate '{image_path}'.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while looking for '{image_path}': {e}")
        return False


def submit_form(image_path=None):
    """Submits the form, optionally looking for a submit button image, or just pressing Enter."""
    if image_path:
        print(f"Looking for Submit button image: '{image_path}'...")
        if os.path.exists(image_path):
            try:
                button_loc = pyautogui.locateCenterOnScreen(image_path, confidence=CONFIDENCE_LEVEL)
                if button_loc:
                     print("Submit button found. Clicking...")
                     pyautogui.click(button_loc)
                     return True
            except pyautogui.ImageNotFoundException:
                 print("Could not find submit button image on screen.")
        else:
             print(f"Submit button image '{image_path}' not found in directory.")
             
    # Fallback to pressing Enter
    print("Pressing 'Enter' to submit...")
    pyautogui.press('enter')
    return True

def main():
    print("--- Starting Automated Form Filler ---")
    print("NOTE: Move your mouse to one of the screen corners to abort the script safely.")
    
    # Open the webpage
    open_form()
    
    # Fill First Name 
    # This requires 'firstname_field.png' to be in the current directory.
    # Take a screenshot of the "First name:" input box on the W3Schools page.
    if not fill_field('firstname_field.png', FORM_DATA['first_name']):
         print("Failed on the first name field. Stopping script.")
         sys.exit(1)
         
    # Short pause between actions
    time.sleep(1)
    
    # Form usually jumps to next field via Tab, or we can find it by image
    # We will demonstrate finding by image again:
    if not fill_field('lastname_field.png', FORM_DATA['last_name']):
          print("Failed on the last name field. Stopping script.")
          sys.exit(1)
          
    time.sleep(1)
    
    # Submit the form
    # Taking a snippet of the "Submit" button as 'submit_btn.png'
    submit_form('submit_btn.png')
    
    print("--- Form Filler Completed ---")

if __name__ == "__main__":
    # Safety feature: if true, moving mouse to a corner throws an exception to kill the script
    pyautogui.FAILSAFE = True 
    main()
