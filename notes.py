import os
import pickle
import datetime

NOTE_DIRECTORY = "notes"

class Note:
    def __init__(self, title, content, category):
        self.title = title
        self.content = content
        self.category = category
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

class NoteSystem:
    def __init__(self):
          if not os.path.exists(NOTE_DIRECTORY):
            os.makedirs(NOTE_DIRECTORY)
        
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        self.save_notes()

    def list_notes(self):
        if not self.notes:
            print("📔 You don't have any notes yet. Add some using option '1'.")
            return
        print("\n📝 Your Notes:")
        for index, note in enumerate(self.notes):
            print(f"{index + 1}. {note.title} ({note.category})")
            print(f"   🕒 Created: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   🔄 Updated: {note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}\n")

    def view_note(self, index):
        if 0 <= index < len(self.notes):
            note = self.notes[index]
            print(f"📌 Title: {note.title}")
            print(f"📂 Category: {note.category}")
            print(f"🕒 Created: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"🔄 Updated: {note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"✏️ Content: {note.content}")
        else:
            print("Invalid note index.")

    def search_notes(self, query):
        found_notes = []
        for note in self.notes:
            if query.lower() in note.title.lower() or query.lower() in note.content.lower():
                found_notes.append(note)
        
        if found_notes:
            print(f"\n🔍 Search Results for '{query}':")
            for index, note in enumerate(found_notes):
                print(f"{index + 1}. {note.title} ({note.category})")
                print(f"   🕒 Created: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"   🔄 Updated: {note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}\n")
        else:
            print(f"No matching notes found for '{query}'.")

    def edit_note(self, index, new_title, new_content, new_category):
        if 0 <= index < len(self.notes):
            note = self.notes[index]
            note.title = new_title
            note.content = new_content
            note.category = new_category
            note.updated_at = datetime.datetime.now()
            print("✅ Note updated successfully.")
            self.save_notes()
        else:
            print("Invalid note index.")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            print("🗑️ Note deleted successfully.")
            self.save_notes()
        else:
            print("Invalid note index.")

    def save_notes(self):
          with open(os.path.join(NOTE_DIRECTORY, 'notes.pkl'), 'wb') as file:
            pickle.dump(self.notes, file)

    def load_notes(self):
      notes_file_path = os.path.join(NOTE_DIRECTORY, 'notes.pkl')
        if os.path.exists(notes_file_path):
            with open(notes_file_path, 'rb') as file:
                self.notes = pickle.load(file)

def main():
    note_system = NoteSystem()
    note_system.load_notes()  # Load existing notes on startup
    
    while True:
        print("\n📚 Note System Menu:")
        print("1. ✍️ Add Note")
        print("2. 📋 List Notes")
        print("3. 🔍 View Note")
        print("4. 🔎 Search Notes")
        print("5. ✏️ Edit Note")
        print("6. 🗑️ Delete Note")
        print("7. 🚪 Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("📝 Enter note title: ")
            content = input("✏️ Enter note content: ")
            category = input("📂 Enter note category: ")
            note = Note(title, content, category)
            note_system.add_note(note)
            print("✅ Note added successfully.")
        elif choice == '2':
            note_system.list_notes()
        elif choice == '3':
            index = int(input("🔢 Enter note index to view: ")) - 1
            note_system.view_note(index)
        elif choice == '4':
            query = input("🔍 Enter search query: ")
            note_system.search_notes(query)
        elif choice == '5':
            index = int(input("🔢 Enter note index to edit: ")) - 1
            new_title = input("✏️ Enter new title: ")
            new_content = input("✏️ Enter new content: ")
            new_category = input("📂 Enter new category: ")
            note_system.edit_note(index, new_title, new_content, new_category)
        elif choice == '6':
            index = int(input("🔢 Enter note index to delete: ")) - 1
            note_system.delete_note(index)
        elif choice == '7':
            print("👋 Goodbye! Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
