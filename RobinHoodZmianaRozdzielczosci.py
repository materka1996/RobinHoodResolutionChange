import binascii
import os
import shutil
from tkinter import (
    messagebox,
    filedialog,
    Tk,
    ttk,
    StringVar
)

# Mapowanie rozdzielczości na wartości HEX
MAPOWANIE_WARTOSCI = {
    '640x480': '804400004044',
    '800x600': '20440000F043',
    '1024x768': '484400001644',
    '1024x576': '804400001044',
    '1280x720': 'A04400003444',
    '1920x1080': 'F04400008744',
    '1600x900': 'C84400006144',
    '1360x768': 'AA4400004044',
    '1920x1440': 'F0440000B444',
    '2560x1440': '20450000B444',
    '1440x900': '00B444006144',
}

class ResolutionChanger:
    def __init__(self, root):
        self.root = root
        self.root.title("SaveGame Res Changer Ultimate")
        self.root.geometry("400x380")
        self.file_path = ""
        self.current_file_hex = ""

        self.setup_ui()

    def setup_ui(self):
        # Nagłówek
        ttk.Label(self.root, text="Edytor Rozdzielczości Savegame", font=('Helvetica', 10, 'bold')).pack(pady=10)

        # Sekcja wyboru pliku
        self.btn_open = ttk.Button(self.root, text="Wybierz plik Profiles", command=self.select_file)
        self.btn_open.pack(pady=5)

        self.lbl_file = ttk.Label(self.root, text="Nie wybrano pliku", foreground="gray")
        self.lbl_file.pack()

        # Sekcja detekcji
        self.lbl_current_res = ttk.Label(self.root, text="Aktualna rozdzielczość: ---", font=('Helvetica', 9, 'italic'))
        self.lbl_current_res.pack(pady=10)

        # Sekcja wyboru nowej rozdzielczości
        ttk.Label(self.root, text="Wybierz nową rozdzielczość:").pack()
        self.res_var = StringVar()
        self.combobox = ttk.Combobox(self.root, textvariable=self.res_var, values=list(MAPOWANIE_WARTOSCI.keys()), state="readonly")
        self.combobox.pack(pady=5)
        
        # Przycisk zapisu
        self.btn_apply = ttk.Button(self.root, text="Zastosuj zmiany", command=self.apply_changes, state="disabled")
        self.btn_apply.pack(pady=10)

        # Sekcja przywracania backupu
        self.separator = ttk.Separator(self.root, orient='horizontal')
        self.separator.pack(fill='x', padx=20, pady=10)

        self.btn_restore = ttk.Button(self.root, text="Przywróć z kopii zapasowej (.bak)", command=self.restore_backup, state="disabled")
        self.btn_restore.pack(pady=5)
        
        self.lbl_backup_status = ttk.Label(self.root, text="", font=('Helvetica', 8))
        self.lbl_backup_status.pack()

    def check_backup_availability(self):
        """Sprawdza czy plik .bak istnieje i aktualizuje stan przycisku."""
        if self.file_path:
            backup_path = self.file_path + ".bak"
            if os.path.exists(backup_path):
                self.btn_restore.config(state="normal")
                self.lbl_backup_status.config(text="Kopia zapasowa jest dostępna", foreground="green")
            else:
                self.btn_restore.config(state="disabled")
                self.lbl_backup_status.config(text="Brak kopii zapasowej", foreground="gray")

    def select_file(self):
        path = filedialog.askopenfilename(title="Wybierz plik Profiles", filetypes=[("Pliki binarne", "*.bin;*.dat;*.sav"), ("Wszystkie", "*.*")])
        if path:
            self.file_path = path
            self.lbl_file.config(text=f"Plik: {os.path.basename(path)}", foreground="black")
            self.detect_current_resolution()
            self.check_backup_availability()

    def detect_current_resolution(self):
        try:
            with open(self.file_path, 'rb') as f:
                self.current_file_hex = binascii.hexlify(f.read()).decode('utf-8').upper()

            detected = "Nieznana (brak w bazie)"
            for res_name, hex_val in MAPOWANIE_WARTOSCI.items():
                if hex_val in self.current_file_hex:
                    detected = res_name
                    break
            
            self.lbl_current_res.config(text=f"Aktualna rozdzielczość: {detected}", foreground="blue")
            self.btn_apply.config(state="normal")
            
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie można odczytać pliku: {e}")

    def apply_changes(self):
        new_res = self.res_var.get()
        if not new_res:
            messagebox.showwarning("Uwaga", "Wybierz rozdzielczość z listy!")
            return

        if not messagebox.askyesno("Potwierdzenie", f"Czy na pewno chcesz zmienić rozdzielczość na {new_res}?"):
            return

        try:
            # Tworzenie backupu przed zmianą (jeśli jeszcze nie istnieje)
            backup_path = self.file_path + ".bak"
            if not os.path.exists(backup_path):
                shutil.copy2(self.file_path, backup_path)

            new_hex = MAPOWANIE_WARTOSCI[new_res]
            found = False
            
            updated_content = self.current_file_hex
            for old_hex in MAPOWANIE_WARTOSCI.values():
                if old_hex in updated_content:
                    updated_content = updated_content.replace(old_hex, new_hex, 1)
                    found = True
                    break

            if found:
                with open(self.file_path, 'wb') as f:
                    f.write(binascii.unhexlify(updated_content))
                
                messagebox.showinfo("Sukces", "Zmieniono rozdzielczość! Plik .bak został zachowany.")
                self.detect_current_resolution()
                self.check_backup_availability()
            else:
                messagebox.showerror("Błąd", "Nie znaleziono znanej sekwencji w pliku.")

        except Exception as e:
            messagebox.showerror("Błąd zapisu", f"Wystąpił błąd: {e}")

    def restore_backup(self):
        backup_path = self.file_path + ".bak"
        if not os.path.exists(backup_path):
            messagebox.showerror("Błąd", "Nie znaleziono pliku kopii zapasowej!")
            return

        if messagebox.askyesconfirm("Przywracanie", "Czy chcesz przywrócić plik z kopii zapasowej? Obecne zmiany zostaną nadpisane."):
            try:
                shutil.copy2(backup_path, self.file_path)
                messagebox.showinfo("Przywrócono", "Pomyślnie przywrócono oryginalny plik.")
                self.detect_current_resolution() # Aktualizacja UI
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się przywrócić pliku: {e}")

if __name__ == "__main__":
    root = Tk()
    app = ResolutionChanger(root)
    root.mainloop()
