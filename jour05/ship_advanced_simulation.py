import tkinter as tk
from ttkbootstrap import Style, ttk
import json
from main_menu import Ship, Part
from datetime import datetime
from PIL import Image, ImageTk
import random

class ShipManagementGUI:
    def __init__(self, root, ship):
        self.root = root
        self.ship = ship
        self.style = Style(theme='darkly')
        
        self.root.title("Ship Management System")
        self.root.geometry("1200x800")
        
        self.main_container = ttk.Frame(self.root, padding="10")
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        self.create_left_panel()
        self.create_right_panel()
        
    def create_left_panel(self):
        left_panel = ttk.LabelFrame(self.main_container, text="Ship Status", padding="10")
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        try:
            image = Image.open("images/image.png")
            image = image.resize((600, 700), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(image)
            
            self.canvas = tk.Canvas(left_panel, width=600, height=700)
            self.canvas.pack(fill=tk.BOTH, expand=True)
            
            self.canvas.create_image(
                300, 
                350, 
                image=self.bg_image,
                anchor='center' 
            )
            
            
            ship_header = self.canvas.create_text(
                300, 
                30,   
                text=f"Ship: {self.ship.name}",
                font=('Helvetica', 24, 'bold'),
                fill='white',
                anchor='center'
            )
            
            
            self.ship_display = tk.Text(
                left_panel,
                wrap=tk.WORD,
                height=20,
                font=('Courier', 18, 'bold'),
                bg='#00000080',  
                fg='white',
                relief='flat',
                padx=10,
                pady=10
            )
            
            self.ship_display_window = self.canvas.create_window(
                300,  
                350,  
                window=self.ship_display,
                width=500, 
                anchor='center'
            )
            
            self.update_ship_display()
            
        except Exception as e:
            print(f"Error loading image: {e}")
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
        right_panel = ttk.Frame(self.main_container, padding="10")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(5, 0))
        
        # Storm Event Section
        storm_frame = ttk.LabelFrame(right_panel, text="Weather Event", padding="10")
        storm_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(
            storm_frame,
            text="🌊 Simulate Storm",
            style='warning.TButton',
            command=self.simulate_storm
        ).pack(fill=tk.X)
        
        # Add New Part Section
        add_frame = ttk.LabelFrame(right_panel, text="Add New Part", padding="10")
        add_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(add_frame, text="New Part Name:").pack(fill=tk.X)
        self.new_part_var = tk.StringVar()
        self.new_part_entry = ttk.Entry(add_frame, textvariable=self.new_part_var)
        self.new_part_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(add_frame, text="Part Material:").pack(fill=tk.X)
        self.new_material_var = tk.StringVar()
        self.new_material_entry = ttk.Entry(add_frame, textvariable=self.new_material_var)
        self.new_material_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(
            add_frame, 
            text="Add Part",
            style='primary.TButton',
            command=self.add_part
        ).pack(fill=tk.X)
        
        # Delete Part Section
        delete_frame = ttk.LabelFrame(right_panel, text="Delete Part", padding="10")
        delete_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(delete_frame, text="Part Name:").pack(fill=tk.X)
        self.delete_part_var = tk.StringVar()
        self.delete_part_entry = ttk.Entry(delete_frame, textvariable=self.delete_part_var)
        self.delete_part_entry.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(
            delete_frame, 
            text="Delete Part",
            style='danger.TButton',
            command=self.delete_part
        ).pack(fill=tk.X)
        
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
        
        ttk.Button(
            right_panel, 
            text="View History",
            style='info.TButton',
            command=self.show_history
        ).pack(fill=tk.X)
        
        self.message_frame = ttk.Frame(right_panel)
        self.message_frame.pack(fill=tk.X, pady=(10, 0))

    def update_ship_display(self):
        self.ship_display.delete(1.0, tk.END)
        display_text = "Current Ship State:\n\n"
        
        
        critical_parts = []
        
        for part_name, part in self.ship._Ship__parts.items():
            display_text += f"{part}\n"
            if part.needs_replacement():
                critical_parts.append(part_name)
        
        # Warning message
        if critical_parts:
            display_text += "\n⚠️ WARNING ⚠️\n"
            display_text += "The following parts need immediate replacement:\n"
            for part in critical_parts:
                display_text += f"- {part}\n"
        
        self.ship_display.insert(tk.END, display_text)
        
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
            self.part_name_var.set("")
            self.material_var.set("")
            
    def replace_part(self):
        old_part = self.old_part_var.get()
        new_name = self.new_part_name_var.get()
        new_material = self.new_part_material_var.get()
        

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
                font=('Courier', 16)
            )
            history_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            content = f"Modification history for {self.ship.name}:\n\n"
            for mod in history_data['modifications']:
                content += f"Time: {mod['timestamp']}\n"
                content += f"Type: {mod['action']}\n"
                
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
        for widget in self.message_frame.winfo_children():
            if isinstance(widget, ttk.Label) and widget.cget("style") == "danger.TLabel":
                widget.destroy()
                
        # Create new error message
        error_label = ttk.Label(
            self.message_frame,  
            text=message,
            style='danger.TLabel',
            wraplength=300  
        )
        error_label.pack(fill=tk.X, pady=5)
        
        self.root.after(4000, error_label.destroy)

    def show_success(self, message):
        for widget in self.message_frame.winfo_children():
            if isinstance(widget, ttk.Label) and widget.cget("style") == "success.TLabel":
                widget.destroy()
                
        success_label = ttk.Label(
            self.message_frame,  
            text=message,
            style='success.TLabel',
            wraplength=300 
        )
        success_label.pack(fill=tk.X, pady=5)
        
        self.root.after(3000, success_label.destroy)

    def add_part(self):
        part_name = self.new_part_var.get()
        material = self.new_material_var.get()
        

        if not all([part_name, material]):
            error_msg = "Failed to add part: Please fill in all fields!"
            self.ship.add_to_history('error', {
                'action': 'add_part',
                'attempted_values': {
                    'part_name': part_name,
                    'material': material
                },
                'error': error_msg
            })
            self.show_error(error_msg)
            self.new_part_var.set("")
            self.new_material_var.set("")
            return
            
        try:
            new_part = Part(part_name, material)
            if part_name in self.ship._Ship__parts:
                error_msg = f"Failed to add part: Part '{part_name}' already exists!"
                self.ship.add_to_history('error', {
                    'action': 'add_part',
                    'attempted_values': {
                        'part_name': part_name,
                        'material': material
                    },
                    'error': error_msg
                })
                self.show_error(error_msg)
            else:
                self.ship._Ship__parts[part_name] = new_part
                self.ship.add_to_history('add_part', {
                    'part_name': part_name,
                    'material': material
                })
                self.update_ship_display()
                self.show_success(f"Added new part: {new_part}")
        except Exception as e:
            error_msg = f"Failed to add part: {str(e)}"
            self.ship.add_to_history('error', {
                'action': 'add_part',
                'attempted_values': {
                    'part_name': part_name,
                    'material': material
                },
                'error': error_msg
            })
            self.show_error(error_msg)
        finally:
            self.new_part_var.set("")
            self.new_material_var.set("")

    def delete_part(self):
        part_name = self.delete_part_var.get()
        
        if not part_name:
            error_msg = "Failed to delete part: Please provide a part name!"
            self.ship.add_to_history('error', {
                'action': 'delete_part',
                'attempted_values': {
                    'part_name': part_name
                },
                'error': error_msg
            })
            self.show_error(error_msg)
            self.delete_part_var.set("")
            return
            
        try:
            if part_name not in self.ship._Ship__parts:
                error_msg = f"Failed to delete part: Part '{part_name}' not found!"
                self.ship.add_to_history('error', {
                    'action': 'delete_part',
                    'attempted_values': {
                        'part_name': part_name
                    },
                    'error': error_msg
                })
                self.show_error(error_msg)
            else:
                deleted_part = self.ship._Ship__parts.pop(part_name)
                self.ship.add_to_history('delete_part', {
                    'part_name': part_name,
                    'deleted_part': str(deleted_part)
                })
                self.update_ship_display()
                self.show_success(f"Deleted part: {deleted_part}")
        except Exception as e:
            error_msg = f"Failed to delete part: {str(e)}"
            self.ship.add_to_history('error', {
                'action': 'delete_part',
                'attempted_values': {
                    'part_name': part_name
                },
                'error': error_msg
            })
            self.show_error(error_msg)
        finally:
            self.delete_part_var.set("")

    def simulate_storm(self):
        """Simulate a storm that damages all parts"""
        try:
            damage_report = []
            
            # Apply damage randomly (10 - 30 per cent)
            for part_name, part in self.ship._Ship__parts.items():
                storm_damage = random.randint(10, 30)
                old_usury = part.usury
                
                # Calculate new usury
                part.usury = min(100, part.usury + storm_damage)
                
                damage_report.append({
                    'part_name': part_name,
                    'old_usury': old_usury,
                    'damage': storm_damage,
                    'new_usury': part.usury
                })
            
            report_text = "Storm Damage Report:\n"
            critical_parts = []
            
            for damage in damage_report:
                report_text += f"\n{damage['part_name']}:\n"
                report_text += f"  Damage taken: {damage['damage']}%\n"
                report_text += f"  Usury: {damage['old_usury']}% → {damage['new_usury']}%\n"
                
                if damage['new_usury'] > 80:
                    critical_parts.append(damage['part_name'])
            
            # Warning about parts in critical state
            if critical_parts:
                report_text += "\n⚠️ CRITICAL WARNING ⚠️\n"
                report_text += "The following parts need immediate replacement:\n"
                for part in critical_parts:
                    report_text += f"- {part}\n"
            
            # Add storm event to history
            self.ship.add_to_history('storm_event', {
                'damage_report': damage_report,
                'critical_parts': critical_parts
            })
            
            # Storm report 
            storm_window = tk.Toplevel(self.root)
            storm_window.title("Storm Event")
            storm_window.geometry("400x500")
            
            report_text_widget = tk.Text(
                storm_window,
                wrap=tk.WORD,
                font=('Courier', 11),
                padx=10,
                pady=10
            )
            report_text_widget.pack(fill=tk.BOTH, expand=True)
            report_text_widget.insert(tk.END, report_text)
            report_text_widget.config(state='disabled')
            
            self.update_ship_display()
            
            # Warning message for parts in critical state
            if critical_parts:
                self.show_error("Storm caused critical damage! Some parts need immediate replacement!")
            else:
                self.show_success("Ship weathered the storm with manageable damage.")
                
        except Exception as e:
            error_msg = f"Error during storm simulation: {str(e)}"
            self.ship.add_to_history('error', {
                'action': 'storm_event',
                'error': error_msg
            })
            self.show_error(error_msg)

def main():
    hull = Part("Hull", "Steel")
    engine = Part("Engine", "Iron")
    ship = Ship("Titanic", [hull, engine])
    
    # Create and run GUI
    root = tk.Tk()
    app = ShipManagementGUI(root, ship)
    root.mainloop()

if __name__ == "__main__":
    main()
