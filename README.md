# Smart Key

## Overview
The **Smart Key** project is a user interface application built with Python's `tkinter` library that simulates a security system. It allows users to enter a PIN to unlock a door and provides an administrative interface for managing users and their access status. The application can:
- Allow users to unlock a door by entering a valid PIN.
- Provide a system administration interface for managing user data, such as first name, last name, PIN, and activity status (active/inactive).
- Display status messages to inform users about successful or unsuccessful PIN entry attempts.

---

## Features

1. **PIN Entry System**:
   - Users can enter a 4-digit PIN to attempt unlocking the door.
   - If the PIN is valid, the system displays the user's details and grants access.
   - If the PIN is invalid or the user is inactive, the system denies access.

2. **Administrative Interface**:
   - Admin users can manage user data such as:
     - First name
     - Last name
     - PIN
     - (In)Active status
   - Admins can update user information, delete users, or add new users.

3. **System Administration Panel**:
   - Admins can open a separate panel to make system-wide changes to user data.
   - A confirmation dialog appears when attempting to access this panel, asking if the user wants to proceed with system administration.

4. **Data Persistence**:
   - User data is saved in a Python file (`user_data.py`) as a dictionary, allowing for easy management and updates.

5. **Interactive UI Elements**:
   - PIN buttons (0-9, Clear (C), and Enter (E)).
   - Status messages to display the result of the PIN entry.
   - Listbox for selecting and editing user information.

---

## How It Works

1. **Main Window**: 
   The main window contains buttons for unlocking the door via PIN or ringing the bell. When a user attempts to unlock the door, they can enter their PIN using a number pad.

2. **PIN Entry**:
   - Users can input a PIN using the on-screen buttons or by typing directly into the entry box.
   - If the PIN is valid, the system checks the user’s activity status:
     - **Active**: Access is granted, and a welcome message with the user’s name is displayed.
     - **Inactive**: Access is denied with a status message indicating that the user is inactive.
   - If the PIN is invalid, the system displays an error message.

3. **Admin Panel**:
   - The admin panel allows for viewing and editing user information.
   - Admins can select a user from the list to view or update their details (first name, last name, PIN, active/inactive status).
   - Changes can be saved back to the database, and users can be deleted.

4. **Ring Button**: 
   - The "RING" button simulates a doorbell, showing a message indicating that someone is coming.

5. **System Administration Confirmation**:
   - If the PIN `9999` is entered, the system prompts the user with a dialog box asking if they wish to enter the system administration mode. If "Yes" is selected, the admin panel is shown.

---

## User Interface

### Main Window
- **RING Button**: Triggers a notification window.
- **UNLOCK Button**: Displays the PIN entry panel for unlocking the door.

### PIN Entry Panel
- **PIN Entry**: Users can enter their PIN using the on-screen number pad.
- **Status Messages**: Shows whether the door is unlocked or if the PIN was incorrect.

### Admin Panel
- **User List**: Displays the list of users with details (Last Name, First Name, PIN, (In)Active status).
- **User Information**: Editable fields for First Name, Last Name, PIN, and Active/Inactive status.
- **Save Button**: Saves changes to the user data.
- **Delete Button**: Deletes the selected user.
- **Exit Button**: Exits the application.

---

### Example User Data

user_data = {
    '1234': {'FirstName': 'John', 'LastName': 'Doe', 'PIN': '1234', '(In)Active': 1},
    '5678': {'FirstName': 'Jane', 'LastName': 'Smith', 'PIN': '5678', '(In)Active': 0},
}

---

### Key Sections:
1. **Overview**: Brief introduction to the project.
2. **Features**: Highlight the key features of the app.
3. **How It Works**: Explains the core functionality and flow of the application.
4. **Example User Data**: Shows how the user data is structured.

This project is not licensed. Feel free to use and modify it according to your needs.

This structure provides a clear and concise guide to your project, making it easier for others to understand and use.
