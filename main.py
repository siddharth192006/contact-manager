import tkinter as tk
from tkinter import messagebox
import os
import qrcode
from tkinter import PhotoImage

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("600x400")
        self.root.config(bg="white")
        self.create_main_page()

    def create_main_page(self):
        """Main Page with Logo and Buttons"""
        # Left side logo (replace with your image file)
        self.logo = PhotoImage(file="logo.png")  # Replace with your logo file path
        logo_label = tk.Label(self.root, image=self.logo, bg="white")
        logo_label.grid(row=0, column=0, padx=10, pady=10)

        # Right side: Buttons in a box with fancy look
        frame = tk.Frame(self.root, bd=1, relief="solid", bg="white")
        frame.grid(row=0, column=1, padx=15, pady=10)

        button1 = tk.Button(frame, text="Contact & Billing", width=15, height=2, command=self.open_contact_page, bg="#4CAF50", fg="white",activebackground='#47a14a',activeforeground='white', font=("Arial", 12, "bold"))
        button1.pack(pady=10)

        button2 = tk.Button(frame, text="About", width=15, height=2, command=self.open_another_action_page, bg="#2196F3", fg="white",activebackground='#1b7fcf',activeforeground='white',font=("Arial", 12, "bold"))
        button2.pack(pady=10)

        button3 = tk.Button(frame, text="Exit", width=15, height=2, command=self.root.quit, bg="#f44336",activebackground='#c9372c', activeforeground='white',fg="white", font=("Arial", 12, "bold"))
        button3.pack(pady=10)

    def open_contact_page(self):
        """Hide Main Page and Open Contact Page"""
        self.root.withdraw()  # Hide the main page
        contact_page = ContactPage(self.root)

    def open_another_action_page(self):
        """Open Another Action Page"""
        self.root.withdraw()  # Hide main page
        another_action_page = AnotherActionPage(self.root)


class ContactPage:
    def __init__(self, root):
        self.root = root
        self.create_contact_page()

    def create_contact_page(self):
        """Contact Page for Client Info and Billing"""
        self.contact_window = tk.Toplevel(self.root)
        self.contact_window.title("Contact and Billing")
        self.contact_window.geometry("600x850")
        self.contact_window.config(bg="white")

        # Input fields for client details
        tk.Label(self.contact_window, text="Client Full Name:", bg="white", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.contact_window, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.contact_window, text="Phone Number:", bg="white", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.contact_window, font=("Arial", 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.contact_window, text="Email ID:", bg="white", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(self.contact_window, font=("Arial", 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.contact_window, text="Price:", bg="white", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.price_entry = tk.Entry(self.contact_window, font=("Arial", 12))
        self.price_entry.grid(row=3, column=1, padx=10, pady=5)

        # Total label
        self.total_label = tk.Label(self.contact_window, text=f"Total: ₹0.00", bg="white", font=("Arial", 12, "bold"))
        self.total_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Save data and generate QR code button
        save_button = tk.Button(self.contact_window, text="Save Information", command=self.save_user_data, width=20, height=2, bg="#4CAF50", fg="white",activebackground='#3b8a3e',activeforeground='white', font=("Arial", 12, "bold"))
        save_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Back button to go back to main page
        back_button = tk.Button(self.contact_window, text="Back to Main Page", command=self.back_to_main, width=20, height=2, bg="#2196F3", fg="white",activebackground='#1c7dc9',activeforeground='white', font=("Arial", 12, "bold"))
        back_button.grid(row=6, column=0, columnspan=2, pady=10)

        # QR code image display
        self.qr_label = tk.Label(self.contact_window, bg="white")
        self.qr_label.grid(row=7, column=0, columnspan=2, pady=10)

    def calculate_price(self):
        """Price Calculation Based on Operation"""
        try:
            price = float(self.price_entry.get())
            total = price + 10  # Example: Adding a fixed amount for simplicity
            self.total_label.config(text=f"Total: ₹{total:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid price entered!")

    def generate_qr(self, payment_info):
        """Generate QR Code for Payment"""
        qr = qrcode.make(payment_info)
        qr.save("payment_qr.png")
        qr_img = tk.PhotoImage(file="payment_qr.png")
        self.qr_label.config(image=qr_img)
        self.qr_label.image = qr_img  # Keep a reference to the image to avoid garbage collection

    def save_user_data(self):
        """Save User Data"""
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        price = self.price_entry.get()
        
        # Basic validation
        if not name or not phone or not email or not price:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        # Save user data
        if not os.path.exists("User Information"):
            os.makedirs("User Information")
        
        with open(f"User Information/{name}.txt", "w") as file:
            file.write(f"Name: {name}\nPhone: {phone}\nEmail: {email}\nPrice: {price}")
        
        # Generate QR code for UPI Payment Link
        payment_info = f"upi://pay?pa=7720887035@fam&pn={name}&mc=0000&tid=1234567890&tr=1&tn=Payment for services&am={price}&cu=INR"
        self.generate_qr(payment_info)

        messagebox.showinfo("Success", "Information saved successfully!")

    def back_to_main(self):
        """Go Back to Main Page"""
        self.contact_window.destroy()
        self.root.deiconify()  # Show main window again


class AnotherActionPage:
    def __init__(self, root):
        self.root = root
        self.create_another_action_page()

    def create_another_action_page(self):
        """Another Action Page with customer support, team guidelines, privacy policy"""
        self.another_action_window = tk.Toplevel(self.root)
        self.another_action_window.title("Another Action")
        self.another_action_window.geometry("600x600")
        self.another_action_window.config(bg="white")

        # Customer Support Section
        customer_support_text = """
        For any queries, please reach out to us at:
        Email: dsiddharth7d7@gmail.com
        Phone: +91 7720887035
        """
        tk.Label(self.another_action_window, text="Customer Support", bg="white", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(self.another_action_window, text=customer_support_text, bg="white", font=("Arial", 10)).pack(pady=10)

        # Team Guidelines Section
        team_guidelines_text = """
        1. Always be helpful and respectful to users.
        2. Address issues promptly and professionally.
        3. Work collaboratively to improve the app experience.
        """
        tk.Label(self.another_action_window, text="Team Guidelines", bg="white", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(self.another_action_window, text=team_guidelines_text, bg="white", font=("Arial", 10)).pack(pady=10)

        # Privacy Policy Section
        privacy_policy_text = """
        Our privacy policy is committed to protecting your personal information.
        We will never share your data with third parties without your consent.
        """
        tk.Label(self.another_action_window, text="Privacy Policy", bg="white", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(self.another_action_window, text=privacy_policy_text, bg="white", font=("Arial", 10)).pack(pady=10)

        # Back Button
        back_button = tk.Button(self.another_action_window, text="Back to Main Page", command=self.back_to_main, width=20, height=2, bg="#2196F3", fg="white",activebackground='#2196F3',activeforeground='white', font=("Arial", 12, "bold"))
        back_button.pack(pady=10)

    def back_to_main(self):
        """Go Back to Main Page"""
        self.another_action_window.destroy()
        self.root.deiconify()  # Show main window again


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
