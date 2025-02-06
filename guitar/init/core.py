import tarfile
import tkinter as tk
from tkinter import filedialog, messagebox
import os


class TarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tar Extractor & Creator")
        self.root.geometry("400x200")

        tk.Button(root, text="Create .tar", command=self.create_tar).pack(pady=10)
        tk.Button(root, text="Extract .tar", command=self.extract_tar).pack(pady=10)

    def create_tar(self):
        files = filedialog.askopenfilenames(title="Select files to archive")
        if not files:
            return

        tar_path = filedialog.asksaveasfilename(defaultextension=".tar", filetypes=[("Tar files", "*.tar")])
        if not tar_path:
            return

        try:
            with tarfile.open(tar_path, "w") as tar:
                for file in files:
                    tar.add(file, arcname=os.path.basename(file))
            messagebox.showinfo("Success", f"Created {tar_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def extract_tar(self):
        tar_path = filedialog.askopenfilename(title="Select a .tar file", filetypes=[("Tar files", "*.tar")])
        if not tar_path:
            return

        extract_dir = filedialog.askdirectory(title="Select extraction folder")
        if not extract_dir:
            return

        try:
            with tarfile.open(tar_path) as tar:
                tar.extractall(extract_dir)
            messagebox.showinfo("Success", f"Extracted to {extract_dir}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    root = tk.Tk()
    app = TarGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()