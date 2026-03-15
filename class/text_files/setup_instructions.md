# Automated Form Filler Setup Instructions

This script uses `pyautogui` to find elements on your screen by taking small image snippets and searching for them. **It requires you to create these reference images on your own computer so it matches your screen's resolution and theme exactly.**

## Prerequisites
1.  **Install dependencies:**
    Open your terminal/command prompt and run:
    ```bash
    pip install pyautogui opencv-python
    ```
    *(Note: `opencv-python` is required for the `confidence` parameter in pyautogui's image location to work properly).*

2.  **Understand the Failsafe:**
    If the script starts doing something unexpected, **quickly move your mouse pointer to any of the four corners of your screen**. PyAutoGUI has a built-in failsafe that will immediately crash and stop the script if the mouse hits a corner.

## Setup Steps

1.  **Open the Target Form:**
    The script is currently configured to test against a public form at: `https://www.w3schools.com/html/html_forms.asp`. Open this URL in your web browser.

2.  **Take a Screenshot of the First Name Field:**
    *   Use your OS's screenshot tool (e.g., Snipping Tool on Windows, Command+Shift+4 on Mac).
    *   Snip **only** the text box for "First name:".
    *   Save this image as **`firstname_field.png`** in the exact same folder as the `automated_form_filler.py` script (`d:\TheDeuce\File_DS\class\`).

3.  **Take a Screenshot of the Last Name Field:**
    *   Snip **only** the text box for "Last name:".
    *   Save this image as **`lastname_field.png`** in the same folder.

4.  **Take a Screenshot of the Submit Button:**
    *   Snip **only** the "Submit" button at the bottom of the form.
    *   Save this image as **`submit_btn.png`** in the same folder.

## Running the Script

Once you have your three `.png` files saved next to the script, simply run it from your terminal:

```bash
python automated_form_filler.py
```

The script will automatically open the browser, wait 5 seconds (to give you time to ensure the window is active and the form is visible), find the fields using your screenshots, type the data, and press Enter to submit.

## Troubleshooting
*   **"ImageNotFoundException" / "Failed to find..." errors:** 
    1.  Ensure the form is actually visible on your screen (not minimized or hidden behind another window).
    2.  Ensure your browser zoom level hasn't changed since you took the screenshots. PyAutoGUI needs an exact pixel match.
    3.  Try taking a slightly larger or smaller snip of the element.
    4.  Make sure the filenames perfectly match (`firstname_field.png`, `lastname_field.png`, `submit_btn.png`) and are in the correct directory.
