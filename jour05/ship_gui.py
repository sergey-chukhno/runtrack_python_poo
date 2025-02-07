import tkinter as tk
from ttkbootstrap import Style, ttk
import json
from main_menu import Ship, Part
from datetime import datetime
from PIL import Image, ImageTk

class ShipManagementGUI:
    def __init__(self, root, ship):
        self.root = root
        self.ship = ship
        self.style = Style(theme='darkly')
        
        # Configure the root window
        self.root.title("Ship Management System")
        self.root.geometry("1200x800")
        
        # Create main container
        self.main_container = ttk.Frame(self.root, padding="10")
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create left and right panels
        self.create_left_panel()
        self.create_right_panel()
        
    def create_left_panel(self):
        # Left panel for ship display
        left_panel = ttk.LabelFrame(self.main_container, text="Ship Status", padding="10")
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        try:
            image = Image.open("images/image.png")
            # Resize image to fit panel
            image = image.resize((600, 700), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(image)
            
            # Create canvas
            self.canvas = tk.Canvas(left_panel, width=600, height=700)
            self.canvas.pack(fill=tk.BOTH, expand=True)
            
            # Center image by using canvas center coordinates
            self.canvas.create_image(
                300,  # Half of canvas width (600/2)
                350,  # Half of canvas height (700/2)
                image=self.bg_image,
                anchor='center'  # Changed anchor to center
            )
            
            # Ship name header with semi-transparent background
            ship_header = self.canvas.create_text(
                300,  # x position (centered)
                30,   # y position
                text=f"Ship: {self.ship.name}",
                font=('Helvetica', 20, 'bold'),
                fill='white',
                anchor='center'
            )
            
            # Create text widget with transparent background
            self.ship_display = tk.Text(
                left_panel,
                wrap=tk.WORD,
                height=20,
                font=('Courier', 14, 'bold'),
                bg='#00000080',  # Semi-transparent black
                fg='white',
                relief='flat',
                padx=10,
                pady=10
            )
            
            # Place text widget on top of canvas
            self.ship_display_window = self.canvas.create_window(
                300,  # x position (centered)
                350,  # y position
                window=self.ship_display,
                width=500,  # adjust width as needed
                anchor='center'
            )
            
            self.update_ship_display()
            
        except Exception as e:
            print(f"Error loading image: {e}")
            # Fallback to normal display without background
            ship_header = ttk.Label(
                left_panel,
                text=f"Ship: {self.ship.name}",
                font=('Helvetica', 20, 'bold')
            )
            ship_header.pack(pady=(0, 10))
            
            self.ship_display = tk.Text(
                left_panel,
                wrap=tk.WORD,
                height=30,
                font=('Courier', 14)
            )
            self.ship_display.pack(fill=tk.BOTH, expand=True)
            self.update_ship_display()

    def create_right_panel(self):
        # Right panel for controls
        right_panel = ttk.Frame(self.main_container, padding="10")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(5, 0))
        
        # Material Change Section
        material_frame = ttk.LabelFrame(right_panel, text="Change Material", padding="10")
        material_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(material_frame, text="Part Name:").pack(fill=tk.X)
        self.part_name_var = tk.StringVar()
        self.part_name_entry = ttk.Entry(material_frame, textvariable=self.part_name_var)
        self.part_name_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(material_frame, text="New Material:").pack(fill=tk.X)
        self.material_var = tk.StringVar()
        self.material_entry = ttk.Entry(material_frame, textvariable=self.material_var)
        self.material_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(
            material_frame, 
            text="Change Material",
            style='primary.TButton',
            command=self.change_material
        ).pack(fill=tk.X)
        
        # Replace Part Section
        replace_frame = ttk.LabelFrame(right_panel, text="Replace Part", padding="10")
        replace_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(replace_frame, text="Part to Replace:").pack(fill=tk.X)
        self.old_part_var = tk.StringVar()
        self.old_part_entry = ttk.Entry(replace_frame, textvariable=self.old_part_var)
        self.old_part_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(replace_frame, text="New Part Name:").pack(fill=tk.X)
        self.new_part_name_var = tk.StringVar()
        self.new_part_name_entry = ttk.Entry(replace_frame, textvariable=self.new_part_name_var)
        self.new_part_name_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(replace_frame, text="New Part Material:").pack(fill=tk.X)
        self.new_part_material_var = tk.StringVar()
        self.new_part_material_entry = ttk.Entry(replace_frame, textvariable=self.new_part_material_var)
        self.new_part_material_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(
            replace_frame, 
            text="Replace Part",
            style='primary.TButton',
            command=self.replace_part
        ).pack(fill=tk.X)
        
        # History Button
        ttk.Button(
            right_panel, 
            text="View History",
            style='info.TButton',
            command=self.show_history
        ).pack(fill=tk.X)
        
        # Create a frame for messages
        self.message_frame = ttk.Frame(right_panel)
        self.message_frame.pack(fill=tk.X, pady=(10, 0))

    def update_ship_display(self):
        self.ship_display.delete(1.0, tk.END)
        display_text = "Current Ship State:\n\n"
        for part_name, part in self.ship._Ship__parts.items():
            display_text += f"{part}\n"
        self.ship_display.insert(tk.END, display_text)
        
        # Configure tags for better visibility
        self.ship_display.tag_configure("center", justify='center')
        self.ship_display.tag_add("center", "1.0", "end")
        
    def change_material(self):
        part_name = self.part_name_var.get()
        material = self.material_var.get()
        
        try:
            self.ship.change_material(part_name, material)
            self.update_ship_display()
            self.show_success(f"Changed {part_name}'s material to {material}")
        except KeyError:
            error_msg = f"Failed to change material: Part '{part_name}' not found!"
            self.ship.add_to_history('error', {
                'action': 'change_material',
                'part_name': part_name,
                'attempted_material': material,
                'error': error_msg
            })
            self.show_error(error_msg)
        finally:
            # Clear input fields regardless of success or failure
            self.part_name_var.set("")
            self.material_var.set("")
            
    def replace_part(self):
        old_part = self.old_part_var.get()
        new_name = self.new_part_name_var.get()
        new_material = self.new_part_material_var.get()
        
        # Input validation
        if not all([old_part, new_name, new_material]):
            error_msg = "Failed to replace part: Please fill in all fields!"
            self.ship.add_to_history('error', {
                'action': 'replace_part',
                'attempted_values': {
                    'old_part': old_part,
                    'new_name': new_name,
                    'new_material': new_material
                },
                'error': error_msg
            })
            self.show_error(error_msg)
            # Clear input fields after validation error
            self.old_part_var.set("")
            self.new_part_name_var.set("")
            self.new_part_material_var.set("")
            return
            
        try:
            new_part = Part(new_name, new_material)
            self.ship.replace_part(old_part, new_part)
            self.update_ship_display()
            self.show_success(f"Replaced {old_part} with {new_part}")
        except (KeyError, Exception) as e:
            if isinstance(e, KeyError):
                error_msg = f"Failed to replace part: Part '{old_part}' not found!"
            else:
                error_msg = f"Failed to replace part: {str(e)}"
            
            self.ship.add_to_history('error', {
                'action': 'replace_part',
                'attempted_values': {
                    'old_part': old_part,
                    'new_name': new_name,
                    'new_material': new_material
                },
                'error': error_msg
            })
            self.show_error(error_msg)
        finally:
            # Clear input fields regardless of success or failure
            self.old_part_var.set("")
            self.new_part_name_var.set("")
            self.new_part_material_var.set("")
            
    def show_history(self):
        try:
            with open(f'{self.ship.name}_history.json', 'r') as f:
                history_data = json.load(f)
            
            history_window = tk.Toplevel(self.root)
            history_window.title("Modification History")
            history_window.geometry("600x400")
            
            history_text = tk.Text(
                history_window, 
                wrap=tk.WORD,
                font=('Courier', 11)
            )
            history_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            content = f"Modification history for {self.ship.name}:\n\n"
            for mod in history_data['modifications']:
                content += f"Time: {mod['timestamp']}\n"
                content += f"Type: {mod['action']}\n"
                
                # Different formatting for errors vs successful actions
                if mod['action'] == 'error':
                    content += "ERROR DETAILS:\n"
                    for key, value in mod['details'].items():
                        if isinstance(value, dict):
                            content += f"{key}:\n"
                            for k, v in value.items():
                                content += f"  {k}: {v}\n"
                        else:
                            content += f"{key}: {value}\n"
                else:
                    content += "ACTION DETAILS:\n"
                    for key, value in mod['details'].items():
                        content += f"{key}: {value}\n"
                content += "\n"
                
            history_text.insert(tk.END, content)
            history_text.config(state='disabled')
            
        except FileNotFoundError:
            self.show_error("No history file found.")
            
    def show_error(self, message):
        # Remove any existing error messages
        for widget in self.message_frame.winfo_children():
            if isinstance(widget, ttk.Label) and widget.cget("style") == "danger.TLabel":
                widget.destroy()
                
        # Create new error message
        error_label = ttk.Label(
            self.message_frame,  # Changed parent to message_frame
            text=message,
            style='danger.TLabel',
            wraplength=300  # Added wrap length for better text display
        )
        error_label.pack(fill=tk.X, pady=5)
        
        # Auto-remove message after 5 seconds (5000 milliseconds)
        self.root.after(5000, error_label.destroy)

    def show_success(self, message):
        # Remove any existing success messages
        for widget in self.message_frame.winfo_children():
            if isinstance(widget, ttk.Label) and widget.cget("style") == "success.TLabel":
                widget.destroy()
                
        # Create new success message
        success_label = ttk.Label(
            self.message_frame,  # Changed parent to message_frame
            text=message,
            style='success.TLabel',
            wraplength=300  # Added wrap length for better text display
        )
        success_label.pack(fill=tk.X, pady=5)
        
        # Auto-remove message after 5 seconds (5000 milliseconds)
        self.root.after(5000, success_label.destroy)

def main():
    # Create initial ship
    hull = Part("Hull", "Steel")
    engine = Part("Engine", "Iron")
    ship = Ship("Titanic", [hull, engine])
    
    # Create and run GUI
    root = tk.Tk()
    app = ShipManagementGUI(root, ship)
    root.mainloop()

if __name__ == "__main__":
    main()
